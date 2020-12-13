import React from 'react';
import './App.css';
import { Switch,Route } from "react-router-dom";

import Users from "./pages/Users"



function App() {
  return (
    <Switch>
      <Route 
        exact
        path={["/", "/users"]}
        component={Users}
      />
    </Switch>
  );
}

export default App;
