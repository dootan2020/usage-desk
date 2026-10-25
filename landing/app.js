'use strict';
const menu=document.querySelector('.menu-toggle'),links=document.querySelector('#nav-links');
menu.addEventListener('click',()=>{const open=menu.getAttribute('aria-expanded')!=='true';menu.setAttribute('aria-expanded',String(open));links.classList.toggle('open',open);});
links.addEventListener('click',e=>{if(e.target.closest('a')){menu.setAttribute('aria-expanded','false');links.classList.remove('open');}});
const tabs=[...document.querySelectorAll('[role=tab]')];
function selectTab(tab){for(const item of tabs){const selected=item===tab;item.setAttribute('aria-selected',String(selected));item.tabIndex=selected?0:-1;document.getElementById(item.getAttribute('aria-controls')).hidden=!selected;}}
for(const tab of tabs){tab.addEventListener('click',()=>selectTab(tab));tab.addEventListener('keydown',e=>{if(!['ArrowRight','ArrowLeft','Home','End'].includes(e.key))return;e.preventDefault();const index=tabs.indexOf(tab),next=e.key==='Home'?0:e.key==='End'?tabs.length-1:(index+(e.key==='ArrowRight'?1:-1)+tabs.length)%tabs.length;selectTab(tabs[next]);tabs[next].focus();});}
document.getElementById('copy-checksum').addEventListener('click',async()=>{const text=document.getElementById('checksum').textContent;try{await navigator.clipboard.writeText(text);document.getElementById('copy-status').textContent='Checksum copied.';}catch{document.getElementById('copy-status').textContent='Select the checksum above and copy it manually.';}});
const glance=document.getElementById('taskbar-glance'),providers=[['⌘','ChatGPT & Codex'],['✳','Claude'],['✦','Antigravity']];let active=0,timer=null;
function advance(){active=(active+1)%providers.length;document.getElementById('glance-icon').textContent=providers[active][0];document.getElementById('glance-name').textContent=providers[active][1];}
function pause(){clearInterval(timer);timer=null;}
function resume(){pause();if(!matchMedia('(prefers-reduced-motion: reduce)').matches&&!document.hidden)timer=setInterval(advance,5000);}
glance.addEventListener('click',advance);glance.addEventListener('mouseenter',pause);glance.addEventListener('mouseleave',resume);glance.addEventListener('focus',pause);glance.addEventListener('blur',resume);document.addEventListener('visibilitychange',()=>document.hidden?pause():resume());resume();
