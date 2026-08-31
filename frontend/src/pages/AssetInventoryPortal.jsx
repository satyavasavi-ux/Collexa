import React, { useState, useEffect } from 'react';
import api from '../services/api';
import { Package, ShieldCheck, AlertTriangle, Search, CheckCircle2 } from 'lucide-react';

const AssetInventoryPortal = () => {
    const [assets, setAssets] = useState([]);

    useEffect(() => {
        api.get('/api/inventory/assets').then(res => setAssets(res.data)).catch(console.error);
    }, []);

    return (
        <div className="space-y-8 animate-fade-in">
            <div className="bg-gradient-to-r from-slate-900 via-indigo-950 to-slate-900 p-8 rounded-3xl text-white shadow-xl">
                <div className="inline-flex items-center space-x-2 px-3 py-1 rounded-full bg-indigo-500/20 text-indigo-300 text-xs font-bold uppercase tracking-wider mb-3">
                    <Package className="h-3.5 w-3.5" />
                    <span>Campus Asset & Laboratory Inventory</span>
                </div>
                <h1 className="text-3xl font-black tracking-tight">Equipment Registry & Depreciation Auditing</h1>
            </div>

            <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
                {assets.map(a => (
                    <div key={a.id} className="bg-white p-6 rounded-3xl border border-slate-200 shadow-sm space-y-3">
                        <div className="flex justify-between items-start">
                            <div>
                                <span className="text-[10px] font-bold px-2 py-0.5 rounded-md bg-indigo-50 text-indigo-700 border border-indigo-200">{a.category}</span>
                                <h3 className="text-base font-black text-slate-800 mt-1">{a.name}</h3>
                            </div>
                            <span className="text-xs font-bold text-slate-500">{a.years_in_service} yrs in service</span>
                        </div>
                        <div className="grid grid-cols-2 gap-3 py-2 border-y border-slate-100 text-xs">
                            <div><span className="text-slate-400 block text-[10px] uppercase font-bold">Purchase Cost</span><span className="font-bold text-slate-700">₹{a.original_cost?.toLocaleString()}</span></div>
                            <div><span className="text-slate-400 block text-[10px] uppercase font-bold">Book Value</span><span className="font-bold text-emerald-600">₹{a.depreciated_book_value?.toLocaleString()}</span></div>
                        </div>
                        <div className="flex justify-between items-center text-xs font-bold">
                            <span className="text-indigo-600">{a.lifecycle_status}</span>
                            <span className="text-slate-400">Salvage: ₹{a.salvage_estimate?.toLocaleString()}</span>
                        </div>
                    </div>
                ))}
            </div>
        </div>
    );
};

export default AssetInventoryPortal;
