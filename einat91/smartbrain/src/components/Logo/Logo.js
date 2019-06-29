import React from 'react';
import Tilt from 'react-tilt'
import brain from './brain.png';
import './Logo.css';

const Logo = () => {
    return (
        <div className='ma4 nt0 center'>
            <Tilt className="Tilt br4 bo shadow-2 b--black center " options={{ max: 55 }} style={{ height: 120, width: 120 }} >
                <div className="Tilt-inner pa3 center"> <img style={{ paddingTop: '5px' }} alt='logo' src={brain}></img> </div>
            </Tilt>

        </div>

    )
}

export default Logo;