"""Local dashboard page (single embedded document, no build step).

One design language: matte black surfaces, glossy white accents, cool white
glows. No color accents anywhere — state is carried by brightness and glow.
The Home tab is a live summary; Games is the workspace. A small lightning
pet (Molniya) sits in the corner and charges while a session runs.
"""
PAGE = r'''<!DOCTYPE html>
<html lang="en" data-theme="dark"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="robots" content="noindex,nofollow"><title>SteamTasks</title><link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 64 64'%3E%3Crect x='6' y='6' width='52' height='52' rx='16' fill='%230e1014' stroke='%233a4150' stroke-width='2'/%3E%3Cpath d='M36 14 22 36h9l-3 14 14-22h-9z' fill='%23f2f5fa'/%3E%3C/svg%3E">
<style>
:root{color-scheme:dark;
--bg:#08090c;--surface:#0e1014;--surface-2:#14171d;--surface-3:#1c2027;--surface-4:#242933;
--ink:#f3f5f9;--ink-2:#aeb5c1;--ink-3:#7e8694;--ink-4:#5b6270;
--line:rgba(255,255,255,.08);--line-2:rgba(255,255,255,.15);
--gloss:linear-gradient(168deg,#ffffff 8%,#dde1e8 58%,#c6ccd6 100%);
--glow-soft:0 0 22px -8px rgba(205,220,255,.22);
--shadow:inset 0 1px 0 rgba(255,255,255,.05),0 22px 48px -28px rgba(0,0,0,.9);
--r-lg:18px;--r-md:13px;--r-sm:9px;--pill:999px;
--ease:cubic-bezier(.22,.8,.3,1);
--ok:#8fe3b4;--warn:#ddc491;--danger:#f0a3a3;
--ok-soft:rgba(143,227,180,.1);--warn-soft:rgba(221,196,145,.1);--danger-soft:rgba(240,163,163,.1)}
*{box-sizing:border-box}
html{background:var(--bg);scroll-behavior:smooth}
body{margin:0;background:var(--bg);color:var(--ink);font:14px/1.55 "Segoe UI Variable Text","Segoe UI",Inter,system-ui,-apple-system,sans-serif;letter-spacing:.1px;min-height:100vh;overflow-x:hidden}
button,input,select{font:inherit;color:inherit}
button{cursor:pointer}
::selection{background:rgba(205,220,255,.28);color:#fff}
*{scrollbar-width:thin;scrollbar-color:var(--surface-4) transparent}
*::-webkit-scrollbar{width:8px;height:8px}
*::-webkit-scrollbar-thumb{background:var(--surface-4);border-radius:999px;border:2px solid var(--bg)}
*::-webkit-scrollbar-thumb:hover{background:#31394a}
*::-webkit-scrollbar-track{background:transparent}
:focus-visible{outline:1px solid rgba(230,238,255,.6);outline-offset:2px;border-radius:8px;box-shadow:0 0 0 4px rgba(205,220,255,.12)}
button:disabled{cursor:default;opacity:.35}
[hidden]{display:none!important}
h1,h2,h3{margin:0;font-weight:650;letter-spacing:-.2px;line-height:1.25}
p{margin:0}
svg{display:block}
.top-glow{position:fixed;inset:0;z-index:0;pointer-events:none;background:radial-gradient(900px 380px at 50% -140px,rgba(215,228,255,.075),transparent 70%)}
.shell{position:relative;z-index:1}
.nav{position:sticky;top:0;z-index:20;display:grid;grid-template-columns:1fr auto 1fr;align-items:center;gap:16px;padding:11px max(26px,calc((100vw - 1240px)/2 + 26px));background:rgba(8,9,12,.82);backdrop-filter:blur(22px) saturate(150%);-webkit-backdrop-filter:blur(22px) saturate(150%);border-bottom:1px solid var(--line)}
.nav-left{display:flex;align-items:center;gap:12px;justify-self:start;min-width:0}
.nav-right{display:flex;align-items:center;justify-content:flex-end;justify-self:end;min-width:0}
.brand{display:flex;align-items:center;gap:10px;font-weight:700;font-size:13px;letter-spacing:.4px;color:var(--ink);text-decoration:none}
.mark{width:26px;height:26px;flex:none;display:grid;place-items:center;border-radius:9px;background:var(--gloss);box-shadow:0 4px 14px -6px rgba(220,232,255,.55),inset 0 1px 0 rgba(255,255,255,.9)}
.mark svg{width:14px;height:14px}
.i{width:17px;height:17px;flex:none;fill:none;stroke:currentColor;stroke-width:1.4;stroke-linecap:round;stroke-linejoin:round}
.lang{display:inline-flex;align-items:center;gap:2px;padding:2px;border-radius:var(--pill);background:var(--surface-2);border:1px solid var(--line)}
.lang-btn{border:0;background:transparent;color:var(--ink-3);font-size:10.5px;font-weight:700;letter-spacing:.6px;padding:4px 9px;border-radius:var(--pill);transition:color .18s var(--ease),background .18s var(--ease)}
.lang-btn:hover{color:var(--ink)}
.lang-btn[aria-pressed=true]{color:#0b0c0f;background:var(--gloss);box-shadow:0 2px 8px -3px rgba(220,232,255,.5)}
.tabs{position:relative;display:flex;gap:2px;padding:3px;justify-self:center;border-radius:var(--pill);background:var(--surface-2);border:1px solid var(--line)}
.tab{position:relative;z-index:1;display:inline-flex;align-items:center;gap:8px;border:0;background:transparent;color:var(--ink-3);padding:7px 16px;border-radius:var(--pill);font-size:12.5px;font-weight:600;white-space:nowrap;transition:color .18s var(--ease)}
.tab .i{transition:transform .25s var(--ease)}
.tab:hover{color:var(--ink)}
.tab:hover .i{transform:translateY(-1px)}
.tab[aria-selected=true]{color:#0b0c0f}
.tab[aria-selected=true] .i{transform:none}
.tab-indicator{position:absolute;top:3px;left:0;height:calc(100% - 6px);width:0;border-radius:var(--pill);z-index:0;pointer-events:none;background:var(--gloss);box-shadow:0 6px 16px -8px rgba(0,0,0,.8),inset 0 1px 0 rgba(255,255,255,.9);transition:transform .35s var(--ease),width .35s var(--ease)}
.chip{display:flex;align-items:center;gap:9px;padding:7px 13px;border-radius:var(--pill);background:var(--surface-2);border:1px solid var(--line);font-size:11px;color:var(--ink-2);white-space:nowrap}
.chip .dot{width:7px;height:7px;border-radius:50%;background:#8fe3b4;box-shadow:0 0 10px rgba(143,227,180,.8);flex:none;animation:breathe 2.4s ease-in-out infinite}
.chip .dot.off{background:#f0a3a3;box-shadow:0 0 10px rgba(240,163,163,.8);animation:breathe 1.6s ease-in-out infinite}
main{max-width:1240px;margin:0 auto;padding:0 26px 90px}
.view{will-change:auto}
.view-inner.is-entering{animation:viewIn .32s var(--ease) both}
.panel{position:relative;background:linear-gradient(180deg,rgba(255,255,255,.022),transparent 34%),var(--surface);border:1px solid var(--line);border-radius:var(--r-lg);box-shadow:var(--shadow);overflow:hidden;transition:border-color .25s var(--ease),box-shadow .25s var(--ease)}
.panel:hover{border-color:var(--line-2);box-shadow:var(--shadow),var(--glow-soft)}
.head{display:flex;align-items:center;justify-content:space-between;gap:12px;min-height:48px;padding:11px 18px;border-bottom:1px solid var(--line);background:linear-gradient(180deg,rgba(255,255,255,.025),transparent)}
.head h2{display:flex;align-items:center;gap:9px;font-size:11.5px;font-weight:700;letter-spacing:.09em;text-transform:uppercase;color:var(--ink-2)}
.head h2 .i{width:15px;height:15px;color:var(--ink)}
.head small{color:var(--ink-3);font-size:11.5px}
.head-right{display:flex;align-items:center;gap:8px;flex-wrap:wrap}
.counter{min-width:24px;height:22px;padding:0 8px;border:1px solid var(--line-2);border-radius:999px;background:var(--surface-2);color:var(--ink-2);font-size:11px;font-weight:700;display:inline-flex;align-items:center;justify-content:center;font-variant-numeric:tabular-nums}
.counter.bump{animation:counterPop .34s var(--ease)}
.body{padding:16px 18px 18px}
.hint{color:var(--ink-3);font-size:12.5px;margin-top:10px}.hint:empty{display:none}
.status-line{min-height:20px;padding:8px 0 0;font-size:12.5px;color:var(--ink-2)}
.alert{border:1px solid rgba(240,163,163,.4);border-left-width:3px;border-radius:var(--r-sm);background:var(--danger-soft);color:#f6c6c6;padding:11px 13px;font-size:12.5px;margin-bottom:14px;animation:fadeUp .3s var(--ease) both}
.btn{position:relative;display:inline-flex;align-items:center;justify-content:center;gap:7px;border:1px solid var(--line-2);background:linear-gradient(180deg,rgba(255,255,255,.03),transparent 60%),var(--surface-2);color:var(--ink);border-radius:var(--r-sm);padding:0 14px;font-size:12.5px;font-weight:600;min-height:34px;white-space:nowrap;box-shadow:inset 0 1px 0 rgba(255,255,255,.06)}
.btn:hover:not(:disabled){background:var(--surface-3);border-color:rgba(255,255,255,.24);box-shadow:inset 0 1px 0 rgba(255,255,255,.09),0 0 14px -6px rgba(205,220,255,.35)}
.btn:active:not(:disabled){background:var(--surface-4)}
.btn .i{color:var(--ink-2)}
.btn:hover:not(:disabled) .i{color:var(--ink)}
.btn.primary{background:var(--gloss);border-color:transparent;color:#0b0c0f;box-shadow:inset 0 1px 0 rgba(255,255,255,.9),0 8px 22px -10px rgba(215,228,255,.55)}
.btn.primary:hover:not(:disabled){background:linear-gradient(168deg,#ffffff 4%,#e6eaf1 60%,#d2d8e2 100%);box-shadow:inset 0 1px 0 rgba(255,255,255,.9),0 10px 26px -10px rgba(215,228,255,.7)}
.btn.primary .i{color:#2a3140}
.btn.danger{background:var(--danger-soft);border-color:rgba(240,163,163,.35);color:var(--danger)}
.btn.danger:hover:not(:disabled){background:rgba(240,163,163,.18);box-shadow:0 0 14px -6px rgba(240,163,163,.4)}
.btn.ghost{background:transparent;border-color:transparent;color:var(--ink-3);box-shadow:none}
.btn.ghost:hover:not(:disabled){color:var(--ink);background:var(--surface-2)}
.btn.small{min-height:28px;padding:0 10px;font-size:12px;border-radius:7px}
.btn.wide{width:100%}
.btn.is-running{border-color:rgba(205,220,255,.35);background:rgba(205,220,255,.1);color:#e8eeff;opacity:1;box-shadow:0 0 18px -6px rgba(205,220,255,.5);animation:livePulse 2.2s ease-out infinite}
.btn.is-running .i{color:#e8eeff}
input,select{background:var(--bg);border:1px solid var(--line-2);border-radius:var(--r-sm);padding:0 12px;height:36px;min-width:0;transition:border-color .16s var(--ease),box-shadow .16s var(--ease)}
input::placeholder{color:var(--ink-4)}
input:focus,select:focus{outline:none;border-color:rgba(225,235,255,.55);box-shadow:0 0 0 3px rgba(205,220,255,.12)}
.search-row{display:flex;gap:9px}
.search-row input{flex:1}
.results{display:grid;gap:7px;max-height:340px;overflow:auto;padding-right:3px}
.result-area{min-height:100px;padding-top:8px}
.result{display:flex;align-items:center;gap:12px;width:100%;text-align:left;padding:10px 12px;border:1px solid var(--line);border-radius:var(--r-sm);background:var(--surface-2);transition:border-color .18s var(--ease),background .18s var(--ease),box-shadow .18s var(--ease);animation:slideIn .26s var(--ease) both}
.result:hover{border-color:var(--line-2);background:var(--surface-3)}
.result[aria-pressed=true]{border-color:rgba(225,235,255,.55);background:rgba(205,220,255,.08);box-shadow:var(--glow-soft)}
.result-body{flex:1;min-width:0}
.result .name{font-weight:600;font-size:13.5px;overflow-wrap:anywhere}
.result .meta{color:var(--ink-3);font-size:11.5px;margin-top:2px;overflow-wrap:anywhere}
.check{width:20px;height:20px;flex:none;display:grid;place-items:center;border:1px solid var(--line-2);border-radius:6px;background:var(--surface)}
.check .i{width:12px;height:12px;color:#0b0c0f;opacity:0}
.result[aria-pressed=true] .check{background:var(--gloss);border-color:transparent;box-shadow:0 0 12px -3px rgba(215,228,255,.6)}
.result[aria-pressed=true] .check .i{opacity:1}
.empty{padding:20px 14px;border:1px dashed var(--line-2);border-radius:var(--r-sm);color:var(--ink-3);font-size:12.5px;text-align:center;background:rgba(255,255,255,.012)}
.pulse{height:44px;border-radius:var(--r-sm);background:linear-gradient(90deg,var(--surface-2),var(--surface-3),var(--surface-2));background-size:220% 100%;animation:sweep 1.2s linear infinite}
.footer-row{display:flex;align-items:center;gap:9px;flex-wrap:wrap;margin-top:12px;padding-top:12px;border-top:1px solid var(--line)}
.sel-label{flex:1;min-width:0;font-size:12.5px;color:var(--ink-3);overflow-wrap:anywhere}
.library{display:grid;gap:8px}
.game{display:flex;flex-wrap:wrap;align-items:center;gap:10px 12px;padding:12px 14px;border:1px solid var(--line);border-radius:var(--r-md);background:linear-gradient(180deg,rgba(255,255,255,.02),transparent 50%),var(--surface-2);transition:border-color .2s var(--ease),background .2s var(--ease),box-shadow .2s var(--ease);animation:pop .26s var(--ease) both}
.game:hover{border-color:var(--line-2);background:var(--surface-3)}
.game.active{border-color:rgba(225,235,255,.5);background:rgba(205,220,255,.07);box-shadow:inset 3px 0 0 #dfe8ff,0 0 24px -10px rgba(205,220,255,.4)}
.icon-box{width:40px;height:40px;flex:none;display:grid;place-items:center;overflow:hidden;border:1px solid var(--line-2);border-radius:10px;background:var(--surface);color:var(--ink-4);font-size:11px;font-weight:700}
.icon-box img{width:100%;height:100%;object-fit:cover;transition:transform .35s var(--ease)}
.game:hover .icon-box img{transform:scale(1.08)}
.game-info{flex:1 1 210px;min-width:0}
.game-title-row{display:flex;align-items:center;gap:7px;flex-wrap:wrap}
.game-name{font-size:14px;font-weight:700;color:var(--ink);overflow-wrap:anywhere}
.game-meta{color:var(--ink-3);font-size:11.5px;margin-top:3px;overflow-wrap:anywhere}
.game-tags{display:flex;align-items:center;gap:6px;flex-wrap:wrap;margin-top:6px}
.badge{flex:none;padding:3px 10px;border:1px solid rgba(143,227,180,.35);border-radius:999px;background:var(--ok-soft);color:var(--ok);font-size:10.5px;font-weight:700;letter-spacing:.05em;text-transform:uppercase}
.badge.warn{border-color:rgba(221,196,145,.35);background:var(--warn-soft);color:var(--warn)}
.badge.run{border-color:rgba(205,220,255,.4);background:rgba(205,220,255,.1);color:#dfe8ff;animation:halo 2.8s ease-out infinite}
.badge.sub{border-color:var(--line-2);background:var(--surface-2);color:var(--ink-2);text-transform:none;letter-spacing:.01em;font-weight:600}
.badge.quest{border-color:rgba(205,220,255,.35);background:rgba(205,220,255,.08);color:#dfe8ff;text-transform:none;letter-spacing:.01em;font-weight:650}
.reason{font-size:12px;color:var(--warn);padding:9px 11px;flex:1 1 100%;border:1px solid rgba(221,196,145,.25);border-left:3px solid rgba(221,196,145,.5);border-radius:var(--r-sm);background:var(--warn-soft)}
.game-actions{display:flex;align-items:center;gap:6px;flex-wrap:wrap;justify-content:flex-end;margin-left:auto}
.exe-row{display:flex;gap:8px;flex:1 1 100%;padding-top:4px}
.exe-row input{flex:1;min-width:0;height:32px}
.icon-picker{display:none}
.session-name{font-size:19px;font-weight:700;letter-spacing:-.3px;margin:14px 0 5px;overflow-wrap:anywhere}
.session-state{min-height:21px;font-size:12.5px;color:var(--ink-2)}
.session-top{display:flex;align-items:flex-start;justify-content:space-between;gap:14px;flex-wrap:wrap}
.session-actions{display:flex;gap:8px;flex:none;width:100%}
.session-actions .btn{flex:1}
.stats{display:grid;grid-template-columns:1fr 1fr;gap:9px;margin-top:14px}
.stat{padding:11px 13px;border:1px solid var(--line);border-radius:var(--r-sm);background:var(--surface-2)}
.stat small{display:block;color:var(--ink-3);font-size:10.5px;letter-spacing:.07em;text-transform:uppercase;font-weight:650}
.stat strong{display:block;margin-top:4px;font-size:17px;font-weight:700;font-variant-numeric:tabular-nums;color:var(--ink)}
.session-note{margin-top:12px;padding:10px 12px;border:1px solid var(--line);border-left:3px solid rgba(205,220,255,.5);border-radius:var(--r-sm);background:var(--surface-2);font-size:12.5px;color:var(--ink-2);min-height:38px}
.quest-list{display:grid;gap:8px}
.quest-card{display:flex;align-items:center;justify-content:space-between;gap:10px;padding:10px 12px;border:1px solid var(--line);border-radius:var(--r-sm);background:var(--surface-2);transition:border-color .25s var(--ease),background .25s var(--ease)}
.quest-card.enrolled{border-color:rgba(205,220,255,.35);background:rgba(205,220,255,.06)}
.quest-card.completed{border-color:rgba(143,227,180,.35);background:var(--ok-soft)}
.quest-main{min-width:0;flex:1}
.quest-title{font-size:13px;font-weight:650;color:var(--ink);overflow-wrap:anywhere}
.quest-sub{font-size:11.5px;color:var(--ink-3);margin-top:2px;overflow-wrap:anywhere}
.quest-bar{height:4px;border-radius:999px;background:var(--surface-4);margin-top:7px;overflow:hidden;position:relative}
.quest-bar>span{display:block;height:100%;width:0;background:var(--gloss);border-radius:999px;box-shadow:0 0 10px rgba(215,228,255,.55);transition:width .8s var(--ease);position:relative;overflow:hidden}
.quest-bar>span:after{content:"";position:absolute;inset:0;background:linear-gradient(90deg,transparent,rgba(255,255,255,.7),transparent);background-size:220% 100%;animation:sweep 1.6s linear infinite}
.quest-card.completed .quest-bar>span:after{animation:none;background:none}
.queue-settings{display:flex;align-items:center;gap:9px;color:var(--ink-2);font-size:12.5px;margin-bottom:12px}
.queue-settings input{width:76px;height:32px}
.queue{list-style:none;margin:0 0 12px;padding:0;display:grid;gap:7px;min-height:28px}
.queue-item{display:flex;align-items:center;gap:9px;padding:8px 10px;border:1px solid var(--line);border-radius:var(--r-sm);background:var(--surface-2);font-size:12.5px;cursor:grab;position:relative;overflow:hidden;transition:border-color .18s var(--ease),background .18s var(--ease),box-shadow .18s var(--ease),opacity .18s var(--ease);animation:pop .24s var(--ease) both}
.queue-item:active{cursor:grabbing}
.queue-item.dragging{opacity:.45;border-style:dashed}
.queue-item.drop-before{box-shadow:0 -2px 0 0 rgba(225,235,255,.6)}
.queue-item.drop-after{box-shadow:0 2px 0 0 rgba(225,235,255,.6)}
.queue-item.current{border-color:rgba(205,220,255,.45);background:rgba(205,220,255,.07)}
.q-grip{width:8px;height:12px;flex:none;opacity:.35;background-image:radial-gradient(circle,currentColor 1px,transparent 1.15px);background-size:4px 4px;background-position:1px 1px;background-repeat:repeat}
.q-num{flex:none;min-width:18px;text-align:center;font-size:11px;font-weight:700;color:var(--ink-3);font-variant-numeric:tabular-nums}
.queue-item.current .q-num{color:#dfe8ff}
.q-name{flex:1;min-width:0;overflow:hidden;text-overflow:ellipsis;white-space:nowrap;font-weight:600}
.q-min{color:var(--ink-3);font-size:11px;flex:none;font-variant-numeric:tabular-nums}
.q-order{display:grid;flex:none}
.q-move,.q-del{border:0;background:transparent;color:var(--ink-3);display:grid;place-items:center;padding:2px 4px;border-radius:4px;line-height:1}
.q-del{padding:3px 5px}
.q-move:hover:not(:disabled),.q-del:hover:not(:disabled){color:var(--ink);background:var(--surface-3)}
.q-del:hover:not(:disabled){color:var(--danger)}
.q-bar{position:absolute;left:0;bottom:0;height:2px;width:0;background:var(--gloss);box-shadow:0 0 8px rgba(215,228,255,.7);transition:width 1s linear}
.queue-actions{display:flex;gap:8px}
.queue-actions .btn{flex:1}
.queue-status{min-height:18px;margin-top:10px;font-size:12px;color:var(--ink-3)}
.toast{position:fixed;right:26px;bottom:110px;z-index:60;max-width:390px;padding:14px 17px;border-radius:var(--r-md);font-size:13px;border:1px solid var(--line-2);background:rgba(20,23,29,.92);backdrop-filter:blur(18px);box-shadow:var(--shadow),var(--glow-soft);animation:fadeUp .3s var(--ease) both}
.toast.error{border-color:rgba(240,163,163,.45);color:#f6c6c6}
.modal-scrim{position:fixed;inset:0;z-index:70;display:grid;place-items:center;padding:20px;background:rgba(5,6,8,.66);backdrop-filter:blur(9px);opacity:0;transition:opacity .18s var(--ease)}
.modal-scrim.is-open{opacity:1}
.modal{width:min(440px,100%);padding:22px 24px;border-radius:var(--r-lg);border:1px solid var(--line-2);background:linear-gradient(180deg,rgba(255,255,255,.03),transparent 40%),var(--surface);box-shadow:var(--shadow),0 30px 80px -20px rgba(0,0,0,.9)}
.modal-title{margin:0;font-size:16.5px;font-weight:650}
.modal-msg{margin:9px 0 0;color:var(--ink-2);font-size:13px;line-height:1.6}
.modal-input{margin-top:15px;width:100%}
.modal-actions{display:flex;justify-content:flex-end;gap:9px;margin-top:20px}
.modal-actions .btn{min-width:104px}
.icon-set{position:absolute;width:0;height:0;overflow:hidden}
.i.sm{width:15px;height:15px}
.i.xs{width:13px;height:13px}
.i.xxs{width:12px;height:12px}
.i.ph{width:15px;height:15px;opacity:.4}
.bl{white-space:nowrap}
/* ---------- summary (Home) ---------- */
.sum-grid{display:grid;grid-template-columns:minmax(0,1.5fr) minmax(300px,1fr);gap:16px;align-items:start;margin-top:22px}
.sum-col{display:grid;gap:16px;min-width:0}
.sum-col .panel{animation:fadeUp .45s var(--ease) both}
.sum-col .panel:nth-child(2){animation-delay:.07s}
.sum-col .panel:nth-child(3){animation-delay:.14s}
.sum-name{font-size:21px;font-weight:700;letter-spacing:-.4px;overflow-wrap:anywhere}
.sum-state{min-height:20px;font-size:12.5px;color:var(--ink-2);margin-top:3px}
.sum-about{margin-top:18px;padding:16px 18px;border:1px solid var(--line);border-radius:var(--r-md);background:var(--surface);color:var(--ink-3);font-size:12.5px;line-height:1.65;animation:fadeUp .45s .2s var(--ease) both}
.sum-about b{color:var(--ink-2);font-weight:650}
.mini-row{display:flex;align-items:center;gap:9px;padding:8px 11px;border:1px solid var(--line);border-radius:var(--r-sm);background:var(--surface-2);font-size:12.5px;animation:pop .24s var(--ease) both}
.mini-row.current{border-color:rgba(205,220,255,.45);background:rgba(205,220,255,.07)}
.mini-row .q-name{font-weight:600}
.mini-row .mini-meta{color:var(--ink-3);font-size:11px;flex:none;font-variant-numeric:tabular-nums}
/* ---------- pet: Molniya ---------- */
.pet{position:fixed;right:22px;bottom:22px;z-index:50;display:grid;place-items:center;cursor:pointer;user-select:none;-webkit-user-select:none}
.pet-body{width:56px;height:56px;border-radius:50%;display:grid;place-items:center;background:radial-gradient(circle at 34% 26%,rgba(255,255,255,.1),transparent 46%),var(--surface-2);border:1px solid var(--line-2);box-shadow:inset 0 1px 0 rgba(255,255,255,.1),0 14px 30px -14px rgba(0,0,0,.9),0 0 20px -8px rgba(205,220,255,.28);animation:petBob 3.8s ease-in-out infinite;transition:box-shadow .5s var(--ease)}
.pet:hover .pet-body{border-color:rgba(225,235,255,.4)}
.pet-bolt{width:26px;height:26px}
.pet-bolt .bolt-body{fill:url(#petGrad);stroke:rgba(255,255,255,.5);stroke-width:.6}
.pet-eye{fill:#0b0c0f;animation:blink 4.6s infinite}
.pet-lid{stroke:#0b0c0f;stroke-width:1;stroke-linecap:round;opacity:0}
.pet-orbit{position:absolute;inset:-4px;border-radius:50%;border:1px dashed rgba(205,220,255,.45);opacity:0;pointer-events:none}
.pet-orbit.b{inset:-10px;border-color:rgba(205,220,255,.25)}
.pet-z{position:absolute;font-size:12px;font-weight:700;color:var(--ink-3);opacity:0;pointer-events:none}
.pet-z.z1{top:-6px;right:34px}
.pet-z.z2{top:2px;right:16px;font-size:9px}
.pet[data-state=idle] .pet-body{animation-duration:4.4s}
.pet[data-state=work] .pet-body{animation-duration:1.7s;box-shadow:inset 0 1px 0 rgba(255,255,255,.12),0 14px 30px -14px rgba(0,0,0,.9),0 0 30px -6px rgba(215,228,255,.65)}
.pet[data-state=work] .pet-orbit{opacity:1;animation:sparkOrbit 2.6s linear infinite}
.pet[data-state=work] .pet-orbit.b{animation-duration:3.8s;animation-direction:reverse}
.pet[data-state=sleep] .pet-body{animation-duration:6.5s;opacity:.6;box-shadow:inset 0 1px 0 rgba(255,255,255,.06),0 10px 24px -14px rgba(0,0,0,.9)}
.pet[data-state=sleep] .pet-eye{opacity:0;animation:none}
.pet[data-state=sleep] .pet-lid{opacity:1}
.pet[data-state=sleep] .pet-z{animation:zfloat 3.2s ease-in-out infinite}
.pet[data-state=sleep] .pet-z.z2{animation-delay:1.6s}
.pet-ring{position:absolute;inset:-2px;border-radius:50%;pointer-events:none;opacity:0}
.pet[data-state=work] .pet-ring{opacity:1}
.pet-bubble{position:absolute;right:0;bottom:72px;width:236px;padding:13px 15px;border-radius:var(--r-md);border:1px solid var(--line-2);background:rgba(17,20,26,.94);backdrop-filter:blur(16px);box-shadow:var(--shadow),var(--glow-soft);opacity:0;transform:translateY(8px);pointer-events:none;transition:opacity .22s var(--ease),transform .22s var(--ease)}
.pet-bubble.open{opacity:1;transform:none;pointer-events:auto}
.pet-bubble .pb-name{display:flex;align-items:baseline;justify-content:space-between;font-weight:700;font-size:13.5px}
.pet-bubble .pb-lvl{color:var(--ink-3);font-size:11px;font-weight:700;font-variant-numeric:tabular-nums}
.pet-bubble .pb-bar{height:4px;border-radius:999px;background:var(--surface-4);margin-top:9px;overflow:hidden}
.pet-bubble .pb-bar span{display:block;height:100%;background:var(--gloss);box-shadow:0 0 8px rgba(215,228,255,.6);transition:width .6s var(--ease)}
.pet-bubble .pb-mood{margin-top:9px;font-size:11.5px;color:var(--ink-3);line-height:1.5}
@keyframes petBob{0%,100%{transform:translateY(0)}50%{transform:translateY(-7px)}}
@keyframes blink{0%,93%,100%{transform:scaleY(1)}96%{transform:scaleY(.1)}}
@keyframes sparkOrbit{to{transform:rotate(360deg)}}
@keyframes zfloat{0%{opacity:0;transform:translateY(4px)}25%{opacity:.9}100%{opacity:0;transform:translateY(-16px)}}
@keyframes fadeUp{from{opacity:0;transform:translateY(12px)}to{opacity:1;transform:none}}
@keyframes viewIn{from{opacity:0;transform:translateY(8px)}to{opacity:1;transform:none}}
@keyframes pop{from{opacity:0;transform:scale(.97)}to{opacity:1;transform:none}}
@keyframes slideIn{from{opacity:0;transform:translateX(-8px)}to{opacity:1;transform:none}}
@keyframes breathe{0%,100%{opacity:1}50%{opacity:.35}}
@keyframes halo{0%{box-shadow:0 0 0 0 rgba(205,220,255,.3)}70%{box-shadow:0 0 0 8px rgba(205,220,255,0)}100%{box-shadow:0 0 0 0 rgba(205,220,255,0)}}
@keyframes sweep{to{background-position:-220% 0}}
@keyframes counterPop{0%{transform:scale(.86)}60%{transform:scale(1.1)}100%{transform:scale(1)}}
@keyframes livePulse{0%,100%{box-shadow:0 0 0 0 rgba(205,220,255,.28)}50%{box-shadow:0 0 0 8px rgba(205,220,255,0)}}
@media (max-width:980px){.sum-grid{grid-template-columns:minmax(0,1fr)}.nav{grid-template-columns:1fr auto;row-gap:10px;padding:11px 16px}.tabs{grid-row:2;grid-column:1/-1;justify-self:stretch;width:100%}.tab{flex:1;justify-content:center;padding:8px 10px}main{padding:0 16px 96px}}
@media (max-width:560px){.brand-name{display:none}.session-top .session-actions{width:100%}.footer-row{flex-direction:column;align-items:stretch}.footer-row .btn{width:100%}.queue-actions{flex-direction:column}.search-row{flex-direction:column}.head{padding:10px 14px}.body{padding:14px}.game{padding:12px}.game-actions{margin-left:0;width:100%;justify-content:flex-start}.exe-row{flex-direction:column}.modal-actions{flex-direction:column-reverse}.modal-actions .btn{width:100%}}
@media (prefers-reduced-motion:reduce){*{animation-duration:.001s!important;transition-duration:.001s!important}}
</style></head><body>
<svg class="icon-set" aria-hidden="true" focusable="false" xmlns="http://www.w3.org/2000/svg"><defs>
<linearGradient id="petGrad" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#ffffff"/><stop offset="1" stop-color="#c3cad6"/></linearGradient>
<symbol id="ic-bolt" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.4" stroke-linecap="round" stroke-linejoin="round"><path d="M13.2 2.6 5.8 13.4h4.9l-1.4 8 7.9-11.2h-5.1z"/></symbol>
<symbol id="ic-search" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.4" stroke-linecap="round" stroke-linejoin="round"><circle cx="10.4" cy="10.4" r="6.1"/><path d="M14.9 14.9 20.4 20.4"/><path d="M8.2 10.4h4.4"/></symbol>
<symbol id="ic-library" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.4" stroke-linecap="round" stroke-linejoin="round"><path d="M4.6 19.4V7.8h3.4v11.6"/><path d="M9.2 19.4V6.4h3.4v13"/><path d="M14.6 19.4 17.4 6.6l2.2.5-2.6 12.3"/><path d="M3.2 19.4h17.6"/></symbol>
<symbol id="ic-session" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.4" stroke-linecap="round" stroke-linejoin="round"><path d="M13.9 18.7A8.3 8.3 0 1 1 18.7 13.9"/><circle cx="12" cy="12" r="2.5"/></symbol>
<symbol id="ic-queue" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.4" stroke-linecap="round" stroke-linejoin="round"><path d="M4.2 7.4h9.6"/><path d="M7 12h9.6"/><path d="M4.2 16.6h9.6"/><path d="M18.4 5.8v12.4"/></symbol>
<symbol id="ic-play" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.4" stroke-linecap="round" stroke-linejoin="round"><path d="M8.4 5.6 18.6 11.6a.45.45 0 0 1 0 .8L8.4 18.4a.45.45 0 0 1-.7-.4V6a.45.45 0 0 1 .7-.4z"/></symbol>
<symbol id="ic-stop" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.4" stroke-linecap="round" stroke-linejoin="round"><path d="M8.6 6.6h6.8a2 2 0 0 1 2 2v6.8a2 2 0 0 1-2 2H8.6a2 2 0 0 1-2-2V8.6a2 2 0 0 1 2-2z"/></symbol>
<symbol id="ic-trash" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.4" stroke-linecap="round" stroke-linejoin="round"><path d="M4.6 7.4h14.8"/><path d="M9.4 7.4V5.2h5.2v2.2"/><path d="M6.6 7.4 7.5 18.6a1.5 1.5 0 0 0 1.5 1.4h6a1.5 1.5 0 0 0 1.5-1.4l.9-11.2"/><path d="M10.5 10.8v5.6M13.5 10.8v5.6"/></symbol>
<symbol id="ic-edit" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.4" stroke-linecap="round" stroke-linejoin="round"><path d="M14.6 5.2 18.8 9.4 8.6 19.6 4.2 20.8 5.4 16.4z"/><path d="M12.8 7 17 11.2"/></symbol>
<symbol id="ic-plus" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.4" stroke-linecap="round" stroke-linejoin="round"><path d="M12 5.6v12.8"/><path d="M5.6 12h12.8"/></symbol>
<symbol id="ic-up" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.4" stroke-linecap="round" stroke-linejoin="round"><path d="M12 18.6V5.4"/><path d="M6.3 11.1 12 5.4l5.7 5.7"/></symbol>
<symbol id="ic-down" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.4" stroke-linecap="round" stroke-linejoin="round"><path d="M12 5.4v13.2"/><path d="M6.3 12.9 12 18.6l5.7-5.7"/></symbol>
<symbol id="ic-close" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.4" stroke-linecap="round" stroke-linejoin="round"><path d="M6.5 6.5 17.5 17.5"/><path d="M17.5 6.5 6.5 17.5"/></symbol>
<symbol id="ic-check" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.4" stroke-linecap="round" stroke-linejoin="round"><path d="M5.2 12.6 9.9 17.3 18.8 6.7"/></symbol>
<symbol id="ic-sync" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.4" stroke-linecap="round" stroke-linejoin="round"><path d="M20 11a8.1 8.1 0 0 0-15.5-2m-.5-4v4h4"/><path d="M4 13a8.1 8.1 0 0 0 15.5 2m.5 4v-4h-4"/></symbol>
<symbol id="ic-image" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.4" stroke-linecap="round" stroke-linejoin="round"><path d="M4.4 6.2h15.2a1.4 1.4 0 0 1 1.4 1.4v8.8a1.4 1.4 0 0 1-1.4 1.4H4.4A1.4 1.4 0 0 1 3 16.4V7.6a1.4 1.4 0 0 1 1.4-1.4z"/><path d="M3.4 16.4 9.1 11l3.9 3.5 2.7-2.3 4.9 4.6"/><circle cx="8.4" cy="9.6" r="1.4"/></symbol>
<symbol id="ic-chip" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.4" stroke-linecap="round" stroke-linejoin="round"><path d="M8.6 6.4h6.8l2.2 2.2v6.8l-2.2 2.2H8.6l-2.2-2.2V8.6z"/><path d="M10.2 3.6v2.8M13.8 3.6v2.8M10.2 17.6v2.8M13.8 17.6v2.8M3.6 10.2h2.8M3.6 13.8h2.8M17.6 10.2h2.8M17.6 13.8h2.8"/><path d="M10.4 10.4h3.2v3.2h-3.2z"/></symbol>
</defs></svg>
<div class="top-glow" aria-hidden="true"></div>
<div class="shell">
<header class="nav">
  <div class="nav-left">
    <a class="brand" href="#home"><span class="mark" aria-hidden="true"><svg viewBox="0 0 24 24"><path d="M13.2 2.6 5.8 13.4h4.9l-1.4 8 7.9-11.2h-5.1z" fill="#101319"/></svg></span><span class="brand-name">worthlesstask</span></a>
    <div class="lang" id="langSwitch" role="group" data-i18n-aria="nav.lang" aria-label="Interface language">
      <button class="lang-btn" type="button" data-lang="en" aria-pressed="true">EN</button>
      <button class="lang-btn" type="button" data-lang="ru" aria-pressed="false">RU</button>
    </div>
  </div>
  <nav class="tabs" id="navTabs" role="tablist" data-i18n-aria="nav.tabs" aria-label="Sections">
    <span class="tab-indicator" id="tabIndicator" aria-hidden="true"></span>
    <button class="tab" id="tabHome" role="tab" aria-selected="true" aria-controls="view-home" data-view="home" tabindex="0"><svg class="i" viewBox="0 0 24 24" aria-hidden="true"><use href="#ic-bolt"></use></svg><span data-i18n="tab.home">Summary</span></button>
    <button class="tab" id="tabPlay" role="tab" aria-selected="false" aria-controls="view-play" data-view="play" tabindex="-1"><svg class="i" viewBox="0 0 24 24" aria-hidden="true"><use href="#ic-library"></use></svg><span data-i18n="tab.play">Games</span></button>
  </nav>
  <div class="nav-right">
    <div class="chip">
      <span id="connectionDot" class="dot off"></span>
      <span id="connectionText" data-i18n="status.connecting">Connecting to the panel</span>
    </div>
  </div>
</header>
<main>
<section id="view-home" class="view" role="tabpanel" aria-labelledby="tabHome" tabindex="-1">
  <div class="view-inner">
    <div class="sum-grid">
      <div class="sum-col">
        <section class="panel">
          <div class="head"><h2><svg class="i" viewBox="0 0 24 24" aria-hidden="true"><use href="#ic-session"></use></svg><span data-i18n="session.title">Current session</span></h2><span id="sumBadge" class="badge run">—</span></div>
          <div class="body">
            <div id="sumError" class="alert" role="alert" hidden></div>
            <div id="sumName" class="sum-name">—</div>
            <div id="sumState" class="sum-state" role="status">—</div>
            <div class="stats">
              <div class="stat"><small data-i18n="session.uptime">Process time</small><strong id="sumElapsed">00:00</strong></div>
              <div class="stat"><small data-i18n="session.pid">PID</small><strong id="sumPid">—</strong></div>
            </div>
            <div id="sumNote" class="session-note" hidden></div>
            <div class="session-actions" style="margin-top:14px">
              <button id="sumStop" class="btn danger" type="button" disabled><svg class="i sm" viewBox="0 0 24 24" aria-hidden="true"><use href="#ic-stop"></use></svg><span class="bl" data-i18n="session.stop">Stop</span></button>
              <button id="sumReset" class="btn ghost" type="button" disabled><svg class="i sm" viewBox="0 0 24 24" aria-hidden="true"><use href="#ic-trash"></use></svg><span class="bl" data-i18n="session.reset">Delete session</span></button>
            </div>
          </div>
        </section>
        <section class="panel">
          <div class="head"><h2><svg class="i" viewBox="0 0 24 24" aria-hidden="true"><use href="#ic-queue"></use></svg><span data-i18n="queue.title">Game queue</span></h2><span class="counter" id="sumQueueCount">0</span></div>
          <div class="body">
            <ol id="sumQueueList" class="queue"></ol>
            <div id="sumQueueEmpty" class="hint" data-i18n="queue.empty">Nothing queued yet</div>
            <div class="queue-actions">
              <button id="sumQueueStart" class="btn primary" type="button" disabled><svg class="i sm" viewBox="0 0 24 24" aria-hidden="true"><use href="#ic-play"></use></svg><span class="bl" data-i18n="queue.start">Start</span></button>
            </div>
            <div id="sumQueueState" class="queue-status">—</div>
          </div>
        </section>
      </div>
      <div class="sum-col">
        <section class="panel">
          <div class="head"><h2><svg class="i" viewBox="0 0 24 24" aria-hidden="true"><use href="#ic-bolt"></use></svg><span data-i18n="quests.title">Discord Quests</span></h2><div class="head-right"><button id="sumAuto" class="btn small" type="button" data-i18n-aria="quests.autoHint" aria-label="Add quest games and queue them"><svg class="i xs" viewBox="0 0 24 24" aria-hidden="true"><use href="#ic-bolt"></use></svg><span class="bl" data-i18n="quests.auto">Auto</span></button><span class="counter" id="sumQuestCount">0</span></div></div>
          <div class="body">
            <div id="sumQuestList" class="quest-list"></div>
            <div id="sumQuestEmpty" class="empty" data-i18n="quests.empty">No active desktop quests found in local Discord cache</div>
          </div>
        </section>
        <section class="panel">
          <div class="head"><h2><svg class="i" viewBox="0 0 24 24" aria-hidden="true"><use href="#ic-library"></use></svg><span data-i18n="library.title">My games</span></h2><span class="counter" id="sumGameCount">0</span></div>
          <div class="body">
            <div id="sumGameList" class="quest-list"></div>
            <button class="btn wide" type="button" data-goto="play" style="margin-top:12px"><svg class="i sm" viewBox="0 0 24 24" aria-hidden="true"><use href="#ic-play"></use></svg><span class="bl" data-i18n="sum.open">Open the workspace</span></button>
          </div>
        </section>
      </div>
    </div>
    <p class="sum-about"><b data-i18n="sum.about.title">What this does</b> · <span data-i18n="sum.about">worthlesstask runs a lightweight process that Discord recognises, attaches Rich Presence to it, and lets desktop Quest progress tick up. Add games in the workspace, press Start, or line up a queue — everything runs and stays on this machine.</span></p>
  </div>
</section>

<section id="view-play" class="view" role="tabpanel" aria-labelledby="tabPlay" tabindex="-1" hidden>
  <div class="view-inner">
    <div class="sum-grid">
      <div class="sum-col">
        <section class="panel">
          <div class="head">
            <h2><svg class="i" viewBox="0 0 24 24" aria-hidden="true"><use href="#ic-library"></use></svg><span data-i18n="library.title">My games</span></h2>
            <div class="head-right">
              <button id="syncQuests" class="btn small" type="button"><svg class="i xs" viewBox="0 0 24 24" aria-hidden="true"><use href="#ic-sync"></use></svg><span class="bl" data-i18n="quests.sync">Sync Discord Quests</span></button>
              <span class="counter" id="gameCount">0</span>
            </div>
          </div>
          <div class="body">
            <div id="games" class="library"></div>
            <div id="libraryEmpty" class="empty" data-i18n="library.empty">Add a game from the search results or sync active Discord quests</div>
          </div>
        </section>
        <section class="panel">
          <div class="head"><h2><svg class="i" viewBox="0 0 24 24" aria-hidden="true"><use href="#ic-search"></use></svg><span data-i18n="search.title">Find a game</span></h2><small data-i18n="search.note">Discord catalogue</small></div>
          <div class="body">
            <form id="searchForm" class="search-row">
              <input id="query" type="search" data-i18n-aria="search.aria" aria-label="Game name" data-i18n-ph="search.placeholder" placeholder="For example: EA SPORTS FC 27" maxlength="256" autocomplete="off" required>
              <button id="search" class="btn primary" type="submit"><svg class="i sm" viewBox="0 0 24 24" aria-hidden="true"><use href="#ic-search"></use></svg><span class="bl" data-i18n="search.submit">Search</span></button>
            </form>
            <div id="searchStatus" class="status-line" role="status" aria-live="polite" data-i18n="search.initial">Type a name to search</div>
            <div class="result-area">
              <div id="results" class="results"></div>
              <div id="searchEmpty" class="empty" data-i18n="search.idle">Catalogue games will appear here</div>
            </div>
            <div class="footer-row">
              <span id="selectionLabel" class="sel-label" data-i18n="selection.none">No game selected</span>
              <button id="addSelected" class="btn" type="button" disabled><svg class="i sm" viewBox="0 0 24 24" aria-hidden="true"><use href="#ic-plus"></use></svg><span class="bl" data-i18n="add">Add</span></button>
              <button id="addAndRun" class="btn primary" type="button" disabled><svg class="i sm" viewBox="0 0 24 24" aria-hidden="true"><use href="#ic-play"></use></svg><span class="bl" data-i18n="addRun">Add &amp; start</span></button>
            </div>
          </div>
        </section>
      </div>
      <div class="sum-col">
        <section class="panel">
          <div class="head"><h2><svg class="i" viewBox="0 0 24 24" aria-hidden="true"><use href="#ic-session"></use></svg><span data-i18n="session.title">Current session</span></h2><span id="sessionBadge" class="badge run">—</span></div>
          <div class="body">
            <div id="globalError" class="alert" role="alert" hidden></div>
            <div class="session-top">
              <div>
                <div id="activeName" class="session-name">—</div>
                <div id="activeState" class="session-state" role="status">—</div>
              </div>
              <div class="session-actions">
                <button id="stopAll" class="btn danger" type="button" disabled><svg class="i sm" viewBox="0 0 24 24" aria-hidden="true"><use href="#ic-stop"></use></svg><span class="bl" data-i18n="session.stop">Stop</span></button>
                <button id="resetSession" class="btn ghost" type="button" disabled><svg class="i sm" viewBox="0 0 24 24" aria-hidden="true"><use href="#ic-trash"></use></svg><span class="bl" data-i18n="session.reset">Delete session</span></button>
              </div>
            </div>
            <div class="stats">
              <div class="stat"><small data-i18n="session.uptime">Process time</small><strong id="elapsed">00:00</strong></div>
              <div class="stat"><small data-i18n="session.pid">PID</small><strong id="pid">—</strong></div>
            </div>
            <div id="sessionNote" class="session-note" hidden></div>
          </div>
        </section>
        <section class="panel">
          <div class="head"><h2><svg class="i" viewBox="0 0 24 24" aria-hidden="true"><use href="#ic-bolt"></use></svg><span data-i18n="quests.title">Discord Quests</span></h2><div class="head-right"><button id="autoQuests" class="btn small" type="button" data-i18n-aria="quests.autoHint" aria-label="Add quest games and queue them"><svg class="i xs" viewBox="0 0 24 24" aria-hidden="true"><use href="#ic-bolt"></use></svg><span class="bl" data-i18n="quests.auto">Auto</span></button><span class="counter" id="questCount">0</span></div></div>
          <div class="body">
            <div id="questList" class="quest-list"></div>
            <div id="questEmpty" class="empty" data-i18n="quests.empty">No active desktop quests found in local Discord cache</div>
          </div>
        </section>
        <section class="panel">
          <div class="head"><h2><svg class="i" viewBox="0 0 24 24" aria-hidden="true"><use href="#ic-queue"></use></svg><span data-i18n="queue.title">Game queue</span></h2><span class="counter" id="queueCount">0</span></div>
          <div class="body">
            <label class="queue-settings"><span data-i18n="queue.per">Minutes per game</span><input id="queueMinutes" type="number" value="15" min="1" max="1440" step="1" data-i18n-aria="queue.aria" aria-label="Minutes per game"><span data-i18n="queue.unit">min</span></label>
            <ol id="queue" class="queue"></ol>
            <div id="queueEmpty" class="hint" data-i18n="queue.empty">Nothing queued yet</div>
            <div class="queue-actions">
              <button id="startQueue" class="btn primary" type="button" disabled><svg class="i sm" viewBox="0 0 24 24" aria-hidden="true"><use href="#ic-play"></use></svg><span class="bl" data-i18n="queue.start">Start</span></button>
              <button id="clearQueue" class="btn ghost" type="button" disabled><svg class="i sm" viewBox="0 0 24 24" aria-hidden="true"><use href="#ic-close"></use></svg><span class="bl" data-i18n="queue.clear">Clear</span></button>
            </div>
            <div id="queueStatus" class="queue-status" data-i18n="queue.stopped">Queue stopped</div>
          </div>
        </section>
      </div>
    </div>
  </div>
</section>
</main>
</div>
<div id="toast" class="toast" role="status" hidden></div>
<div id="modalRoot" class="modal-scrim" hidden>
  <div class="modal" role="dialog" aria-modal="true" aria-labelledby="modalTitle" aria-describedby="modalMsg">
    <h2 class="modal-title" id="modalTitle"></h2>
    <p class="modal-msg" id="modalMsg"></p>
    <input class="modal-input" id="modalInput" type="text" hidden>
    <div class="modal-actions">
      <button class="btn" type="button" id="modalCancel"></button>
      <button class="btn primary" type="button" id="modalOk"></button>
    </div>
  </div>
</div>
<script>
'use strict';
const $ = id => document.getElementById(id);
const SVGNS='http://www.w3.org/2000/svg';
const I18N={
en:{
"nav.lang":"Interface language","nav.tabs":"Sections","tab.home":"Summary","tab.play":"Games",
"sum.about.title":"What this does",
"sum.about":"worthlesstask runs a lightweight process that Discord recognises, attaches Rich Presence to it, and lets desktop Quest progress tick up. Add games in the workspace, press Start, or line up a queue — everything runs and stays on this machine.",
"sum.open":"Open the workspace",
"pet.name":"Lightning","pet.lvl":"Lv","pet.hint":"Your pet",
"pet.mood.idle":"Idling. Start a game and I will charge up.","pet.mood.work":"Charging on {game}. One spark per second.","pet.mood.sleep":"Asleep. No connection to the panel.",
"search.title":"Find a game","search.note":"Discord catalogue","search.placeholder":"For example: EA SPORTS FC 27","search.aria":"Game name",
"search.submit":"Search","search.busy":"Searching…",
"library.title":"My games","library.empty":"Add a game from the search results or sync active Discord quests","library.unit":"games","library.icon":"Icon",
"library.queueAdd":"Add to queue","library.queueRemove":"Remove from queue","library.delete":"Delete",
"library.exeName":"EXE name","library.makeExe":"Create EXE","library.save":"Save",
"library.exePlaceholder":"for example fc26.exe","library.exeAria":"Game file name",
"library.start":"Start","library.starting":"Starting…","library.running":"Running",
"badge.session":"Session","badge.noExe":"No EXE","badge.outside":"Custom EXE","badge.ready":"EXE ready","badge.missing":"EXE not built","meta.noExe":"EXE not set",
"bypass.native_exe":"Catalogue EXE","bypass.subdir_exe":"Subfolder EXE","bypass.catalogue_exe":"Catalogue EXE",
"bypass.carrier_ipc_sku":"Carrier + IPC + SKU","bypass.carrier_ipc":"Carrier + IPC","bypass.quest_sibling_ipc":"Quest Sibling + IPC","bypass.manual":"Manual EXE",
"quests.title":"Discord Quests","quests.sync":"Sync Quests & Bypass","quests.syncing":"Syncing…",
"quests.auto":"Auto","quests.autoHint":"Add the games the active quests need and queue them",
"notify.autoDone":"Quest games ready: {g} added, {q} queued","notify.autoNone":"Nothing to add — queue already covers the active quests",
"quests.empty":"No active desktop quests found in local Discord cache","quests.enrolled":"Enrolled","quests.completed":"Completed","quests.available":"Available in Discord","quests.active":"Active now",
"quests.orbs":"Orbs","quests.synced":"Discord quests and bypasses synced ({n} updated)",
"session.title":"Current session","session.uptime":"Process time","session.pid":"PID","session.stop":"Stop","session.reset":"Delete session",
"queue.title":"Game queue","queue.per":"Minutes per game","queue.unit":"min","queue.aria":"Minutes per game","queue.empty":"Nothing queued yet",
"queue.start":"Start","queue.restart":"Restart","queue.clear":"Clear","queue.of":"of","queue.running":"Queue running","queue.stopped":"Queue stopped",
"selection.none":"No game selected","add":"Add","add.busy":"Adding…","add.exists":"Already in library","addRun":"Add & start",
"status.connected":"Panel connected","status.offline":"No connection to the panel","dlg.ok":"OK","dlg.cancel":"Cancel","dlg.delete":"Delete","dlg.end":"End","dlg.delTitle":"Delete game?","dlg.delMsg":"The game will be removed from the library. Installed game files are not affected.","dlg.deleted":"Game removed from the library","dlg.resetTitle":"End session?","dlg.resetMsg":"End the session and clear its record?",
"search.loading":"Loading results…","search.none":"No matches","search.found":"Found: {n}. Select an entry.",
"active.idle":"Nothing running","rpc.connected":"RPC confirmed by Discord","rpc.connecting":"Connecting to Discord…",
"rpc.reconnecting":"Waiting / reconnecting","rpc.error":"RPC error","active.prepare":"Preparing and starting the process…","active.stopping":"Stopping the process…",
"active.ready":"Ready to start","active.unconfirmed":"RPC not confirmed yet",
"queue.unitShort":"min",
"err.exe.missing":"EXE not found",
"err.busy.operation":"Wait for the current start or stop to finish",
"err.busy.other":"Another operation is still running. Wait for it to finish.",
"err.session.active":"Stop the active session first",
"err.exe.unavailable":"The catalogue has no executable for this game. Automatic start is unavailable.",
"err.queue.too_long":"The queue must hold at most 100 games",
"err.queue.minutes":"Enter a whole number of minutes between 1 and 1440",
"err.game.missing":"Game not found",
"err.icon.too_large":"The icon must be 2 MiB or smaller",
"err.icon.format":"Unsupported icon format: ICO, PNG, JPG, BMP or WebP",
"err.slug.invalid":"Invalid game identifier",
"err.search.too_long":"The search query must be 256 characters or fewer",
"err.game.name_length":"Enter a game name of up to 256 characters",
"err.game.bad_id":"Invalid Application ID",
"err.game.stale":"That entry is out of date. Search again.",
"err.game.invalid":"Check the game's settings",
"err.exe.bad_name":"Expected an .exe name with no path or shell characters",
"err.exe.build_failed":"Could not build the EXE",
"err.queue.not_list":"The queue must be a list of games",
"err.library.save_failed":"Could not save the library",
"err.library.load_failed":"Could not read the library",
"err.request.origin":"Only requests from the local panel are allowed",
"err.request.size":"Invalid request size (4 MiB maximum)",
"err.request.streaming":"Streamed request bodies are not supported",
"err.request.truncated":"Request body arrived incomplete",
"err.request.json":"Malformed request JSON",
"err.request.object":"The request body must be a JSON object",
"err.server.internal":"Internal error. See the application log for details.",
"err.exe.bad_type":"The file name must be a string","err.icon.missing":"No icon uploaded","err.http.not_found":"Not found",
"err.request.local_only":"The panel accepts requests from 127.0.0.1 only","err.server.no_port":"No free local port",
"err.process.stop_failed":"Could not open the process to stop it",
"err.rpc.unconfirmed":"The process is running, but Discord has not confirmed the RPC yet. Check the desktop Discord.",
"err.game.bad_id_length":"The Application ID must be 17–20 digits",
"err.app.missing":"The application folder or the library file was not found",
"err.exe.not_windows":"The prepared file is not a Windows EXE",
"err.library.bad_shape":"Expected a list of games","err.library.bad_id":"Invalid identifier in the library",
"err.icon.not_in_folder":"The icon must live in the icons folder","err.icon.empty":"Choose a non-empty icon of up to 2 MiB",
"err.exe.symlink_instead":"A symbolic link cannot be used instead of the EXE",
"err.process.exited":"The process exited unexpectedly. See the application log for details.",
"err.queue.stopped":"The queue stopped. See the application log for details.",
"err.exe.symlink_blocked":"The EXE cannot be written through a symbolic link",
"err.exe.foreign_file":"That file already exists and does not belong to worthlesstask",
"net.aborted":"The request was cancelled or timed out",
"net.offline":"No connection to the local program. Check that worthlesstask is running.",
"http.generic":"Request failed: ",
"status.connecting":"Connecting to the panel","session.pending":"Pending","session.processing":"Processing","session.process":"Process","session.external":"Started manually","session.connectedShort":"Connected",
"session.multi":"Several game windows are running ({n}). Discord shows the last one. Press Stop to close them all.",
"session.externalNote":"The game was started manually — by the file next to the program. You can stop it here.",
"session.lastAck":"Last acknowledgement: ",
"session.ackWait":"The process exists. Waiting for an RPC answer; this is not an activity confirmation yet.",
"session.noteIdle":"The process launch and the RPC acknowledgement are shown separately.",
"queue.dragHint":"Drag to reorder","queue.up":"Up","queue.down":"Down","queue.remove":"Remove from queue",
"search.emptyNone":"No matches. Try the full or original name.",
"search.noFile":"No direct EXE in catalogue — Carrier + IPC bypass will be configured automatically",
"search.error":"Search failed","search.changedHint":"Press Search for a new query","search.changed":"Query changed",
"search.initial":"Type a name to search","search.idle":"Catalogue games will appear here",
"notify.added":"Game added, bypass EXE prepared","notify.addedRun":"Game added, start requested","notify.exeSaved":"EXE name saved",
"notify.startRequested":"Start request accepted",
"notify.prepareDone":"EXE created. The file sits in the workers folder — double-click it or press Start to open the game window.",
"notify.iconTooLarge":"The icon must be 2 MiB or smaller","notify.iconSaved":"Icon saved. It applies to the window at the next start.",
"notify.stopRequested":"Stop request accepted","notify.sessionDeleted":"Session deleted","notify.queueCleared":"Queue cleared","notify.queueStarted":"Queue started",
"card.fileTip":"File: {p}\nDouble-click it or press Start to open the game window.","card.processTip":"Process name: ","card.exeFailed":"Could not build the EXE: ",
"reason.no_exe":"No EXE set. Enter the file name or press Sync Quests & Bypass.",
"reason.manual":"The EXE name was entered manually. Ensure it matches a catalogue process or use Sync Quests & Bypass.",
"reason.derived":"Discord lists no direct file for this game. Press Sync Quests & Bypass to attach an automatic carrier executable."
},
ru:{
"nav.lang":"Язык интерфейса","nav.tabs":"Разделы","tab.home":"Сводка","tab.play":"Игры",
"sum.about.title":"Что это делает",
"sum.about":"worthlesstask запускает лёгкий процесс, который распознаёт Discord, привязывает к нему Rich Presence и позволяет набирать прогресс квестов для ПК. Добавьте игры в рабочей области, нажмите «Запустить» или соберите очередь — всё работает локально на вашем компьютере.",
"sum.open":"Открыть рабочую область",
"pet.name":"Молния","pet.lvl":"Ур.","pet.hint":"Ваш питомец",
"pet.mood.idle":"Отдыхаю. Запустите игру — и я начну заряжаться.","pet.mood.work":"Заряжаюсь на игре {game}. Одна искра в секунду.","pet.mood.sleep":"Сплю. Нет связи с панелью.",
"search.title":"Найти игру","search.note":"каталог Discord","search.placeholder":"Например: EA SPORTS FC 27","search.aria":"Название игры",
"search.submit":"Найти","search.busy":"Поиск…",
"library.title":"Мои игры","library.empty":"Добавьте игру через поиск или синхронизируйте активные квесты Discord","library.unit":"игр","library.icon":"Иконка",
"library.queueAdd":"В очередь","library.queueRemove":"Убрать из очереди","library.delete":"Удалить",
"library.exeName":"Имя EXE","library.makeExe":"Создать EXE","library.save":"Сохранить",
"library.exePlaceholder":"например fc26.exe","library.exeAria":"Имя файла игры",
"library.start":"Запустить","library.starting":"Запуск…","library.running":"Запущено",
"badge.session":"Сессия","badge.noExe":"Нет EXE","badge.outside":"Свой EXE","badge.ready":"EXE готов","badge.missing":"EXE не создан","meta.noExe":"EXE не указан",
"bypass.native_exe":"EXE каталога","bypass.subdir_exe":"Папка + EXE","bypass.catalogue_exe":"EXE каталога",
"bypass.carrier_ipc_sku":"Carrier + IPC + SKU","bypass.carrier_ipc":"Carrier + IPC","bypass.quest_sibling_ipc":"Quest Sibling + IPC","bypass.manual":"Ручной EXE",
"quests.title":"Квесты Discord","quests.sync":"Синхронизировать квесты","quests.syncing":"Синхронизация…",
"quests.auto":"Авто","quests.autoHint":"Добавить игры активных квестов и поставить их в очередь",
"notify.autoDone":"Игры квеста готовы: добавлено {g}, в очереди {q}","notify.autoNone":"Добавлять нечего — очередь уже покрывает активные квесты",
"quests.empty":"В локальном кэше Discord пока нет активных заданий для ПК","quests.enrolled":"Принято","quests.completed":"Завершено","quests.available":"Доступно в Discord","quests.active":"Активно",
"quests.orbs":"Орбов","quests.synced":"Квесты и обходы синхронизированы (обновлено: {n})",
"session.title":"Текущая сессия","session.uptime":"Время процесса","session.pid":"PID","session.stop":"Остановить","session.reset":"Удалить сессию",
"queue.title":"Очередь игр","queue.per":"На каждую игру","queue.unit":"мин","queue.aria":"Минут на игру","queue.empty":"Очередь пуста",
"queue.start":"Запустить","queue.restart":"Перезапустить","queue.clear":"Очистить","queue.of":"из","queue.running":"Очередь работает","queue.stopped":"Очередь остановлена",
"selection.none":"Игра не выбрана","add":"Добавить","add.busy":"Добавление…","add.exists":"Уже в библиотеке","addRun":"Добавить и запустить",
"status.connected":"Панель подключена","status.offline":"Нет связи с панелью","dlg.ok":"ОК","dlg.cancel":"Отмена","dlg.delete":"Удалить","dlg.end":"Завершить","dlg.delTitle":"Удалить игру?","dlg.delMsg":"Игра будет удалена из библиотеки. Файлы установленной игры не затрагиваются.","dlg.deleted":"Игра удалена из библиотеки","dlg.resetTitle":"Завершить сессию?","dlg.resetMsg":"Завершить сессию и очистить запись о ней?",
"search.loading":"Загружаем результаты…","search.none":"Совпадений нет","search.found":"Найдено: {n}. Выберите запись.",
"active.idle":"Ничего не запущено","rpc.connected":"RPC подтверждён Discord","rpc.connecting":"Подключение к Discord…",
"rpc.reconnecting":"Ожидание / переподключение","rpc.error":"Ошибка RPC","active.prepare":"Подготовка и запуск процесса…","active.stopping":"Остановка процесса…",
"active.ready":"Готово к запуску","active.unconfirmed":"RPC ещё не подтверждён",
"queue.unitShort":"мин",
"err.exe.missing":"EXE не найден",
"err.busy.operation":"Дождитесь завершения запуска или остановки",
"err.busy.other":"Другая операция ещё выполняется. Дождитесь её завершения.",
"err.session.active":"Сначала остановите активную сессию",
"err.exe.unavailable":"В каталоге нет исполняемого файла для этой игры. Автоматический запуск недоступен.",
"err.queue.too_long":"Очередь должна содержать не более 100 игр",
"err.queue.minutes":"Укажите целое число минут от 1 до 1440",
"err.game.missing":"Игра не найдена",
"err.icon.too_large":"Иконка должна быть не больше 2 МиБ",
"err.icon.format":"Формат файла не поддерживается: используйте ICO, PNG, JPG, BMP или WebP",
"err.slug.invalid":"Некорректный идентификатор игры",
"err.search.too_long":"Поисковый запрос должен быть не длиннее 256 символов",
"err.game.name_length":"Укажите название игры до 256 символов",
"err.game.bad_id":"Некорректный Application ID",
"err.game.stale":"Выбранная карточка устарела. Повторите поиск.",
"err.game.invalid":"Проверьте параметры игры",
"err.exe.bad_name":"Ожидается имя .exe без пути и служебных символов",
"err.exe.build_failed":"Не удалось создать EXE",
"err.queue.not_list":"Очередь должна быть списком игр",
"err.library.save_failed":"Не удалось сохранить библиотеку",
"err.library.load_failed":"Не удалось прочитать библиотеку",
"err.request.origin":"Разрешены только запросы из локальной панели",
"err.request.size":"Некорректный размер запроса (максимум 4 МиБ)",
"err.request.streaming":"Потоковая передача запроса не поддерживается",
"err.request.truncated":"Запрос получен не полностью",
"err.request.json":"Некорректный JSON запроса",
"err.request.object":"Тело запроса должно быть JSON-объектом",
"err.server.internal":"Внутренняя ошибка. Подробности в журнале приложения.",
"err.exe.bad_type":"Имя файла должно быть строкой","err.icon.missing":"Иконка не загружена","err.http.not_found":"Не найдено",
"err.request.local_only":"Панель принимает запросы только с 127.0.0.1","err.server.no_port":"Нет свободного локального порта",
"err.process.stop_failed":"Не удалось открыть процесс для остановки",
"err.rpc.unconfirmed":"Процесс запущен, но RPC ещё не подтверждён. Проверьте настольный клиент Discord.",
"err.game.bad_id_length":"Application ID должен содержать 17–20 цифр",
"err.app.missing":"Не найдена папка приложения или файл библиотеки",
"err.exe.not_windows":"Подготовленный файл не является Windows EXE",
"err.library.bad_shape":"Ожидался список игр","err.library.bad_id":"Недопустимый идентификатор в библиотеке",
"err.icon.not_in_folder":"Иконка должна находиться в папке icons","err.icon.empty":"Выберите непустую иконку размером до 2 МиБ",
"err.exe.symlink_instead":"Нельзя использовать символическую ссылку вместо EXE",
"err.process.exited":"Процесс завершился неожиданно — подробности в журнале приложения.",
"err.queue.stopped":"Очередь остановлена — подробности в журнале приложения.",
"err.exe.symlink_blocked":"Нельзя записать EXE через символическую ссылку",
"err.exe.foreign_file":"Файл уже существует и не принадлежит worthlesstask",
"net.aborted":"Запрос прерван или превышено время ожидания",
"net.offline":"Нет связи с локальной программой. Проверьте, что worthlesstask запущен.",
"http.generic":"Ошибка запроса: ",
"status.connecting":"Подключение к панели","session.pending":"Ожидание","session.processing":"Обработка","session.process":"Процесс","session.external":"Запущено вручную","session.connectedShort":"Подключено",
"session.multi":"Запущено несколько окон игр ({n}). Discord показывает последнее. Нажмите «Остановить», чтобы закрыть все.",
"session.externalNote":"Игра запущена вручную — через файл рядом с программой. Остановить её можно здесь.",
"session.lastAck":"Последнее подтверждение: ",
"session.ackWait":"Процесс активен. Ожидается ответ RPC от Discord.",
"session.noteIdle":"Состояние процесса и подтверждение RPC отображаются отдельно.",
"queue.dragHint":"Перетащите, чтобы изменить порядок","queue.up":"Выше","queue.down":"Ниже","queue.remove":"Убрать из очереди",
"search.emptyNone":"Ничего не найдено. Попробуйте полное или оригинальное название.",
"search.noFile":"В каталоге нет прямого EXE — обход Carrier + IPC настроится автоматически",
"search.error":"Ошибка поиска","search.changedHint":"Нажмите «Найти» для нового запроса","search.changed":"Запрос изменён",
"search.initial":"Введите название для поиска","search.idle":"Игры из каталога появятся здесь",
"notify.added":"Игра добавлена, обход и EXE подготовлены","notify.addedRun":"Игра добавлена, запуск начат","notify.exeSaved":"Имя EXE сохранено",
"notify.startRequested":"Запрос на запуск принят",
"notify.prepareDone":"EXE создан в папке workers — нажмите «Запустить» или откройте его двойным щелчком.",
"notify.iconTooLarge":"Иконка должна быть не больше 2 МиБ","notify.iconSaved":"Иконка сохранена. Она применится к окну при следующем запуске.",
"notify.stopRequested":"Запрос на остановку принят","notify.sessionDeleted":"Сессия удалена","notify.queueCleared":"Очередь очищена","notify.queueStarted":"Очередь запущена",
"card.fileTip":"Файл: {p}\nНажмите «Запустить» или откройте его двойным щелчком.","card.processTip":"Имя процесса: ","card.exeFailed":"Не удалось создать EXE: ",
"reason.no_exe":"EXE не задан. Укажите имя файла или нажмите «Синхронизировать квесты».",
"reason.manual":"Имя EXE указано вручную. Проверьте, что оно совпадает с процессом из каталога Discord, или используйте синхронизацию обхода.",
"reason.derived":"Discord не публикует прямой файл для этой игры. Нажмите «Синхронизировать квесты», чтобы автоматически привязать Carrier-обход."
}};
window.I18N=I18N;window.worthlesstaskLang=()=>ui.lang;
const ui={state:null,selected:null,candidates:[],cards:new Map(),busy:new Set(),online:false,searchSeq:0,searchController:null,refreshing:null,queueKey:'',queueMiniKey:'',gameMiniKey:'',questKeys:{},exeEditing:null,view:'home',lang:'en',searchBusy:false,minutesSynced:false,nextSwitch:null};
function text(el,value){if(!el)return;const s=String(value??'');if(el.textContent!==s)el.textContent=s}
function setText(el,value){const label=el&&el.querySelector('.bl');text(label||el,value)}
function node(tag,cls,value){const e=document.createElement(tag);if(cls)e.className=cls;if(value!==undefined)e.textContent=value;return e}
function icon(sym,cls){const s=document.createElementNS(SVGNS,'svg');s.setAttribute('class',cls||'i');s.setAttribute('viewBox','0 0 24 24');s.setAttribute('aria-hidden','true');const u=document.createElementNS(SVGNS,'use');u.setAttribute('href','#ic-'+sym);s.append(u);return s}
function notify(message,error=false){text($('toast'),message);$('toast').hidden=false;$('toast').classList.toggle('error',error);clearTimeout(notify.timer);notify.timer=setTimeout(()=>$('toast').hidden=true,4800)}
async function api(path,options={}){const {timeout=12000,signal,...rest}=options;const controller=new AbortController();const abort=()=>controller.abort();if(signal)signal.addEventListener('abort',abort,{once:true});const timer=setTimeout(abort,timeout);try{const response=await fetch(path,{...rest,signal:controller.signal});const data=await response.json();if(!response.ok){const err=new Error(serverError(data));err.code=data&&data.code||'';err.status=response.status;throw err}return data}catch(e){if(e.name==='AbortError')throw new Error(t('net.aborted'));if(e instanceof TypeError)throw new Error(t('net.offline'));throw e}finally{clearTimeout(timer);if(signal)signal.removeEventListener('abort',abort)}}
const post=(path,payload)=>api(path,{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(payload||{})});
function t(key){const pack=I18N[ui.lang]||I18N.en;return pack[key]!==undefined?pack[key]:(I18N.en[key]!==undefined?I18N.en[key]:'')}
function serverError(data){const code=data&&data.code;if(code){const v=t('err.'+code);if(v)return v}return (data&&data.error)||t('http.generic')}
function moveIndicator(){const tabs=$('navTabs'),ind=$('tabIndicator');if(!tabs||!ind)return;const active=tabs.querySelector('.tab[aria-selected="true"]');if(!active)return;ind.style.width=active.offsetWidth+'px';ind.style.transform='translateX('+active.offsetLeft+'px)'}
function applyI18n(){
document.documentElement.lang=ui.lang==='ru'?'ru':'en';
for(const el of document.querySelectorAll('[data-i18n]')){const v=t(el.dataset.i18n);if(v)text(el,v)}
for(const el of document.querySelectorAll('[data-i18n-ph]')){const v=t(el.dataset.i18nPh);if(v)el.setAttribute('placeholder',v)}
for(const el of document.querySelectorAll('[data-i18n-aria]')){const v=t(el.dataset.i18nAria);if(v)el.setAttribute('aria-label',v)}
for(const b of document.querySelectorAll('[data-lang]'))b.setAttribute('aria-pressed',String(b.dataset.lang===ui.lang));
setText($('search'),ui.searchBusy?t('search.busy'):t('search.submit'));
setText($('syncQuests'),ui.busy.has('sync')?t('quests.syncing'):t('quests.sync'));
text($('connectionText'),ui.online?t('status.connected'):(ui.state?t('status.offline'):t('status.connecting')));
moveIndicator();requestAnimationFrame(moveIndicator)}
function setLang(lang){if(lang!=='en'&&lang!=='ru')return;ui.lang=lang;try{localStorage.setItem('worthlesstask.lang',lang)}catch(_){}ui.questKeys={};ui.queueKey='';ui.queueMiniKey='';applyI18n();if(ui.state)render(ui.state)}
try{const saved=localStorage.getItem('worthlesstask.lang');if(saved==='en'||saved==='ru')ui.lang=saved}catch(_){}
document.querySelectorAll('[data-lang]').forEach(b=>b.addEventListener('click',()=>setLang(b.dataset.lang)));
window.addEventListener('resize',moveIndicator);
function playEnter(view){const inner=view.querySelector('.view-inner');if(!inner)return;inner.classList.remove('is-entering');void inner.offsetWidth;inner.classList.add('is-entering')}
const scrollMemory={home:0,play:0};
function showView(name,focusId){const next=name==='play'?'play':'home';if(next===ui.view){if(focusId){const el=$(focusId);if(el)el.focus()}return}
scrollMemory[ui.view]=window.scrollY;
ui.view=next;
const home=$('view-home'),play=$('view-play');
home.hidden=next!=='home';play.hidden=next!=='play';
$('tabHome').setAttribute('aria-selected',String(next==='home'));$('tabPlay').setAttribute('aria-selected',String(next==='play'));
$('tabHome').tabIndex=next==='home'?0:-1;$('tabPlay').tabIndex=next==='play'?0:-1;
window.scrollTo(0,scrollMemory[next]);
if(location.hash.slice(1)!==next)history.replaceState(null,'','#'+next);
moveIndicator();playEnter(next==='home'?home:play);
if(focusId){const el=$(focusId);if(el)el.focus()}}
document.querySelectorAll('[data-view]').forEach(b=>b.addEventListener('click',()=>showView(b.dataset.view)));
document.querySelectorAll('[data-goto]').forEach(b=>b.addEventListener('click',()=>showView(b.dataset.goto,b.dataset.focus)));
window.addEventListener('hashchange',()=>showView(location.hash.slice(1)));
$('navTabs').addEventListener('keydown',e=>{const tabs=[...$('navTabs').querySelectorAll('.tab')];const i=tabs.indexOf(document.activeElement);if(i<0)return;let n=null;
if(e.key==='ArrowRight'||e.key==='ArrowDown')n=(i+1)%tabs.length;else if(e.key==='ArrowLeft'||e.key==='ArrowUp')n=(i-1+tabs.length)%tabs.length;
else if(e.key==='Home')n=0;else if(e.key==='End')n=tabs.length-1;
else if(e.key===' '||e.key==='Enter'){e.preventDefault();tabs[i].click();return}
if(n===null)return;e.preventDefault();tabs[n].focus();tabs[n].click()});
function imageBox(){const box=node('div','icon-box');box.append(icon('image','i ph'));const img=node('img');img.alt='';img.loading='lazy';img.decoding='async';img.hidden=true;img.addEventListener('error',()=>{img.hidden=true});box.append(img);return{box,img,url:null}}
function setImage(ref,url,version){if(url){try{const u=new URL(url,location.origin);if(u.origin!==location.origin&&u.hostname!=='cdn.discordapp.com')url=null;else if(u.origin===location.origin&&version)u.searchParams.set('v',version);if(url)url=u.href}catch{url=null}}if(ref.url===url)return;ref.url=url;ref.img.hidden=!url;if(url)ref.img.src=url;else ref.img.removeAttribute('src')}
function button(label,kind,slug,cls='btn small ghost',sym){const b=node('button',cls);b.type='button';b.dataset.act=kind;if(slug)b.dataset.slug=slug;if(sym)b.append(icon(sym,'i xs'));b.append(node('span','bl',label));return b}
function iconButton(sym,kind,slug,cls,label){const b=node('button',cls);b.type='button';b.dataset.act=kind;if(slug)b.dataset.slug=slug;b.append(icon(sym,cls==='q-del'?'i xxs':'i xs'));if(label)b.setAttribute('aria-label',label);return b}
function findQuestForGame(g,quests){if(!Array.isArray(quests))return null;return quests.find(q=>q.primary_app_id===g.application_id||(Array.isArray(q.accepted_app_ids)&&q.accepted_app_ids.includes(g.application_id)))||null}
function makeCard(g){const root=node('article','game');root.dataset.slug=g.slug;const im=imageBox(),info=node('div','game-info'),titleRow=node('div','game-title-row'),name=node('div','game-name'),meta=node('div','game-meta'),tags=node('div','game-tags'),badge=node('span','badge'),bypassBadge=node('span','badge sub'),questBadge=node('span','badge quest');titleRow.append(name);tags.append(bypassBadge,questBadge);info.append(titleRow,meta,tags);const reason=node('p','reason');const actions=node('div','game-actions');const icon_=button(t('library.icon'),'icon',g.slug,'btn small ghost','image'),queue=button(t('library.queueAdd'),'queue',g.slug,'btn small ghost','queue'),del=button(t('library.delete'),'delete',g.slug,'btn small ghost','trash'),rename=button(t('library.exeName'),'rename',g.slug,'btn small ghost','edit'),prepare=button(t('library.makeExe'),'prepare',g.slug,'btn small ghost','chip'),start=button(t('library.start'),'start',g.slug,'btn small primary start','play');const file=node('input','icon-picker');file.type='file';file.accept='.ico,.png,.jpg,.jpeg,.bmp,.webp';file.dataset.icon=g.slug;const exeRow=node('div','exe-row');exeRow.hidden=true;const exeInput=node('input');exeInput.type='text';exeInput.maxLength=180;exeInput.placeholder=t('library.exePlaceholder');exeInput.setAttribute('aria-label',t('library.exeAria'));const exeSave=button(t('library.save'),'exe-save',g.slug,'btn small primary','check');exeRow.append(exeInput,exeSave);actions.append(icon_,queue,del,rename,prepare,start,file);root.append(im.box,info,badge,actions,reason,exeRow);return{root,im,name,meta,tags,badge,bypassBadge,questBadge,reason,icon:icon_,queue,del,rename,prepare,start,file,exeRow,exeInput,exeSave}}
function updateCard(ref,g,s){const active=s.active?.slug===g.slug;const pending=s.operation?.slug===g.slug;const locked=!!s.operation||ui.busy.size>0||!ui.online;const ready=!!g.worker_ready;const derived=g.can_start&&g.executable_source!=='catalogue'&&!g.bypass_mode;const exeDisplay=g.executable_rel||g.executable||t('meta.noExe');text(ref.name,g.game_name);text(ref.meta,'ID '+g.application_id+' · '+exeDisplay+(g.epic_app_id?' · Epic SKU':''));ref.meta.title=g.worker_path?t('card.fileTip').replace('{p}',g.worker_path):(exeDisplay?t('card.processTip')+exeDisplay:'');text(ref.badge,active?t('badge.session'):!g.can_start?t('badge.noExe'):derived?t('badge.outside'):ready?t('badge.ready'):t('badge.missing'));ref.badge.className='badge '+(active?'run':g.can_start&&ready&&!derived?'':'warn');
const bmode=g.bypass_mode||(g.executable_rel&&g.executable_rel.includes('/')?'subdir_exe':(g.executable_source==='catalogue'?'native_exe':''));const btext=bmode?t('bypass.'+bmode):'';text(ref.bypassBadge,btext);ref.bypassBadge.hidden=!btext;
const mq=findQuestForGame(g,s.quests);const qpct=mq?(mq.is_completed?'100%':mq.progress_percent+'%'):'';const qtext=mq?(mq.orb_reward?mq.orb_reward+' '+t('quests.orbs')+' · '+(mq.is_completed?t('quests.completed'):qpct):mq.quest_name):'';text(ref.questBadge,qtext);ref.questBadge.hidden=!qtext;ref.tags.hidden=ref.bypassBadge.hidden&&ref.questBadge.hidden;
ref.root.classList.toggle('active',active);const reasonKey=g.availability_reason&&t(g.availability_reason)?g.availability_reason:null;const wcode=g.worker_error_code&&t('err.'+g.worker_error_code);const note=reasonKey?t(reasonKey):(g.worker_error?(wcode||t('card.exeFailed')+g.worker_error):'');text(ref.reason,note||'');ref.reason.hidden=!note;setImage(ref.im,g.icon_url,g.icon_version);setText(ref.start,pending?t('library.starting'):active?t('library.running'):t('library.start'));ref.start.disabled=locked||active||!g.can_start;ref.start.classList.toggle('is-running',active||pending);ref.prepare.hidden=!g.can_start||ready;ref.prepare.disabled=locked;ref.rename.disabled=locked;ref.exeSave.disabled=locked;ref.exeRow.hidden=ui.exeEditing!==g.slug;ref.icon.disabled=ui.busy.size>0;ref.del.disabled=locked||active;setText(ref.queue,s.queue.includes(g.slug)?t('library.queueRemove'):t('library.queueAdd'));ref.queue.disabled=locked||!g.can_start;setText(ref.icon,t('library.icon'));setText(ref.del,t('library.delete'));setText(ref.rename,t('library.exeName'));setText(ref.prepare,t('library.makeExe'));setText(ref.exeSave,t('library.save'));if(document.activeElement!==ref.exeInput){ref.exeInput.placeholder=t('library.exePlaceholder');ref.exeInput.setAttribute('aria-label',t('library.exeAria'))}}

function renderQuestsInto(listId,emptyId,countId,s){let quests=Array.isArray(s.quests)?s.quests.slice():[];/* live quests first: enrolled and unfinished, then the rest as-is */
quests.sort((a,b)=>{const rank=q=>q.is_completed?2:(q.is_enrolled?0:1);return rank(a)-rank(b)});
text($(countId),String(quests.length));$(emptyId).hidden=quests.length>0;const qk=JSON.stringify([ui.lang,quests.map(q=>[q.quest_id,q.progress_percent,q.is_enrolled,q.is_completed,q.orb_reward])]);if(ui.questKeys[listId]===qk)return;ui.questKeys[listId]=qk;const list=$(listId);list.replaceChildren();for(const q of quests){const isDone=!!q.is_completed;const live=!!q.is_enrolled&&!isDone;const pct=isDone?100:(q.progress_percent||0);const card=node('div','quest-card'+(isDone?' completed':(live?' enrolled':'')));const main=node('div','quest-main');const title=node('div','quest-title',q.game_title||q.quest_name);const statusText=isDone?t('quests.completed'):(live?t('quests.active'):t('quests.available'));const sub=node('div','quest-sub',statusText+' · '+q.target_minutes+' '+t('queue.unitShort')+(q.orb_reward?' · '+q.orb_reward+' '+t('quests.orbs'):''));const bar=node('div','quest-bar');const fill=node('span');fill.style.width=pct+'%';bar.append(fill);main.append(title,sub,bar);const pill=node('span','badge '+(isDone?'':(live?'run':'warn')),pct+'%');card.append(main,pill);list.append(card)}}
function fmtUptime(sec){sec=Math.max(0,Math.floor(sec||0));return String(Math.floor(sec/60)).padStart(2,'0')+':'+String(sec%60).padStart(2,'0')}
function sessionNoteFor(s){const a=s.active,op=s.operation;if(op)return '';if(!a)return t('session.noteIdle');if(a.rpc_error)return a.rpc_error;if(a.also_running>0)return t('session.multi').replace('{n}',a.also_running+1);if(a.reason==='external')return t('session.externalNote');if(a.last_ack)return t('session.lastAck')+new Date(a.last_ack).toLocaleTimeString(ui.lang==='ru'?'ru-RU':'en-US');return t('session.ackWait')}
function renderQueueInto(s){const list=$('queue');list.replaceChildren();s.queue.forEach((slug,i)=>{const g=s.games.find(x=>x.slug===slug);const current=s.active?.slug===slug;const li=node('li','queue-item'+(current?' current':''));li.draggable=true;li.dataset.slug=slug;li.style.animationDelay=(i*.04)+'s';li.title=t('queue.dragHint');li.append(node('span','q-grip',''),node('span','q-num',String(i+1)),node('span','q-name',g?.game_name||slug),node('span','q-min',(g?.duration_minutes||15)+t('queue.unitShort')));
const order=node('div','q-order');const up=iconButton('up','queue-up',slug,'q-move',t('queue.up'));up.disabled=i===0;const down=iconButton('down','queue-down',slug,'q-move',t('queue.down'));down.disabled=i===s.queue.length-1;order.append(up,down);const rm=iconButton('close','queue',slug,'q-del',t('queue.remove'));li.append(order,rm);if(current)li.append(node('span','q-bar'));list.append(li)})}
function renderMiniQueue(s){const key=JSON.stringify([ui.lang,s.queue,s.games.map(g=>[g.slug,g.game_name,g.duration_minutes]),s.active?.slug]);if(ui.queueMiniKey===key)return;ui.queueMiniKey=key;const list=$('sumQueueList');list.replaceChildren();s.queue.forEach((slug,i)=>{const g=s.games.find(x=>x.slug===slug);const li=node('li','mini-row'+(s.active?.slug===slug?' current':''));li.style.animationDelay=(i*.04)+'s';li.append(node('span','q-num',String(i+1)),node('span','q-name',g?.game_name||slug),node('span','mini-meta',(g?.duration_minutes||15)+t('queue.unitShort')));list.append(li)});$('sumQueueEmpty').hidden=!!s.queue.length;text($('sumQueueCount'),s.queue.length+' '+t('queue.of')+' '+s.games.length)}
function renderSummary(s){const op=s.operation,a=s.active,locked=!!op||ui.busy.size>0||!ui.online;
text($('sumName'),a?.game_name||(op?.slug?s.games.find(g=>g.slug===op.slug)?.game_name:t('active.idle')));const rpc=a?.rpc_state;const labels={connected:t('rpc.connected'),connecting:t('rpc.connecting'),reconnecting:t('rpc.reconnecting'),error:t('rpc.error')};text($('sumState'),op?(op.kind==='start'?t('active.prepare'):t('active.stopping')):(a?labels[rpc]||t('active.unconfirmed'):t('active.ready')));text($('sumBadge'),op?t('session.processing'):rpc==='connected'?(a?.reason==='external'?t('session.external'):t('session.connectedShort')):a?t('session.process'):t('session.pending'));$('sumBadge').className='badge '+(op||rpc==='connected'?'run':a?'':'warn');text($('sumElapsed'),fmtUptime(a?.uptime_s));text($('sumPid'),a?.pid||'—');const sn=sessionNoteFor(s);const sumNote=$('sumNote');text(sumNote,sn||'');sumNote.hidden=!sn;
$('sumStop').disabled=locked||!a;$('sumReset').disabled=locked||(!a&&!s.last_error);
renderMiniQueue(s);$('sumQueueStart').disabled=locked||!s.queue.length||s.queue_running;text($('sumQueueState'),s.queue_running?t('queue.running')+(s.next_switch_in_s!=null?' · '+Math.ceil(s.next_switch_in_s)+' '+t('queue.unitShort'):''):t('queue.stopped'));
renderQuestsInto('sumQuestList','sumQuestEmpty','sumQuestCount',s);
text($('sumGameCount'),String(s.games.length));
const gl=$('sumGameList');const gkey=JSON.stringify([ui.lang,s.games.map(g=>[g.slug,g.game_name,!!g.worker_ready]),s.active?.slug]);if(ui.gameMiniKey!==gkey){ui.gameMiniKey=gkey;gl.replaceChildren();for(const g of s.games.slice(0,7)){const row=node('div','mini-row'+(s.active?.slug===g.slug?' current':''));row.append(node('span','q-name',g.game_name),node('span','mini-meta',g.worker_ready?'✓':'·'));gl.append(row)}}}

function render(s){ui.state=s;const op=s.operation,a=s.active,locked=!!op||ui.busy.size>0||!ui.online;
ui.nextSwitch=s.next_switch_in_s;
if(!ui.minutesSynced&&s.games?.length&&document.activeElement!==$('queueMinutes')){const qg=s.queue?.length?s.games.find(g=>g.slug===s.queue[0]):s.games[0];if(qg?.duration_minutes)$('queueMinutes').value=String(qg.duration_minutes);ui.minutesSynced=true}
const seen=new Set();for(const g of s.games){seen.add(g.slug);let ref=ui.cards.get(g.slug);if(!ref){ref=makeCard(g);ref.root.style.animationDelay=(ui.cards.size*.035)+'s';ui.cards.set(g.slug,ref);$('games').append(ref.root)}updateCard(ref,g,s)}for(const[slug,ref]of ui.cards){if(!seen.has(slug)){ref.root.remove();ui.cards.delete(slug)}}$('libraryEmpty').hidden=!!s.games.length;text($('gameCount'),s.games.length+' '+t('library.unit'));
$('syncQuests').disabled=locked;setText($('syncQuests'),ui.busy.has('sync')?t('quests.syncing'):t('quests.sync'));
const autoBusy=ui.busy.has('auto');$('autoQuests').disabled=locked||autoBusy;$('sumAuto').disabled=locked||autoBusy;setText($('autoQuests'),autoBusy?'…':t('quests.auto'));setText($('sumAuto'),autoBusy?'…':t('quests.auto'));
renderQuestsInto('questList','questEmpty','questCount',s);
text($('activeName'),a?.game_name||(op?.slug?s.games.find(g=>g.slug===op.slug)?.game_name:t('active.idle')));const rpc=a?.rpc_state;const labels={connected:t('rpc.connected'),connecting:t('rpc.connecting'),reconnecting:t('rpc.reconnecting'),error:t('rpc.error')};text($('activeState'),op?(op.kind==='start'?t('active.prepare'):t('active.stopping')):(a?labels[rpc]||t('active.unconfirmed'):t('active.ready')));text($('sessionBadge'),op?t('session.processing'):rpc==='connected'?(a?.reason==='external'?t('session.external'):t('session.connectedShort')):a?t('session.process'):t('session.pending'));$('sessionBadge').className='badge '+(op||rpc==='connected'?'run':a?'':'warn');text($('elapsed'),fmtUptime(a?.uptime_s));text($('pid'),a?.pid||'—');const note=sessionNoteFor(s);const sn=$('sessionNote');text(sn,note||'');sn.hidden=!note;$('stopAll').disabled=locked||!a;$('resetSession').disabled=locked||(!a&&!s.last_error);
const error=(s.last_error_code&&t('err.'+s.last_error_code))||s.last_error||'';const ge=$('globalError');if(ge){text(ge,error);ge.hidden=!error}const se=$('sumError');if(se){text(se,error);se.hidden=!error}
const key=JSON.stringify([s.queue,s.games.map(g=>[g.slug,g.game_name,g.duration_minutes])]);if(ui.queueKey!==key){ui.queueKey=key;renderQueueInto(s)}const rows=[...$('queue').querySelectorAll('.queue-item')];rows.forEach((li,i)=>{for(const b of li.querySelectorAll('button')){const act=b.dataset.act;b.disabled=locked||(act==='queue-up'&&i===0)||(act==='queue-down'&&i===rows.length-1)}});paintQueueBar();$('queueEmpty').hidden=!!s.queue.length;text($('queueCount'),s.queue.length+' '+t('queue.of')+' '+s.games.length);$('startQueue').disabled=locked||!s.queue.length||s.queue_running;setText($('startQueue'),s.queue_running?t('queue.restart'):t('queue.start'));$('clearQueue').disabled=locked||!s.queue.length;text($('queueStatus'),s.queue_running?t('queue.running')+(s.next_switch_in_s!=null?' · '+Math.ceil(s.next_switch_in_s)+' '+t('queue.unitShort'):''):t('queue.stopped'));
renderSummary(s);paintPet();selectionState()}
function paintQueueBar(){const bar=$('queue').querySelector('.queue-item.current .q-bar');if(bar){const mins=ui.state?.games.find(g=>g.slug===ui.state.active?.slug)?.duration_minutes||15;const left=ui.nextSwitch;bar.style.width=(left!=null&&mins>0)?Math.max(0,Math.min(100,(1-left/(mins*60))*100))+'%':'0'}}
let dragSlug=null;
function clearDropMarks(){for(const el of $('queue').children)el.classList.remove('dragging','drop-before','drop-after')}
$('queue').addEventListener('dragstart',e=>{const li=e.target.closest('.queue-item');if(!li||ui.busy.size)return;dragSlug=li.dataset.slug;li.classList.add('dragging');e.dataTransfer.effectAllowed='move';try{e.dataTransfer.setData('text/plain',dragSlug)}catch(_){}});
$('queue').addEventListener('dragover',e=>{if(!dragSlug)return;e.preventDefault();e.dataTransfer.dropEffect='move';const li=e.target.closest('.queue-item');for(const el of $('queue').children)el.classList.remove('drop-before','drop-after');if(!li||li.dataset.slug===dragSlug)return;const box=li.getBoundingClientRect();li.classList.add(e.clientY<box.top+box.height/2?'drop-before':'drop-after')});
$('queue').addEventListener('drop',e=>{if(!dragSlug)return;e.preventDefault();const li=e.target.closest('.queue-item');const slug=dragSlug;const target=li?li.dataset.slug:null;const before=li?li.classList.contains('drop-before'):false;dragSlug=null;clearDropMarks();if(!target||target===slug)return;
const q=[...(ui.state?.queue||[])];const from=q.indexOf(slug);if(from<0)return;q.splice(from,1);let to=q.indexOf(target);if(to<0)return;if(!before)to+=1;q.splice(to,0,slug);mutation('queue',()=>post('/api/queue',{slugs:q,minutes:minutes()}))});
$('queue').addEventListener('dragend',()=>{dragSlug=null;clearDropMarks()});
function selectionState(){const selected=ui.selected;const existing=ui.state?.games.find(g=>g.application_id===selected?.id);const exists=!!existing;const busy=ui.busy.has('add');text($('selectionLabel'),selected?selected.name+' · ID '+selected.id:t('selection.none'));$('addSelected').disabled=!selected||exists||busy||!ui.online;$('addAndRun').disabled=!selected||busy||!ui.online||(exists&&(!existing.can_start||ui.state?.active?.slug===existing.slug));setText($('addSelected'),busy?t('add.busy'):exists?t('add.exists'):t('add'));setText($('addAndRun'),busy?'…':exists?t('library.start'):t('addRun'))}
async function refresh(){if(ui.refreshing)return ui.refreshing;ui.refreshing=(async()=>{try{const s=await api('/api/state');ui.online=true;text($('connectionText'),t('status.connected'));$('connectionDot').classList.remove('off');render(s)}catch(e){ui.online=false;text($('connectionText'),t('status.offline'));$('connectionDot').classList.add('off');if(ui.state)render(ui.state)}finally{ui.refreshing=null}})();return ui.refreshing}
async function poll(){try{await refresh()}catch(e){/* a failed tick must never stop the loop */}setTimeout(poll,document.hidden?4000:800)}
/* Last will: when the last tab goes away, the backend retires itself shortly
   after. A reload also fires pagehide, so the server waits a few seconds —
   the fresh page cancels it with a heartbeat before the timer expires. */
window.addEventListener('pagehide',e=>{if(e.persisted)return;try{navigator.sendBeacon('/api/shutdown')}catch(_){try{fetch('/api/shutdown',{method:'POST',keepalive:true})}catch(__){}}});
window.addEventListener('pageshow',e=>{if(e.persisted)fetch('/api/heartbeat',{method:'POST',keepalive:true}).catch(()=>{})});
setInterval(()=>{fetch('/api/heartbeat',{method:'POST',keepalive:true}).catch(()=>{})},2500);
/* Local 1-second ticker: uptime, queue countdown and the pet's charge advance
   between polls, so nothing on screen waits for the next /api/state. */
setInterval(()=>{const s=ui.state;if(!s)return;const a=s.active;
if(a&&!s.operation){if(a._tick==null)a._tick=Math.floor(a.uptime_s||0);else a._tick++;a.uptime_s=a._tick;text($('elapsed'),fmtUptime(a.uptime_s));text($('sumElapsed'),fmtUptime(a.uptime_s));petCharge(1)}
if(s.queue_running&&ui.nextSwitch!=null){ui.nextSwitch=Math.max(0,ui.nextSwitch-1);paintQueueBar();const line=t('queue.running')+' · '+Math.ceil(ui.nextSwitch)+' '+t('queue.unitShort');text($('queueStatus'),line);text($('sumQueueState'),line)}},1000);
document.addEventListener('visibilitychange',()=>{if(!document.hidden)refresh()});
window.addEventListener('focus',()=>refresh());
async function mutation(key,action,success){if(ui.busy.size)return;ui.busy.add(key);if(ui.state)render(ui.state);try{const res=await action();const msg=typeof success==='function'?success(res):success;if(msg)notify(msg);await refresh()}catch(e){notify(e.message,true)}finally{ui.busy.delete(key);if(ui.state)render(ui.state)}}
function renderResults(results){$('results').replaceChildren();ui.selected=null;ui.candidates=results;$('searchEmpty').hidden=results.length>0;text($('searchEmpty'),t('search.emptyNone'));for(const [i,r] of results.entries()){const card=node('button','result');card.type='button';card.dataset.resultId=r.id;card.setAttribute('aria-pressed','false');card.style.animationDelay=(i*.03)+'s';const im=imageBox();setImage(im,r.icon_url,'');const content=node('div','result-body');content.append(node('div','name',r.name),node('div','meta','ID '+r.id),node('div','meta',r.executables?.length?r.executables.join(' · '):t('search.noFile')));const check=node('span','check');check.append(icon('check','i'));card.append(im.box,content,check);card.addEventListener('click',()=>{ui.selected=r;for(const b of $('results').children)b.setAttribute('aria-pressed',String(b===card));selectionState()});$('results').append(card)}selectionState()}
$('searchForm').addEventListener('submit',async e=>{e.preventDefault();const q=$('query').value.trim();if(!q)return;const seq=++ui.searchSeq;ui.searchController?.abort();ui.searchController=new AbortController();ui.selected=null;selectionState();$('search').disabled=true;ui.searchBusy=true;setText($('search'),t('search.busy'));text($('searchStatus'),t('search.loading'));$('results').setAttribute('aria-busy','true');$('results').replaceChildren(node('div','pulse'),node('div','pulse'));$('searchEmpty').hidden=true;try{const data=await api('/api/search?q='+encodeURIComponent(q),{signal:ui.searchController.signal,timeout:95000});if(seq!==ui.searchSeq)return;renderResults(data.results);text($('searchStatus'),data.results.length?t('search.found').replace('{n}',data.results.length):t('search.none'))}catch(e){if(seq!==ui.searchSeq)return;renderResults([]);text($('searchStatus'),t('search.error'));text($('searchEmpty'),e.message)}finally{if(seq===ui.searchSeq){$('results').setAttribute('aria-busy','false');$('search').disabled=false;ui.searchBusy=false;setText($('search'),t('search.submit'))}}});
$('query').addEventListener('input',()=>{if(ui.searchController){ui.searchSeq++;ui.searchController.abort();ui.searchController=null;$('search').disabled=false;ui.searchBusy=false;setText($('search'),t('search.submit'));$('results').replaceChildren();$('searchEmpty').hidden=false;text($('searchEmpty'),t('search.changedHint'));text($('searchStatus'),t('search.changed'));ui.selected=null;selectionState()}});
$('addSelected').addEventListener('click',()=>{const r=ui.selected;if(!r)return;mutation('add',()=>post('/api/games',{game_name:r.name,application_id:r.id}),t('notify.added'))});
$('addAndRun').addEventListener('click',()=>{const r=ui.selected;if(!r)return;const existing=ui.state?.games.find(g=>g.application_id===r.id);if(existing){mutation('start',()=>post('/api/play',{slug:existing.slug}),t('notify.startRequested'));return}mutation('add',()=>post('/api/games',{game_name:r.name,application_id:r.id,autostart:true}),t('notify.addedRun'))});
$('syncQuests').addEventListener('click',()=>mutation('sync',()=>post('/api/quests/sync',{auto_add:true}),res=>{const n=(res?.sync?.added_quests?.length||0)+(res?.sync?.updated_slugs?.length||0);return t('quests.synced').replace('{n}',n)}));
function autoQuestsRun(){mutation('auto',()=>post('/api/quests/auto',{minutes:minutes()}),res=>{const r=res?.auto||{};return (r.added?.length||r.queued?.length)?t('notify.autoDone').replace('{g}',r.added.length).replace('{q}',r.queued.length):t('notify.autoNone')})}
$('autoQuests').addEventListener('click',autoQuestsRun);
$('sumAuto').addEventListener('click',autoQuestsRun);
function minutes(){const n=Number($('queueMinutes').value);if(!Number.isInteger(n)||n<1||n>1440)throw new Error(t('err.queue.minutes'));return n}
$('queueMinutes').addEventListener('change',()=>{if(!ui.state?.queue?.length||ui.busy.size)return;try{const m=minutes();mutation('queue',()=>post('/api/queue',{slugs:ui.state.queue,minutes:m}))}catch(e){notify(e.message,true)}});
function reorder(slug,delta){const q=[...(ui.state?.queue||[])];const i=q.indexOf(slug);const j=i+delta;if(i<0||j<0||j>=q.length)return;[q[i],q[j]]=[q[j],q[i]];mutation('queue',()=>post('/api/queue',{slugs:q,minutes:minutes()}))}
const modal={root:$('modalRoot'),title:$('modalTitle'),msg:$('modalMsg'),input:$('modalInput'),
  ok:$('modalOk'),cancel:$('modalCancel'),opener:null,resolve:null};
function dialogOpen(opts,withInput){
  return new Promise(resolve=>{
    if(modal.resolve){const prev=modal.resolve;modal.resolve=null;prev(false)}
    modal.resolve=resolve;
    modal.opener=document.activeElement;
    text(modal.title,opts.title||'');
    text(modal.msg,opts.message||'');
    modal.input.hidden=!withInput;
    if(withInput){modal.input.value=opts.initial||'';modal.input.placeholder=opts.placeholder||'';modal.input.maxLength=Number(opts.maxLength)||256}
    modal.cancel.hidden=!!opts.hideCancel;
    setText(modal.cancel,opts.cancelText||t('dlg.cancel'));
    setText(modal.ok,opts.confirmText||t('dlg.ok'));
    modal.ok.className='btn '+(opts.danger?'danger':'primary');
    document.documentElement.style.overflow='hidden';
    modal.root.hidden=false;
    requestAnimationFrame(()=>modal.root.classList.add('is-open'));
    if(withInput)modal.input.focus();
    else if(!modal.cancel.hidden)modal.cancel.focus();
    else modal.ok.focus();
  });
}
function dialogClose(result){
  if(!modal.resolve)return;
  const resolve=modal.resolve;modal.resolve=null;
  modal.root.classList.remove('is-open');
  document.documentElement.style.overflow='';
  setTimeout(()=>{modal.root.hidden=true;
    if(modal.opener&&modal.opener.focus){try{modal.opener.focus()}catch(_){}}},200);
  resolve(result);
}
const dialogCancel=()=>dialogClose(modal.input.hidden?false:null);
modal.ok.addEventListener('click',()=>dialogClose(modal.input.hidden?true:modal.input.value.trim()));
modal.cancel.addEventListener('click',dialogCancel);
modal.root.addEventListener('mousedown',e=>{if(e.target===modal.root)dialogCancel()});
document.addEventListener('keydown',e=>{
  if(!modal.resolve)return;
  if(e.key==='Escape'){e.preventDefault();dialogCancel();return}
  if(e.key==='Enter'&&e.target!==modal.ok&&e.target!==modal.cancel){e.preventDefault();modal.ok.click();return}
  if(e.key==='Tab'){
    const f=[modal.ok,modal.cancel,modal.input].filter(el=>!el.hidden);
    const i=f.indexOf(document.activeElement);
    if(i<0||(e.shiftKey&&i===0)||(!e.shiftKey&&i===f.length-1)){
      e.preventDefault();f[e.shiftKey?f.length-1:0].focus();
    }
  }
},true);
function showConfirm(o){return dialogOpen(Object.assign({danger:false},o),false).then(v=>v===true)}
function showAlert(o){return dialogOpen(Object.assign({hideCancel:true},o),false).then(()=>true)}
function showPrompt(o){return dialogOpen(o,true).then(v=>v===null?null:v)}
document.addEventListener('click',async e=>{const b=e.target.closest('[data-act]');if(!b||b.disabled)return;const slug=b.dataset.slug,kind=b.dataset.act;if(kind==='icon'){ui.cards.get(slug)?.file.click();return}if(kind==='queue-up'){reorder(slug,-1);return}if(kind==='queue-down'){reorder(slug,1);return}if(kind==='rename'){const ref=ui.cards.get(slug);ui.exeEditing=ui.exeEditing===slug?null:slug;if(ref&&ui.exeEditing){const g=ui.state?.games.find(x=>x.slug===slug);ref.exeInput.value=(g&&g.executable)||''}if(ui.state)render(ui.state);if(ref&&ui.exeEditing)ref.exeInput.focus();return}if(kind==='exe-save'){const ref=ui.cards.get(slug);const name=(ref?ref.exeInput.value:'').trim();ui.exeEditing=null;mutation('exe',()=>post('/api/executable/'+encodeURIComponent(slug),{executable:name}),t('notify.exeSaved'));return}if(kind==='delete'&&!await showConfirm({title:t('dlg.delTitle'),message:t('dlg.delMsg'),confirmText:t('dlg.delete'),cancelText:t('dlg.cancel'),danger:true}))return;mutation(kind,async()=>{if(kind==='start')await post('/api/play',{slug});else if(kind==='stop')await post('/api/stop');else if(kind==='prepare')await post('/api/prepare/'+encodeURIComponent(slug));else if(kind==='delete')await api('/api/games/'+encodeURIComponent(slug),{method:'DELETE'});else if(kind==='queue'){const s=await api('/api/state');await post('/api/queue',{slugs:s.queue.includes(slug)?s.queue.filter(x=>x!==slug):[...s.queue,slug],minutes:minutes()})}},kind==='start'?t('notify.startRequested'):kind==='prepare'?t('notify.prepareDone'):kind==='delete'?t('dlg.deleted'):null)});
document.addEventListener('keydown',e=>{if(!ui.exeEditing)return;const input=e.target.closest?.('.exe-row input');if(!input)return;if(e.key==='Enter'){e.preventDefault();input.closest('.exe-row').querySelector('[data-act="exe-save"]').click()}else if(e.key==='Escape'){ui.exeEditing=null;if(ui.state)render(ui.state)}});
document.addEventListener('change',e=>{const slug=e.target.dataset?.icon,file=e.target.files?.[0];if(!slug||!file)return;if(file.size>2097152){notify(t('notify.iconTooLarge'),true);e.target.value='';return}mutation('icon',()=>api('/api/icon/'+encodeURIComponent(slug),{method:'POST',headers:{'X-Filename':encodeURIComponent(file.name),'Content-Type':'application/octet-stream'},body:file}),t('notify.iconSaved')).finally(()=>e.target.value='')});
$('stopAll').onclick=()=>mutation('stop',()=>post('/api/stop'),t('notify.stopRequested'));
$('sumStop').onclick=()=>mutation('stop',()=>post('/api/stop'),t('notify.stopRequested'));
$('resetSession').onclick=()=>endSession();
$('sumReset').onclick=()=>endSession();
async function endSession(){if(!await showConfirm({title:t('dlg.resetTitle'),message:t('dlg.resetMsg'),confirmText:t('dlg.end'),cancelText:t('dlg.cancel'),danger:true}))return;mutation('reset',()=>post('/api/session/reset'),t('notify.sessionDeleted'))}
$('clearQueue').onclick=()=>mutation('queue',()=>post('/api/queue',{slugs:[]}),t('notify.queueCleared'));
$('startQueue').onclick=()=>startQueueRun();
$('sumQueueStart').onclick=()=>startQueueRun();
function startQueueRun(){mutation('queue',async()=>{await post('/api/queue',{slugs:ui.state.queue,minutes:minutes()});await post('/api/queue/start')},t('notify.queueStarted'))}
/* ---------- pet: Molniya the lightning ---------- */
const pet={root:null,bubble:null,charge:0,saveTimer:null};
function petLevel(xp){return Math.min(99,Math.floor(xp/300)+1)}
function petInit(){
  try{pet.charge=Number(localStorage.getItem('worthlesstask.pet.charge'))||0}catch(_){pet.charge=0}
  const root=node('div','pet');root.dataset.state='idle';root.title=t('pet.hint');root.setAttribute('role','button');root.setAttribute('tabindex','0');root.setAttribute('aria-label',t('pet.name'));
  const ring=document.createElementNS(SVGNS,'svg');ring.setAttribute('class','pet-ring');ring.setAttribute('viewBox','0 0 60 60');const rc=document.createElementNS(SVGNS,'circle');rc.setAttribute('cx','30');rc.setAttribute('cy','30');rc.setAttribute('r','28');rc.setAttribute('fill','none');rc.setAttribute('stroke','rgba(215,228,255,.5)');rc.setAttribute('stroke-width','1.5');rc.setAttribute('stroke-dasharray','4 10');rc.setAttribute('stroke-linecap','round');ring.append(rc);
  const body=node('div','pet-body');
  const bolt=document.createElementNS(SVGNS,'svg');bolt.setAttribute('class','pet-bolt');bolt.setAttribute('viewBox','0 0 24 24');
  const bp=document.createElementNS(SVGNS,'path');bp.setAttribute('class','bolt-body');bp.setAttribute('d','M13.2 2.6 5.8 13.4h4.9l-1.4 8 7.9-11.2h-5.1z');
  const eye1=document.createElementNS(SVGNS,'circle');eye1.setAttribute('class','pet-eye');eye1.setAttribute('cx','10.2');eye1.setAttribute('cy','10.6');eye1.setAttribute('r','.85');
  const eye2=document.createElementNS(SVGNS,'circle');eye2.setAttribute('class','pet-eye');eye2.setAttribute('cx','13.6');eye2.setAttribute('cy','9.9');eye2.setAttribute('r','.85');
  const lid=document.createElementNS(SVGNS,'path');lid.setAttribute('class','pet-lid');lid.setAttribute('d','M9.3 10.7h1.9M12.7 10h1.9');lid.setAttribute('fill','none');
  bolt.append(bp,eye1,eye2,lid);body.append(bolt);
  const z1=node('span','pet-z z1','z'),z2=node('span','pet-z z2','z');
  const bubble=node('div','pet-bubble');
  bubble.innerHTML='<div class="pb-name"><span class="pb-n"></span><span class="pb-lvl"></span></div><div class="pb-bar"><span></span></div><div class="pb-mood"></div>';
  root.append(ring,body,z1,z2,bubble);
  pet.root=root;pet.bubble=bubble;
  const toggle=()=>{bubble.classList.toggle('open');paintPet()};
  root.addEventListener('click',toggle);
  root.addEventListener('keydown',e=>{if(e.key==='Enter'||e.key===' '){e.preventDefault();toggle()}});
  document.body.append(root);
}
function petCharge(sec){pet.charge+=sec;clearTimeout(pet.saveTimer);pet.saveTimer=setTimeout(()=>{try{localStorage.setItem('worthlesstask.pet.charge',String(pet.charge))}catch(_){}},4000);paintPet()}
function paintPet(){if(!pet.root)return;const s=ui.state;
const state=!ui.online?'sleep':(s&&(s.active||s.operation))?'work':'idle';
if(pet.root.dataset.state!==state)pet.root.dataset.state=state;
if(pet.bubble&&pet.bubble.classList.contains('open')){
  const lvl=petLevel(pet.charge);const pct=Math.round((pet.charge%300)/300*100);
  const n=pet.bubble.querySelector('.pb-n');if(n.textContent!==t('pet.name'))n.textContent=t('pet.name');
  text(pet.bubble.querySelector('.pb-lvl'),t('pet.lvl')+' '+lvl+' · '+pct+'%');
  pet.bubble.querySelector('.pb-bar span').style.width=pct+'%';
  const game=s&&s.active?s.active.game_name:null;
  const mood=!ui.online?t('pet.mood.sleep'):(game?t('pet.mood.work').replace('{game}',game):t('pet.mood.idle'));
  text(pet.bubble.querySelector('.pb-mood'),mood);
}}
petInit();
applyI18n();
showView(location.hash.slice(1));
poll();
</script></body></html>'''
