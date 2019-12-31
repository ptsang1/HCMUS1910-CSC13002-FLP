import React, { Component } from 'react';
import './Log.css';
import { render } from 'react-dom';

class LogIn extends Component {
    constructor(props) {
        super(props);
        this.state = {

        };
    }


    render() {
        return (
            <div className="container_login">
                <div className="signin-content">
                    <div className="signin-image">
                        <img src={require("./img/login.jpg")} alt="sign up image" />
                        <p className="signup-question">Bạn chưa có tài khoản?</p>
                        <a href="/signup" className="signup-image-link">Đăng kí tài khoản mới</a>
                        <a href="/" className="signup-image-link">Tiếp tục sử dụng ẩn danh</a>
                    </div>

                    <div className="signin-form">
                        <h2 className="form-title">Đăng Nhập</h2>
                        <form method="POST" className="register-form" id="login-form">
                            <div className="form-group">
                                <label for="your_name"><i className="fa fa-user"></i></label>
                                <input className="login" type="text" name="your_name" id="your_name" placeholder="Tài khoản" />
                            </div>
                            <div className="form-group">
                                <label for="your_pass"><i className="fa fa-lock"></i></label>
                                <span className="btn-show-pass">
                                    <i className="fa fa-eye"></i>
                                </span>
                                <input className="login" type="password" name="your_pass" id="your_pass" placeholder="Mật khẩu" />
                            </div>
                            <div className="form-group">
                                <input className="login" type="checkbox" name="remember-me" id="remember-me" className="agree-term" />
                                <label for="remember-me" className="label-agree-term"><span><span></span></span>Ghi nhớ đăng nhập</label>
                            </div>
                            <div className="form-btn form-group">
                                <input className="login" type="submit" name="signin" id="signin" className="form-submit btn" value="Đăng nhập" />
                            </div>
                        </form>
                        <div className="social-login">
                            <span className="social-label">Đăng nhập với</span>
                            <ul className="socials">
                                <li><a href="#"><i className="display-flex-center fa fa-facebook"></i></a></li>
                                <li><a href="#"><i className="display-flex-center fa fa-twitter"></i></a></li>
                                <li><a href="#"><i className="display-flex-center fa fa-google"></i></a></li>
                            </ul>
                        </div>
                    </div>
                </div>
            </div>
        )
    }
}

export default LogIn;