import React from "react";
import { MapContainer, TileLayer } from "react-leaflet";

function App() {
  return (
    <div className="h-screen w-screen flex flex-col">
      {/* Top bar */}
      <header className="h-12 bg-slate-900 text-white flex items-center px-4">
        <h1 className="font-semibold">PropFlow</h1>
      </header>

      {/* Main content */}
      <div className="flex flex-1">
        {/* Left sidebar */}
        <div className="w-1/4 bg-slate-50 border-r border-slate-200 p-4">
          <h2 className="font-semibold mb-2">Search</h2>
          <form className="flex gap-2 mb-4">
            <input
              type="text"
              placeholder="Enter postcode (e.g. E5)"
              className="flex-1 border border-slate-300 rounded px-2 py-1 text-sm"
            />
            <button
              type="submit"
              className="bg-slate-900 text-white px-3 py-1 text-sm rounded"
            >
              Go
            </button>
          </form>

          <h3 className="font-semibold mb-2 text-sm">
            Top priority properties
          </h3>
          <ul className="space-y-2 text-xs">
            <li className="p-2 border rounded bg-white">
              (List items will go here)
            </li>
          </ul>
        </div>

        {/* Map */}
        <div className="flex-1 relative">
          <MapContainer
            center={[51.5074, -0.1278]} // London
            zoom={11}
            className="h-full w-full"
          >
            <TileLayer
              url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
              attribution="&copy; OpenStreetMap contributors"
            />
          </MapContainer>
        </div>

        {/* Right panel */}
        <div className="w-1/3 bg-white border-l border-slate-200 p-4">
          <h2 className="font-semibold mb-2">Property details</h2>
          <p className="text-sm text-slate-600">
            When you click a property on the map, details will appear here.
          </p>
        </div>
      </div>
    </div>
  );
}

export default App;
