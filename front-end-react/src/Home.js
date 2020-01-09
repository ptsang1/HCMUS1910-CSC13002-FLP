import React, { Component } from 'react';
import Masonry from 'react-masonry-infinite';
import shortid from 'shortid';
import './App.css';
import data from './data/data.json'

class Popup extends React.Component {
  render() {
    return (
      <div className='popup'>
        <div className='popup_inner'>
          <div className="row">
            <img className="col" src={this.props.img.src}></img>
            <div className="col detail scroll-bar">
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
      isLiked: false,
      i: 0,
      searchResults: [],
      getUser: '',
    };
  }

  generateElements = (i) => data.slice(i * 10, i * 10 + 10).map((item, index) => {
    const newImg = new Image()
    newImg.src = item.img[0]
    return {
      key: shortid.generate(),
      img: newImg,
      username: item.username,
      name: item.name,
      ingredients: item.ingredients,
      steps: item.steps,
      isLiked: false,
      id: item.owner_id
    };
  });

  componentWillMount() {
    this.setState(state => ({
      elements: state.elements.concat(this.generateElements(0))
    }))  }

  componentDidMount() {
    this.setState(state => ({
      searchResults: state.elements
    }))
  }

  componentWillUnmount = () => {
    this.setState({
      elements: []
    })
  }

  loadMore = () => {
    const element = this.generateElements(this.state.i + 1);
    if (element.length > 0) {
      setTimeout(() => {
        this.setState(state => ({
          elements: state.elements.concat(element),
          i: state.i + 1,
        }))
      }, 2500);
    }
    else {
      this.setState({
        hasMore: false
      })
    }
  }


  clickLike = (key) => {
    this.setState({
      dataPopUp: this.state.elements.map(item => item.isLiked = item.key === key ? item.key === key && !item.isLiked : item.isLiked),
    });
  }

  goToPersonalPage = (key) => {
    this.setState({
      getUser: this.state.elements.filter(item => item.key === key)[0].id
    });
    window.location.href=`/user?id=${this.state.elements.filter(item => item.key === key)[0].id}`;
  }


  togglePopup = (key) => {
    this.setState({
      dataPopUp: this.state.elements.filter(item => item.key === key)[0],
      showPopup: !this.state.showPopup
    });
  }

 
  componentWillReceiveProps({ keyword }) {
    this.setState({
      searchResults: keyword === '' ? this.state.elements : this.state.elements.filter(item => this.searchFor(keyword, item) === true)
    })
  }

  render() {
    // console.log(this.state.elements)

    // const searchResults = keyword === '' ? this.state.elements : this.state.elements.filter(item => this.searchFor(keyword, item) === true)

    // const { searchResults } = this.state
    // console.log('searchResults', searchResults)
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
                <div key={item.key} className="post" style={{ height: `${item.img.height / item.img.width * 378.45 + 122}` }}>
                  <h2 onClick={() => this.goToPersonalPage(item.key)} style={{ cursor: "pointer" }}>{item.username}</h2>
                  <img className="post-img" src={item.img.src} alt="" onClick={() => this.togglePopup(item.key)} style={{ cursor: "pointer" }} />
                  <div className="post-body">
                    <ul className="post-react flex flex-wrap align-items-center">
                      <li><i className={item.isLiked ? "fa fa-heart fa-3x" : "fa fa-heart-o fa-3x"} onClick={() => this.clickLike(item.key)} style={{ cursor: "pointer" }}></i></li>
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
