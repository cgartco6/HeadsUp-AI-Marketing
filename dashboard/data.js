// Sample dashboard data
const dashboardData = {
    growthTimeline: {
        labels: ['Week 1', 'Week 2', 'Month 1', 'Month 3', 'Month 6'],
        targets: [20, 50, 250, 600, 1000],
        actual: [22, 48, 230, 580, 1020]
    },
    
    provincialRevenue: {
        'ZA-GT': 89500, // Gauteng
        'ZA-WC': 67250, // Western Cape
        'ZA-KZN': 44180, // KwaZulu-Natal
        'ZA-EC': 30700,  // Eastern Cape
        'ZA-FS': 18950,  // Free State
        'ZA-MP': 32100,  // Mpumalanga
        'ZA-LP': 25800,  // Limpopo
        'ZA-NW': 19300,  // North West
        'ZA-NC': 14200   // Northern Cape
    },
    
    businessTiers: {
        smb: 58,    // Percentage
        medium: 28,  // Percentage
        enterprise: 14 // Percentage
    },
    
    contentPerformance: {
        platforms: ['TikTok', 'WhatsApp', 'Facebook', 'LinkedIn'],
        engagement: [85, 78, 65, 42] // Percentage
    },
    
    currentStats: {
        revenue: 189560,
        users: 428,
        growth: 18.7
    }
};
