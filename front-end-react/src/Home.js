import React, { Component } from 'react';
import Masonry from 'react-masonry-infinite';
import shortid from 'shortid';
import './App.css';
import data from './data/data.json'

class Popup extends React.Component {
  render() {
    return (
      <div className='popup' >
        <div className='popup_inner' >
          <div className="row">
            <img className="col" src={this.props.img.src}></img>
            <div className="col detail">
              <div className="closeBtn" onClick={this.props.closePopup}><i className="fa fa-times fa-3x"></i></div>
              <h1>{this.props.name}</h1>
              <h2>viết bởi: {this.props.username}</h2>
              <div>
                <p className="title">Nguyên liệu:</p>
                <ul className="content">
                  {this.props.ingredients.map((item, index) => <li key={index}>{item}</li>)}
                </ul>
              </div>
              <div>
                <p className="title">Các bước:</p>
                <ul className="content">
                  {this.props.steps.map((item, index) => <li key={index}>{item}</li>)}
                </ul>
              </div>
            </div>
          </div>
        </div>
      </div>
    );
  }
}

class Home extends Component {
  constructor(props) {
    super(props);
    this.state = {
      hasMore: true,
      elements: [],
      load: true,
      showPopUp: false,
      dataPopUp: {},
    };
  }

  generateElements = () => [...Array(10).keys()].map((item, index) => {
    const newImg = new Image()
    newImg.onload = () => {
    }
    const imgs = data.map(item => item.img)
    console.log(data[index])
    newImg.src = imgs[index][0]
    return {
      key: shortid.generate(),
      img: newImg,
      username: data[index].username,
      name: data[index].name,
      ingredients: data[index].ingredients,
      steps: data[index].steps,
    };
  });

  componentWillMount() {
    this.setState(state => ({
      elements: state.elements.concat(this.generateElements())
    }))
  }

  componentWillUnmount = () => {
    this.setState({
      elements: []
    })
  }

  loadMore = () => setTimeout(() => this.setState(state => ({
    elements: state.elements.concat(this.generateElements()),
  })), 2500);

  clickLike = () => {

  }

  togglePopup = (key) => {
    console.log(this.state.elements.filter(item => item.key === key)[0])
    this.setState({
      dataPopUp: this.state.elements.filter(item => item.key === key)[0],
      showPopup: !this.state.showPopup
    });
  }

  render() {
    console.log(this.state.elements)
    return (
      <div>
        <div className="container">
          {this.state.elements ? (<Masonry
            className="masonry"
            hasMore={this.state.hasMore}
            loader={
              <div className="sk-folding-cube">
                <div className="sk-cube1 sk-cube" />
                <div className="sk-cube2 sk-cube" />
                <div className="sk-cube4 sk-cube" />
                <div className="sk-cube3 sk-cube" />
              </div>
            }
            loadMore={this.loadMore}
          >
            {
              this.state.elements.map(item => (
                <div key={item.key} className="post" style={{ height: `${item.img.height / item.img.width * 456.14 + 122}` }}>
                  <h2>{item.username}</h2>
                  <img className="post-img" src={item.img.src} alt="" onClick={() => this.togglePopup(item.key)} style={{ cursor: "pointer" }} />
                  <div className="post-body">
                    <ul className="post-react flex flex-wrap align-items-center">
                      <li><i className="fa fa-heart-o fa-3x" onClick={this.clickLike}></i></li>
                      <li><i className="fa fa-comments-o fa-3x"></i></li>
                      <li><i className="fa fa-share-alt fa-3x"></i></li>
                    </ul>
                    <h1 className="post-content">{item.name}</h1>
                  </div>
                </div>
              ))
            }

          </Masonry>) : null}
        </div>
            {this.state.showPopup ?
              <Popup
                img={this.state.dataPopUp.img}
                name={this.state.dataPopUp.name}
                ingredients={this.state.dataPopUp.ingredients}
                steps={this.state.dataPopUp.steps}
                username={this.state.dataPopUp.username}
                closePopup={this.togglePopup.bind(this)}
              />
              : null
            }
      </div>
    );
  }
}

export default Home;