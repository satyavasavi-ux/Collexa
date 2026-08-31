import React from 'react';

export const Card = ({ children, className = '', hover = true }) => {
    return (
        <div className={`bg-white rounded-3xl p-6 border border-slate-200 shadow-sm ${hover ? 'hover:shadow-md' : ''} transition-all ${className}`}>
            {children}
        </div>
    );
};
