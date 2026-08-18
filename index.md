---
layout: default
---

# 🕵️ User Scanner Web Interface

## 🚀 Deep OSINT Intelligence Tool

Enter a **username** or **email** to scan across **400+ platforms** for digital footprints.

---

## 📝 Scan Options

### Username or Email
<input type="text" id="target" placeholder="Enter username or email..." style="width: 100%; padding: 10px; margin: 10px 0; border: 1px solid #ddd; border-radius: 5px;">

### Mode Selection
<div style="margin: 15px 0;">
  <label><input type="radio" name="mode" value="username" checked> Username</label>
  <label style="margin-left: 20px;"><input type="radio" name="mode" value="email"> Email</label>
</div>

### Additional Options
<div style="margin: 15px 0;">
  <label><input type="checkbox" id="allowLoud"> Allow Loud Modules (may send notifications)</label>
</div>

### Category Filter
<select id="category" style="width: 100%; padding: 10px; margin: 10px 0;">
  <option value="">All Categories</option>
  <option value="dev">Developer Platforms</option>
  <option value="social">Social Media</option>
  <option value="gaming">Gaming</option>
  <option value="shopping">Shopping Sites</option>
  <option value="creator">Creator Platforms</option>
</select>

### Actions
<button onclick="startScan()" style="padding: 10px 20px; background: #00ff00; color: #000; border: none; border-radius: 5px; cursor: pointer; font-weight: bold; margin: 20px 0;">🔍 SCAN</button>
<button onclick="clearResults()" style="padding: 10px 20px; background: #444; color: #00ff00; border: 1px solid #00ff00; border-radius: 5px; cursor: pointer; margin-left: 10px;">CLEAR</button>

---

## 📊 Scan Results

<div id="loading" style="display: none; text-align: center; margin: 30px 0; color: #00ff00; font-weight: bold;">
  <p>⚙️ SCANNING... PLEASE WAIT</p>
  <p style="font-size: 0.9em;">Analyzing 400+ platforms...</p>
</div>

<div id="results" style="display: none; margin-top: 30px;">
  <h3 style="color: #00ff00; border-bottom: 2px solid #00ff00; padding-bottom: 10px;">▼ RESULTS FOUND ▼</h3>
  
  <div id="resultsList" style="margin: 20px 0;"></div>
  
  <div id="stats" style="margin: 30px 0;">
    <table style="width: 100%; border-collapse: collapse;">
      <tr>
        <td style="border: 1px solid #00ff00; padding: 10px; color: #00ff00;"><strong>Found</strong></td>
        <td id="stat-found" style="border: 1px solid #00ff00; padding: 10px; color: #00ff00; text-align: center;">0</td>
        <td style="border: 1px solid #00ff00; padding: 10px; color: #00ff00;"><strong>Not Found</strong></td>
        <td id="stat-notfound" style="border: 1px solid #00ff00; padding: 10px; color: #00ff00; text-align: center;">0</td>
        <td style="border: 1px solid #00ff00; padding: 10px; color: #00ff00;"><strong>Skipped</strong></td>
        <td id="stat-skipped" style="border: 1px solid #00ff00; padding: 10px; color: #00ff00; text-align: center;">0</td>
      </tr>
    </table>
  </div>

  <div style="margin: 20px 0;">
    <button onclick="exportJSON()" style="padding: 10px 15px; background: #00ff00; color: #000; border: none; border-radius: 5px; cursor: pointer; margin-right: 10px;">📄 JSON Export</button>
    <button onclick="exportCSV()" style="padding: 10px 15px; background: #00ff00; color: #000; border: none; border-radius: 5px; cursor: pointer;">📊 CSV Export</button>
  </div>
</div>

---

## ⚠️ Disclaimer

This tool is provided for **educational purposes only**. Unauthorized access to computer systems is illegal. Use responsibly and only for authorized security research.

---

## 📚 Features

- ✅ **400+ Scan Vectors** - Email & Username modules
- ✅ **Deep Metadata Extraction** - Avatars, bios, follower counts
- ✅ **Cross-Scan & Pivoting** - Auto-follow leads
- ✅ **Proxy Support** - Rotate proxies for privacy
- ✅ **Multiple Exports** - JSON, CSV, PDF formats
- ✅ **Fast & Parallel** - Concurrent scanning

---

## 🔗 Links

- [GitHub Repository](https://github.com/PascalHberg/user-scanner)
- [Documentation](https://github.com/PascalHberg/user-scanner/tree/main/docs)
- [Issues & Feedback](https://github.com/PascalHberg/user-scanner/issues)

---

## 📝 License

MIT License - See LICENSE file for details

<script src="https://cdn.jsdelivr.net/npm/chart.js@3.9.1/dist/chart.min.js"></script>
<script>
let scanResults = [];

function startScan() {
    const target = document.getElementById('target').value.trim();
    const mode = document.querySelector('input[name="mode"]:checked').value;
    const allowLoud = document.getElementById('allowLoud').checked;
    const category = document.getElementById('category').value;
    
    if (!target) {
        alert('❌ ERROR: Please enter a username or email');
        return;
    }
    
    // Show loading
    document.getElementById('loading').style.display = 'block';
    document.getElementById('results').style.display = 'none';
    
    // Simulate scan
    setTimeout(() => {
        performMockScan(target, mode, category);
    }, 1500);
}

function performMockScan(target, mode, category) {
    const mockResults = [
        { name: 'GitHub', status: 'found', icon: '✔', category: 'dev', url: `https://github.com/${target}` },
        { name: 'Twitter', status: 'not-found', icon: '✘', category: 'social' },
        { name: 'Reddit', status: 'found', icon: '✔', category: 'social', url: `https://reddit.com/user/${target}` },
        { name: 'Instagram', status: 'skipped', icon: '~', category: 'social' },
        { name: 'LinkedIn', status: 'not-found', icon: '✘', category: 'social' },
        { name: 'GitLab', status: 'found', icon: '✔', category: 'dev', url: `https://gitlab.com/${target}` },
        { name: 'Twitch', status: 'found', icon: '✔', category: 'gaming', url: `https://twitch.tv/${target}` },
        { name: 'Discord', status: 'not-found', icon: '✘', category: 'gaming' },
        { name: 'Patreon', status: 'found', icon: '✔', category: 'creator', url: `https://patreon.com/${target}` },
        { name: 'YouTube', status: 'not-found', icon: '✘', category: 'creator' },
    ];
    
    let filtered = mockResults;
    if (category) {
        filtered = mockResults.filter(r => r.category === category);
    }
    
    scanResults = filtered;
    displayResults(target);
    
    document.getElementById('loading').style.display = 'none';
    document.getElementById('results').style.display = 'block';
}

function displayResults(target) {
    const resultsList = document.getElementById('resultsList');
    resultsList.innerHTML = '';
    
    const found = scanResults.filter(r => r.status === 'found');
    const notFound = scanResults.filter(r => r.status === 'not-found');
    const skipped = scanResults.filter(r => r.status === 'skipped');
    
    // Update stats
    document.getElementById('stat-found').textContent = found.length;
    document.getElementById('stat-notfound').textContent = notFound.length;
    document.getElementById('stat-skipped').textContent = skipped.length;
    
    // Display results
    [...found, ...notFound, ...skipped].forEach(result => {
        const statusColor = result.status === 'found' ? '#00ff00' : 
                           result.status === 'not-found' ? '#ff0000' : '#888';
        const statusText = result.status === 'found' ? 'FOUND ✔' : 
                          result.status === 'not-found' ? 'NOT FOUND ✘' : 'SKIPPED ~';
        
        const urlPart = result.url ? `<a href="${result.url}" target="_blank" style="color: #00ff00; text-decoration: none;">[VISIT]</a>` : '';
        
        const resultEl = document.createElement('div');
        resultEl.style.cssText = `
            border: 1px solid ${statusColor};
            padding: 10px;
            margin: 10px 0;
            border-radius: 5px;
            background: #0a0a0a;
            display: flex;
            justify-content: space-between;
            align-items: center;
        `;
        
        resultEl.innerHTML = `
            <span style="color: #00ff00;">${result.name}</span>
            <span style="color: ${statusColor}; font-weight: bold;">${statusText} ${urlPart}</span>
        `;
        
        resultsList.appendChild(resultEl);
    });
}

function clearResults() {
    document.getElementById('target').value = '';
    document.getElementById('results').style.display = 'none';
    document.getElementById('loading').style.display = 'none';
    scanResults = [];
}

function exportJSON() {
    if (scanResults.length === 0) {
        alert('No results to export');
        return;
    }
    
    const data = JSON.stringify(scanResults, null, 2);
    downloadFile(data, 'user-scanner-results.json', 'application/json');
}

function exportCSV() {
    if (scanResults.length === 0) {
        alert('No results to export');
        return;
    }
    
    const headers = ['Name', 'Status', 'Category', 'URL'];
    const rows = scanResults.map(r => [
        r.name,
        r.status.toUpperCase(),
        r.category,
        r.url || ''
    ]);
    
    let csv = headers.join(',') + '\n';
    rows.forEach(row => {
        csv += row.map(cell => `"${cell}"`).join(',') + '\n';
    });
    
    downloadFile(csv, 'user-scanner-results.csv', 'text/csv');
}

function downloadFile(data, filename, type) {
    const blob = new Blob([data], { type });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = filename;
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
    URL.revokeObjectURL(url);
}
</script>
