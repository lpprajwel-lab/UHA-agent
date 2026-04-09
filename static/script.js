document.getElementById('run-btn').addEventListener('click', async () => {
    const statusEl = document.getElementById('agent-status');
    const resultsContainer = document.getElementById('results-container');
    const btn = document.getElementById('run-btn');
    
    statusEl.className = 'status-indicator processing';
    statusEl.innerText = 'Status: Agent Reasoning in Progress...';
    btn.disabled = true;
    btn.style.opacity = '0.7';
    resultsContainer.innerHTML = '';
    
    // add small artificial delay for visual effect
    await new Promise(r => setTimeout(r, 600));

    try {
        const response = await fetch('/run', { method: 'POST' });
        const data = await response.json();
        
        if (data.status === 'success') {
            statusEl.className = 'status-indicator done';
            statusEl.innerText = 'Status: Analysis Complete';
            
            data.data.forEach((item, index) => {
                const delay = index * 100;
                const solutionsHtml = item.solutions.map(s => `<li>${s}</li>`).join('');
                
                const card = document.createElement('div');
                card.className = 'result-card';
                card.style.animationDelay = `${delay}ms`;
                
                card.innerHTML = `
                    <div class="card-header">
                        <h2>${item.area}</h2>
                        <span class="risk-badge risk-${item.risk_level}">${item.risk_level} RISK</span>
                    </div>
                    <h3>Reasoning Engine</h3>
                    <p class="reason">${item.reason}</p>
                    <h3>Suggested Interventions</h3>
                    <ul class="solutions">${solutionsHtml}</ul>
                    <div class="impact" style="text-align: center;">Expected Impact: ${item.impact}</div>
                `;
                resultsContainer.appendChild(card);
            });
        } else {
            statusEl.className = 'status-indicator idle';
            statusEl.innerText = 'Status: Error - ' + data.message;
        }
    } catch (e) {
        statusEl.className = 'status-indicator idle';
        statusEl.innerText = 'Status: Error starting agent';
        console.error(e);
    } finally {
        btn.disabled = false;
        btn.style.opacity = '1';
    }
});
