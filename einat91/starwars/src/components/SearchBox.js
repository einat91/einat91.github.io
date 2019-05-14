import React from 'react';

const SearchBox = ({ searchChange }) => {
    return (
        <div className='pa2'>
            <input
                className='tc pa3 ba b--gren bg-lightest-blue'
                type='search'
                placeholder='Robot Searching'
                onChange={searchChange}
            />
        </div>
    );
}

export default SearchBox;