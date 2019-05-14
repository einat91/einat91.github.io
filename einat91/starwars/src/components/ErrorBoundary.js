import React, { Component } from 'react';

class ErrorBoundary extends Component {
    constructor(props) {
        super(props);
        this.state = {
            hasError: false
        };
    }
    componentDidCatch(error, info) {
        this.setState({ hasError: true });
    }
    render() {
        if (this.state.hasError) {
            return <h1> Ooops. Something went wrong...</h1>;
        }
        return this.props.children;  //anything between the error boundries  
    }
}

export default ErrorBoundary;