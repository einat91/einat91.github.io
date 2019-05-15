import React from 'react';
import './Navigation.css';

const Navigation = ({ onRouteChange, isSignedIn }) => {
    if (isSignedIn) {
        return (
            <nav style={{ display: 'flex', justifyContent: 'flex-end' }}>
                <p className='Title grow fa-italic'>  Smart Brain </p>
                <p onClick={() => onRouteChange('signout')} className='f4 link din white fa-italic pa3 pointer underline-hover'> Sign Out </p>
            </nav>
        );
    } else {
        return (
            <nav style={{ display: 'flex', justifyContent: 'flex-end' }}>
              <p className='f4 link din grow black fa-italic pa3'>  Smart Brain </p>
                <p onClick={() => onRouteChange('signin')} className='f4 link din white fa-italic pa3 pointer underline-hover'> Sign In </p>
                <p onClick={() => onRouteChange('register')} className='f4 link din white fa-italic pa3 pointer underline-hover'> Register </p>
            </nav>
        );
    }
}

export default Navigation;
