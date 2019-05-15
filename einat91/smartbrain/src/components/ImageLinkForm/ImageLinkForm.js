import React from 'react'
import './ImageLinkForm.css'

const ImageLinkForm = ({ onInputChange, onButtonSumbit }) => {
    return (
        <div>
            <p className='f4'>
                {'This Magic Brain will detect faces in your pictures. Give it a try'}
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