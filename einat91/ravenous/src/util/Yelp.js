
const apiKey = 'TxeveKMsCP7bYixVUXuMZN499D_B5QwwHq9Xxs5qlQV0XRztFLhit-yKQpZezFOWNTiobzru75as1JyewDCQTNZhUw7db_n7fljk-iCrKnpvKRovetCRkiH6UUYZXXYx';
const fetchAddress = `https://cors-anywhere.herokuapp.com/https://api.yelp.com/v3/businesses/search`;

const Yelp = {
    search(term, location, sortBy) {
        return fetch(`${fetchAddress}?term=${term}&location=${location}&sort_by=${sortBy}`, {
            headers: {
                Authorization: `Bearer ${apiKey}`
            }
        }).catch(response => {
            if (response.status === 400) {
                throw new Error('Error! Valid input is required');
                // return fetch(`${fetchAddress}?term=${term}&location=${location}&sort_by=${sortBy}`, {
                //   headers: {
                //     Authorization: `Bearer ${apiKey}`
                //}
                //})
            }
        })
            .then(response => {
                return response.json();
            }).then(jsonResponse => {
                if (jsonResponse) {
                    if (jsonResponse.businesses) {
                        return jsonResponse.businesses.map(business => ({
                            id: business.id,
                            imageSrc: business.image_url,
                            name: business.name,
                            address: business.location.address1,
                            city: business.location.city,
                            state: business.location.state,
                            zipCode: business.location.zip_code,
                            category: business.categories[0].title,
                            rating: business.rating,
                            reviewCount: business.review_count,

                        }));
                    }
                }
            })

    }
}

export default Yelp;