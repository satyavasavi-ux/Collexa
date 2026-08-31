import React, { useState, useEffect } from 'react';
import api from '../services/api';
import { useAuth } from '../context/AuthContext';
import { Calendar, Ticket, MapPin, Clock, Award, CheckCircle2, Users, Sparkles } from 'lucide-react';

const EventsClubsPortal = () => {
    const { user } = useAuth();
    const [events, setEvents] = useState([]);
    const [myTickets, setMyTickets] = useState([]);
    const [msg, setMsg] = useState('');

    useEffect(() => {
        fetchEvents();
    }, []);

    const fetchEvents = async () => {
        try {
            const [evtRes, tktRes] = await Promise.all([
                api.get('/api/events/'),
                api.get('/api/events/my-tickets')
            ]);
            setEvents(evtRes.data);
            setMyTickets(tktRes.data);
        } catch (err) {
            console.error('Failed to load campus events', err);
        }
    };

    const handleRegister = async (eventId) => {
        try {
            const res = await api.post(`/api/events/${eventId}/register`);
            setMsg(`Registered successfully! Your Ticket Pass Code is: ${res.data.ticket_code}`);
            setTimeout(() => setMsg(''), 6000);
            fetchEvents();
        } catch (err) {
            alert(err.response?.data?.detail || 'Failed to register for event');
        }
    };

    return (
        <div className="space-y-8 animate-fade-in">
            {/* Header */}
            <div className="flex flex-col md:flex-row md:items-center justify-between gap-4 bg-gradient-to-r from-rose-900 via-pink-900 to-slate-900 p-8 rounded-3xl text-white shadow-xl">
                <div>
                    <div className="inline-flex items-center space-x-2 px-3 py-1 rounded-full bg-rose-500/20 text-rose-300 text-xs font-bold uppercase tracking-wider mb-3">
                        <Sparkles className="h-3.5 w-3.5" />
                        <span>Campus Life & Innovation</span>
                    </div>
                    <h1 className="text-3xl font-black tracking-tight">Events, Hackathons & Student Clubs</h1>
                    <p className="text-slate-300 text-sm mt-1">Discover campus workshops, tech conferences, hackathons, and cultural festivals.</p>
                </div>
            </div>

            {msg && (
                <div className="p-4 rounded-2xl bg-emerald-50 border border-emerald-200 text-emerald-800 text-sm font-bold flex items-center shadow-sm">
                    <CheckCircle2 className="h-4 w-4 mr-2 text-emerald-600" />
                    {msg}
                </div>
            )}

            {/* My Registered Passes */}
            {myTickets.length > 0 && (
                <div className="bg-white rounded-3xl p-6 border border-slate-200 shadow-sm space-y-4">
                    <h3 className="text-xs font-black uppercase tracking-widest text-rose-600 flex items-center">
                        <Ticket className="h-4 w-4 mr-1.5" />
                        Your Event Ticket Passes ({myTickets.length})
                    </h3>
                    <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
                        {myTickets.map((tkt) => (
                            <div key={tkt.id} className="p-4 rounded-2xl bg-gradient-to-br from-rose-50 to-pink-50 border border-rose-200 space-y-2">
                                <div className="flex justify-between items-center">
                                    <span className="text-xs font-black text-rose-800">Pass Code</span>
                                    <span className="text-xs font-mono font-black bg-rose-600 text-white px-2 py-0.5 rounded-lg">{tkt.ticket_code}</span>
                                </div>
                                <p className="text-xs text-slate-700 font-bold">Event ID #{tkt.event_id}</p>
                                <p className="text-[10px] text-slate-500">Status: {tkt.attendance_status}</p>
                            </div>
                        ))}
                    </div>
                </div>
            )}

            {/* Events Grid */}
            <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
                {events.map((evt) => (
                    <div key={evt.id} className="bg-white rounded-3xl p-6 border border-slate-200 shadow-sm space-y-4 hover:shadow-md transition-all">
                        <div className="flex justify-between items-start">
                            <div>
                                <span className="text-[10px] font-bold px-2 py-0.5 rounded-md bg-rose-50 text-rose-700 border border-rose-200 uppercase">
                                    {evt.category}
                                </span>
                                <h3 className="text-xl font-black text-slate-800 mt-2">{evt.title}</h3>
                                <p className="text-xs font-bold text-slate-500">Organized by {evt.organizer}</p>
                            </div>
                        </div>

                        <p className="text-xs text-slate-600 leading-relaxed">{evt.description}</p>

                        <div className="grid grid-cols-2 gap-3 py-3 border-y border-slate-100 text-xs text-slate-600">
                            <span className="flex items-center"><Calendar className="h-3.5 w-3.5 mr-1 text-slate-400" /> {new Date(evt.start_time).toLocaleDateString()}</span>
                            <span className="flex items-center"><MapPin className="h-3.5 w-3.5 mr-1 text-slate-400" /> {evt.venue}</span>
                        </div>

                        <div className="flex justify-between items-center pt-2">
                            <span className="text-xs font-black text-emerald-600">{evt.registration_fee > 0 ? `₹${evt.registration_fee}` : 'Free Entry'}</span>
                            <button
                                onClick={() => handleRegister(evt.id)}
                                className="px-5 py-2.5 bg-rose-600 hover:bg-rose-700 text-white text-xs font-bold rounded-xl shadow-md transition-all"
                            >
                                RSVP / Register
                            </button>
                        </div>
                    </div>
                ))}
            </div>
        </div>
    );
};

export default EventsClubsPortal;
