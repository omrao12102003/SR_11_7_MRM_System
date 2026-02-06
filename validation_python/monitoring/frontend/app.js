async function loadDashboard() {
    try {
        const [modelsRes, approvalsRes, reportRes] = await Promise.all([
            fetch('/api/models'), 
            fetch('/api/approvals'),
            fetch('/api/report')
        ]);
        
        const models = await modelsRes.json();
        const approvals = await approvalsRes.json();
        const report = await reportRes.text();
        
        // Models ✓
        document.querySelector('#models tbody').innerHTML = 
            models.map(m => `<tr><td>${m.model_id}</td><td>${m.model_name}</td><td>${m.version}</td><td>${m.status}</td><td>${m.owner}</td></tr>`).join('');
        
        // Approvals as text (robust)
        const approvalsText = approvals.length ? 
            approvals.map(a => `${a.model_id}: ${a.timestamp}`).join('<br>') : 
            'No approvals data';
        document.querySelector('#approvals tbody').innerHTML = `<tr><td colspan="5">${approvalsText}</td></tr>`;
        
        document.getElementById('report').textContent = report;
        
    } catch(e) {
        document.getElementById('report').textContent = 'Error: ' + e.message;
    }
}

loadDashboard();
