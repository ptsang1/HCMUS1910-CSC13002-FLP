import React, { Component } from 'react';
import './App.css';
import data from './data/data.json'
import user_data from './data/users.json'
import shortid from 'shortid';


class User extends Component {
    constructor(props) {
        super(props);
        this.state = {
            user_id: '',
            user: {},
            posts: []
        }
    }

    // componentWillReceiveProps({ user_id }) {
    //     console.log(user_id)
    //     this.setState({
    //         user: user_data.filter(item => item.userid === user_id),
    //         posts: data.filter(item => item.owner_id === user_id)      
    //        })
    //   }

    findUser = () => {
        const params = new URL(window.location.href).searchParams;
        const user_id = params.get('id');
        return user_data.filter(item => item.userid === user_id)[0] 
    }
    findUsersPosts = () => {
        const params = new URL(window.location.href).searchParams;
        const user_id = params.get('id');
       return data.filter(item => item.owner_id === user_id)
    }
    componentWillMount() {
        this.setState(state => ({
            user: this.findUser(),
            posts: this.findUsersPosts()
        }))
    }


    render() {
        
        return (
            <div className="container">
                <div className="content">
                    <div className="contentInfo">
                        <div className="imgContent">
                            <img className="avatar" src={this.state.user.avatarlink} />
                        </div>
                    </div>
                    <div className="info">
                        <h1>{this.state.user.fullname}</h1>
                        <h2>{this.state.posts.length} posts</h2>
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