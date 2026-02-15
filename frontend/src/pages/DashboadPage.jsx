import React from "react";
import StatsCard from "../component/startsCards";
const Dashboard = () => {
  return (
    <div style={{ padding: "16px", overflowY: "auto" }}>
      <div className="stats-grid">
        <StatsCard title="Total Revenue" value="$45,231" color="red" />
        <StatsCard title="New Orders" value="1,234" color="green" />
        <StatsCard title="Total Visitors" value="8,549" color="blue" />
        <StatsCard title="Conversion Rate" value="3.2%" color="gray" />
      </div>
    </div>
  );
};

export default Dashboard;
