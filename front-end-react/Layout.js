import React, { Component } from 'react';
import './App.css';
import { BrowserRouter as Router, Switch, Route } from 'react-router-dom';
import Home from './Home'
import WriteRecipe from './WriteRecipe';
import Nav from './Nav';

function Layout() {
    return (
        // <Nav>
            <Switch>
                <Route path="/" exact component={Home} />
                <Route path="/writerecipe" component={WriteRecipe} />
            </Switch>
        // </Nav>
    )
}

export default Layout;