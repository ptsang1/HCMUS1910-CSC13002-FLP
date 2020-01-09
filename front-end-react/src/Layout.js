import React, { Component } from 'react';
import './App.css';
import { BrowserRouter as Router, Switch, Route } from 'react-router-dom';
import Home from './Home'
import SearchResult from './searchResult'
import WriteRecipe from './WriteRecipe';
import User from './User';
import Nav from './Nav';

function Layout(){
  return (
    <div>
      <Nav />
      <Switch>
        <Route path="/" exact component={Home} />
        <Route path="/searchresults" exact component={SearchResult} />
        <Route path="/writerecipe" component={WriteRecipe} />
        <Route path="/user" exact component={User} />
      </Switch>
    </div>
  )
}

export default Layout;