import logo from './logo.svg';
import './App.css';
import React, { useEffect, useState } from "react";
import { BarChart, Bar, XAxis, YAxis, Tooltip, CartesianGrid } from "recharts";

const SalesDashboard = () => {
  const [salesData, setSalesData] = useState([]);

  useEffect(() => {
    fetch("http://localhost:8000/sales_data")
      .then((response) => response.json())
      .then((data) => setSalesData(data));
  }, []);
  return (
    <div class = "Chart">
      <h2 class = "App">Sales Performance Dashboard</h2>
      <BarChart width={1000} height={500} data={salesData}>
        <CartesianGrid strokeDasharray="4 4" />
        <XAxis dataKey="region" />
        <YAxis />
        <Tooltip />
        <Bar dataKey="revenue" fill="#880808" />
      </BarChart>
    </div>
  );
};

export default SalesDashboard;
