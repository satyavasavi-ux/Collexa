import React from 'react';

export const Button = ({ children, variant = 'primary', size = 'md', className = '', ...props }) => {
    const base = "inline-flex items-center justify-center font-bold rounded-2xl transition-all duration-200 focus:outline-none focus:ring-2 focus:ring-offset-2 disabled:opacity-50";
    const variants = {
        primary: "bg-indigo-600 hover:bg-indigo-700 text-white shadow-md shadow-indigo-600/20 focus:ring-indigo-500",
        secondary: "bg-slate-100 hover:bg-slate-200 text-slate-800 focus:ring-slate-400",
        danger: "bg-rose-600 hover:bg-rose-700 text-white shadow-md shadow-rose-600/20 focus:ring-rose-500",
        success: "bg-emerald-600 hover:bg-emerald-700 text-white shadow-md shadow-emerald-600/20 focus:ring-emerald-500",
        outline: "border border-slate-300 hover:bg-slate-50 text-slate-700 focus:ring-slate-400"
    };
    const sizes = {
        sm: "px-3 py-1.5 text-xs",
        md: "px-5 py-2.5 text-xs",
        lg: "px-6 py-3 text-sm"
    };
    return (
        <button className={`${base} ${variants[variant] || variants.primary} ${sizes[size] || sizes.md} ${className}`} {...props}>
            {children}
        </button>
    );
};
