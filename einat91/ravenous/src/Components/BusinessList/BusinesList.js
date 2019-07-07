import React from 'react';
import './BusinessList.css';

import Business from '../Business/Business';

class BusinessList extends React.Component {
    check() {
        if (!this.props) {
            return <h1> Oops! Something went wrong</h1>
        }
    }

    render() {
        return (
            <div className="BusinessList">
                {
                    //this.check() && 
                    this.props.businesses.map(business => {
                        return <Business business={business} key={business.id} />
                    })
                }
            </div>
        );
    }
}

export default BusinessList;