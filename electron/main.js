'use strict';
/* worthlesstask shell: a very trimmed Electron window around the local
   Python dashboard. The shell owns the backend process: it spawns it,
   follows the "worthlesstask dashboard: <url>" line on stdout, loads that
   URL, and terminates the whole process tree on quit. */
const { app, BrowserWindow, shell } = require('electron');
const { spawn } = require('child_process');
const path = require('path');
const http = require('http');

const APP_ROOT = path.join(__dirname, '..');
const PACKAGED_EXE = path.join(APP_ROOT, 'dist', 'worthlesstask', 'worthlesstask.exe');

let win = null;
let backend = null;
let backendUrl = null;
let quitting = false;

app.commandLine.appendSwitch('disable-features', 'Translate,BackForwardCache');

function spawnBackend() {
  // Source is preferred: the page served lives in the source tree, while the
  // packaged exe bakes in whichever page existed at build time.
  const fs = require('fs');
  const hasPython = (() => {
    try { require('child_process').execSync('python --version', { stdio: 'ignore' }); return true; }
    catch (_) { return false; }
  })();
  const command = hasPython
    ? { file: 'python', args: ['-m', 'worthlesstask', 'web'] }
    : fs.existsSync(PACKAGED_EXE)
      ? { file: PACKAGED_EXE, args: [] }
      : null;
  if (!command) {
    const { dialog } = require('electron');
    dialog.showErrorBox('worthlesstask', 'Neither python nor the packaged build was found.');
    app.quit();
    return;
  }
  backend = spawn(command.file, command.args, {
    cwd: APP_ROOT,
    windowsHide: true,
    stdio: ['ignore', 'pipe', 'pipe'],
  });
  const scan = (chunk) => {
    if (backendUrl) return;
    const match = String(chunk).match(/worthlesstask dashboard: (http:\/\/\S+)/);
    if (match) backendUrl = match[1];
  };
  backend.stdout.on('data', scan);
  backend.stderr.on('data', scan);
  backend.on('exit', () => { if (!quitting) app.quit(); });
}

function probe(url) {
  return new Promise((resolve) => {
    const req = http.get(url + '/api/health', { timeout: 900 }, (res) => {
      res.resume();
      resolve(res.statusCode === 200);
    });
    req.on('error', () => resolve(false));
    req.on('timeout', () => { req.destroy(); resolve(false); });
  });
}

async function waitBackend() {
  const deadline = Date.now() + 30000;
  while (Date.now() < deadline) {
    if (backendUrl && await probe(backendUrl)) return;
    await new Promise((r) => setTimeout(r, 400));
  }
  throw new Error('the dashboard backend did not come up');
}

function createWindow() {
  win = new BrowserWindow({
    width: 1240,
    height: 840,
    minWidth: 760,
    minHeight: 560,
    backgroundColor: '#08090c',
    show: false,
    autoHideMenuBar: true,
    title: 'SteamTasks',
    webPreferences: {
      contextIsolation: true,
      nodeIntegration: false,
      sandbox: true,
      devTools: false,
      spellcheck: false,
    },
  });
  win.removeMenu();
  // Links that leave the dashboard (none expected, but be safe) open outside.
  win.webContents.setWindowOpenHandler(({ url }) => {
    shell.openExternal(url);
    return { action: 'deny' };
  });
  win.once('ready-to-show', () => win.show());
  win.on('closed', () => { win = null; });
  win.loadURL(backendUrl);
}

function killBackend() {
  if (!backend || backend.exitCode !== null) return;
  // The packaged backend spawns game workers; take down the whole tree.
  if (process.platform === 'win32') {
    spawn('taskkill', ['/pid', String(backend.pid), '/T', '/F'], { windowsHide: true });
  } else {
    backend.kill('SIGTERM');
  }
}

app.whenReady().then(async () => {
  spawnBackend();
  try {
    await waitBackend();
  } catch (err) {
    const { dialog } = require('electron');
    dialog.showErrorBox('worthlesstask', String(err.message || err));
    app.quit();
    return;
  }
  createWindow();
});

app.on('window-all-closed', () => app.quit());
app.on('before-quit', () => { quitting = true; killBackend(); });
app.on('quit', () => killBackend());
