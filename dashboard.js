// Initialize Dashboard
document.addEventListener('DOMContentLoaded', function() {
    // Update live stats
    document.getElementById('revenue').textContent = `R ${dashboardData.currentStats.revenue.toLocaleString()}`;
    document.getElementById('users').textContent = dashboardData.currentStats.users;
    document.getElementById('growth').textContent = `+${dashboardData.currentStats.growth}%`;
    
    // Create Growth Chart
    const growthChart = document.getElementById('growthChart');
    Plotly.newPlot(growthChart, [{
        x: dashboardData.growthTimeline.labels,
        y: dashboardData.growthTimeline.actual,
        type: 'scatter+markers',
        mode: 'lines+markers',
        name: 'Actual Users',
        line: {color: '#4CAF50', width: 3},
        marker: {size: 10}
    }, {
        x: dashboardData.growthTimeline.labels,
        y: dashboardData.growthTimeline.targets,
        type: 'scatter',
        mode: 'lines',
        name: 'Target',
        line: {color: '#2a5298', width: 2, dash: 'dash'}
    }], {
        title: 'Subscriber Growth Target: 1,000 by Month 6',
        xaxis: {title: 'Timeline'},
        yaxis: {title: 'Active Users'},
        showlegend: true,
        legend: {orientation: 'h', y: -0.2}
    });
    
    // Create SA Revenue Map
    const mapData = [{
        type: 'choropleth',
        locations: Object.keys(dashboardData.provincialRevenue),
        z: Object.values(dashboardData.provincialRevenue),
        geojson: southAfricaGeoJSON,
        colorscale: 'Blues',
        hoverinfo: 'location+z',
        name: 'Revenue (R)',
        showscale: true
    }];
    
    const mapLayout = {
        title: 'Revenue by Province',
        geo: {
            scope: 'africa',
            center: {lon: 25, lat: -29},
            zoom: 4,
            showframe: false,
            showcoastlines: false,
            projection: {type: 'mercator'}
        },
        margin: {t: 30, b: 0, l: 0, r: 0}
    };
    
    Plotly.newPlot('saMap', mapData, mapLayout);
    
    // Create Business Tier Chart
    const tierData = [{
        values: Object.values(dashboardData.businessTiers),
        labels: Object.keys(dashboardData.businessTiers).map(k => 
            k === 'smb' ? 'Small Business' : 
            k === 'medium' ? 'Medium Business' : 'Enterprise'),
        type: 'pie',
        hole: 0.4,
        marker: {
            colors: ['#FFC107', '#2196F3', '#4CAF50']
        }
    }];
    
    const tierLayout = {
        showlegend: true,
        legend: {orientation: 'h', y: -0.1}
    };
    
    Plotly.newPlot('tierChart', tierData, tierLayout);
    
    // Create Content Performance Chart
    const contentData = [{
        x: dashboardData.contentPerformance.platforms,
        y: dashboardData.contentPerformance.engagement,
        type: 'bar',
        marker: {color: '#2a5298'}
    }];
    
    const contentLayout = {
        yaxis: {
            title: 'Engagement (%)',
            range: [0, 100]
        }
    };
    
    Plotly.newPlot('contentChart', contentData, contentLayout);
    
    // Timeline activation
    const timelineSteps = document.querySelectorAll('.timeline-step');
    timelineSteps.forEach((step, index) => {
        if (index <= 1) { // Activate first two steps
            step.classList.add('active');
        }
    });
    
    // Demo button functionality
    document.querySelector('.demo-button').addEventListener('click', function() {
        alert('Live demo would launch here!\nScanning receipt...\nComparing prices...\nShowing savings!');
    });
});
