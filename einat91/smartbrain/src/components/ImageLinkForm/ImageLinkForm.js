import React from 'react'
import './ImageLinkForm.css'

const ImageLinkForm = ({ onInputChange, onButtonSumbit }) => {
    return (
        <div>
            <p className='center f4'>
                {'Face Recognition App'}
            </p>
            <p className='f5'>
                {'How does it work? simply copy and paste here a link to your favorite online photo. Try it!'}
             </p>
             <p className ='f6 bold'>  
                {'Please copy the actual link of the photo and not the website'}
            </p>
            <div className='center'>
                <div className='form center pa4 br3 shadow-5'>
                    <input className='f5 pa2 w-80 center' type='tex' onChange={onInputChange} />
                    <button
                        className='w-20 grow f5 link ph3 pv dib black'
                        onClick={onButtonSumbit}
                    > Detect</button>
                </div>
            </div>

        </div>
    )
}
export default ImageLinkForm;