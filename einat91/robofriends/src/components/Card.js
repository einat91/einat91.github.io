import React from 'react';

const Card = ({ id, name, email }) => {
    return (
        <div className='tc bg-light-green dib br3 pa2 ma2 grow bw2 shadow-5'>
            <img alt='robot' src={`https://robohash.org/${id}?100x100`} />
            <div>
                <h2> {name}</h2>
                <p> {email}</p>
            </div>
        </div>
    );
}
export default Card;