import React, { Component } from 'react';
import './App.css';
import data from './data/data.json'
import user_data from './data/users.json'
import shortid from 'shortid';


class User extends Component {
    constructor(props) {
        super(props);
        this.state = {
          user: {},
          posts: []
        }
    }
    findUser = () => user_data.filter(item => item.userid === '8cebdae8-320f-11ea-8830-02557972d8a6')
    findUsersPosts = () => data.filter(item => item.owner_id === '8cebdae8-320f-11ea-8830-02557972d8a6')
    componentWillMount() {
        this.setState(state => ({
          user: this.findUser(),
          posts: this.findUsersPosts()
        })) 
    }


    render() {
        console.log(this.state.posts)
        return (
            <div className="container">
                <div className="content">
                    <div className="contentInfo">
                        <div className="imgContent">
                            <img className="avatar" src={this.state.user[0].avatarlink} />
                        </div>
                        <div>
                            <h1>{this.state.user[0].fullname}</h1>
                            <h2>{this.state.posts.length} posts</h2>
                        </div>
                    </div>
                    <div className="user_posts">{
                        
              this.state.posts.map(item => (
                <div key={item.key}>
                  <img className="post-img" src={item.img[0]} alt="" style={{ cursor: "pointer" }} />
                </div>
              ))
            }</div>
                    {/* <div className="col-sm-4 col-md-3 tab">
                        <ul id="myTab" className="nav nav-tabs nav-top-border mt-80" role="tablist">
                            <li className="nav-item"><a className="nav-link active" href="#description" data-toggle="tab">Bài đăng</a></li>
                            <li className="nav-item"><a className="nav-link" href="#specs" data-toggle="tab">Yêu thích</a></li>
                        </ul>
                        <div className="tab-content pt-20">
                            <div role="tabpanel" className="tab-pane active" id="description">
                                <div className="imgPostContent">
                                    <img className="imgPost" src="img.jpg" />
                                    <img className="imgPost" src="img.jpg" />
                                </div>
                                <div className="imgPostContent">
                                    <img className="imgPost" src="img.jpg" />
                                    <img className="imgPost" src="img.jpg" />
                                </div>
                                <div className="imgPostContent">
                                    <img className="imgPost" src="img.jpg" />
                                    <img className="imgPost" src="img.jpg" />
                                </div>
                                <div className="imgPostContent">
                                    <img className="imgPost" src="img.jpg" />
                                </div>
                            </div>

                            <div role="tabpanel" className="tab-pane fade" id="specs">
                                <div className="table-responsive">

                                </div>
                            </div>
                        </div>
                    </div> */}
                </div>
            </div>
        )
    }
}

export default User;