// Enhanced functionality for Kruskal-s-Algorithm
const utils = {
    processData: (input) => {
        // Validate and process input data
        if (!input || typeof input !== 'object') {
            throw new Error('Invalid input data');
        }
        
        return {
            processed: true,
            timestamp: Date.now(),
            data: input,
            version: '2.0'
        };
    },
    
    validateInput: (data) => {
        return data && typeof data === 'object' && Object.keys(data).length > 0;
    },
    
    logActivity: (action, details) => {
        console.log(`[${new Date().toISOString()}] ${action}:`, details);
    }
};

export default utils;