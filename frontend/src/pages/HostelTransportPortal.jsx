import React, { useState, useEffect } from 'react';
import api from '../services/api';
import { useAuth } from '../context/AuthContext';
import { Home, Bus, MapPin, Phone, User, CheckCircle2, CreditCard, ShieldAlert } from 'lucide-react';

const HostelTransportPortal = () => {
    const { user } = useAuth();
    const [hostels, setHostels] = useState([]);
    const [busRoutes, setBusRoutes] = useState([]);
    const [activeTab, setActiveTab] = useState('hostels');

    useEffect(() => {
        fetchHostelTransportData();
    }, []);

    const fetchHostelTransportData = async () => {
        try {
            const [hostelRes, busRes] = await Promise.all([
                api.get('/api/hostel-transport/hostels'),
                api.get('/api/hostel-transport/bus-routes')
            ]);
            setHostels(hostelRes.data);
            setBusRoutes(busRes.data);
        } catch (err) {
            console.error('Failed to load hostel and transport info', err);
        }
    };

    return (
        <div className="space-y-8 animate-fade-in">
            {/* Header */}
            <div className="flex flex-col md:flex-row md:items-center justify-between gap-4 bg-gradient-to-r from-amber-900 via-orange-900 to-slate-900 p-8 rounded-3xl text-white shadow-xl">
                <div>
                    <div className="inline-flex items-center space-x-2 px-3 py-1 rounded-full bg-amber-500/20 text-amber-300 text-xs font-bold uppercase tracking-wider mb-3">
                        <Home className="h-3.5 w-3.5" />
                        <span>Campus Amenities & Logistics</span>
                    </div>
                    <h1 className="text-3xl font-black tracking-tight">Hostel & Transport Fleet Portal</h1>
                    <p className="text-slate-300 text-sm mt-1">Manage residence room allocations, mess schedules, and campus shuttle bus transit routes.</p>
                </div>
                <div className="flex space-x-2">
                    <button
                        onClick={() => setActiveTab('hostels')}
                        className={`px-5 py-2.5 rounded-xl text-xs font-bold transition-all ${
                            activeTab === 'hostels' ? 'bg-amber-500 text-slate-950 font-black shadow-md' : 'bg-slate-800 text-slate-300 hover:bg-slate-700'
                        }`}
                    >
                        Hostel Residences
                    </button>
                    <button
                        onClick={() => setActiveTab('transport')}
                        className={`px-5 py-2.5 rounded-xl text-xs font-bold transition-all ${
                            activeTab === 'transport' ? 'bg-amber-500 text-slate-950 font-black shadow-md' : 'bg-slate-800 text-slate-300 hover:bg-slate-700'
                        }`}
                    >
                        Bus Transit Routes
                    </button>
                </div>
            </div>

            {/* Tab 1: Hostels */}
            {activeTab === 'hostels' && (
                <div className="space-y-6">
                    <h2 className="text-xs font-black uppercase tracking-widest text-slate-500">Residential Halls & Blocks</h2>
                    <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
                        {hostels.map((h) => (
                            <div key={h.id} className="bg-white rounded-3xl p-6 border border-slate-200 shadow-sm space-y-4 hover:shadow-md transition-all">
                                <div className="flex justify-between items-start">
                                    <div>
                                        <span className="text-[10px] font-bold px-2 py-0.5 rounded-md bg-amber-50 text-amber-700 border border-amber-200">
                                            {h.type} Hostel
                                        </span>
                                        <h3 className="text-lg font-black text-slate-800 mt-2">{h.name}</h3>
                                    </div>
                                    <span className="text-xs font-bold text-slate-500">{h.total_rooms} Rooms</span>
                                </div>

                                <div className="space-y-2 text-xs text-slate-600">
                                    <p className="flex items-center"><User className="h-3.5 w-3.5 mr-2 text-slate-400" /> Warden: <span className="font-bold ml-1 text-slate-800">{h.warden_name}</span></p>
                                    <p className="flex items-center"><Phone className="h-3.5 w-3.5 mr-2 text-slate-400" /> {h.warden_phone}</p>
                                    <p className="flex items-center"><MapPin className="h-3.5 w-3.5 mr-2 text-slate-400" /> {h.address}</p>
                                </div>

                                <div className="pt-4 border-t border-slate-100 flex justify-between items-center text-xs">
                                    <span className="text-slate-400">Mess & Laundry Included</span>
                                    <span className="font-black text-emerald-600">₹35,000 / Sem</span>
                                </div>
                            </div>
                        ))}
                    </div>
                </div>
            )}

            {/* Tab 2: Transport */}
            {activeTab === 'transport' && (
                <div className="space-y-6">
                    <h2 className="text-xs font-black uppercase tracking-widest text-slate-500">Active Shuttle Bus Routes</h2>
                    <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
                        {busRoutes.map((rt) => (
                            <div key={rt.id} className="bg-white rounded-3xl p-6 border border-slate-200 shadow-sm space-y-4 hover:shadow-md transition-all">
                                <div className="flex justify-between items-start">
                                    <div className="flex items-center space-x-3">
                                        <div className="p-3 bg-orange-50 text-orange-600 rounded-2xl border border-orange-200">
                                            <Bus className="h-6 w-6" />
                                        </div>
                                        <div>
                                            <span className="text-xs font-black text-orange-600 uppercase tracking-wider">{rt.route_number}</span>
                                            <h3 className="text-base font-black text-slate-800">{rt.route_name}</h3>
                                        </div>
                                    </div>
                                    <span className="text-xs font-bold text-slate-600 bg-slate-100 px-3 py-1 rounded-full">{rt.departure_time}</span>
                                </div>

                                <div className="grid grid-cols-2 gap-3 py-3 border-y border-slate-100 text-xs">
                                    <div>
                                        <span className="text-slate-400 block text-[10px] uppercase font-bold">Start Origin</span>
                                        <span className="font-bold text-slate-700">{rt.start_point}</span>
                                    </div>
                                    <div>
                                        <span className="text-slate-400 block text-[10px] uppercase font-bold">Destination</span>
                                        <span className="font-bold text-slate-700">{rt.end_point}</span>
                                    </div>
                                    <div>
                                        <span className="text-slate-400 block text-[10px] uppercase font-bold">Driver</span>
                                        <span className="font-bold text-slate-700">{rt.driver_name} ({rt.driver_phone})</span>
                                    </div>
                                    <div>
                                        <span className="text-slate-400 block text-[10px] uppercase font-bold">Bus Number</span>
                                        <span className="font-bold text-slate-700">{rt.bus_number}</span>
                                    </div>
                                </div>
                            </div>
                        ))}
                    </div>
                </div>
            )}
        </div>
    );
};

export default HostelTransportPortal;
