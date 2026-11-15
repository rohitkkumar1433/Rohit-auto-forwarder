const statusEl=document.getElementById('status');
document.getElementById('start').addEventListener('click',()=>{statusEl.textContent='Status: Demo only — backend is not connected.';});
document.getElementById('stop').addEventListener('click',()=>{statusEl.textContent='Status: Stopped (demo).';});
