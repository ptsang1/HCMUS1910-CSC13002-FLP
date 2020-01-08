import React, { Component } from 'react';
import './App.css';
import { BrowserRouter as Router, Switch, Route } from 'react-router-dom';
import Home from './Home'
import SearchResult from './searchResult'
import WriteRecipe from './WriteRecipe';
import User from './User';
import Nav from './Nav';

class Layout extends Component {
  state = {
    keyword: '',
    user_id: ''
  }

  handleSearch = (keyword) => {
    this.setState({
      keyword
    })
  }

  goToPersonalPage = (user_id) => {
    this.setState({
      user_id
    })
  }

  render() {
    return (
      <div>
        <Nav handleSearch={this.handleSearch}/>
          <Switch>
            <Route path="/" exact render={() => <Home keyword={this.state.keyword}/>} />
            <Route path="/searchresults" exact render={() => <SearchResult keyword={this.state.keyword} />} />
            <Route path="/writerecipe" component={WriteRecipe} />
            <Route path="/user" exact render={() => <User user_id={this.state.user_id}/>} />
          </Switch>
      </div>
    )
  }
}

export default Layout;