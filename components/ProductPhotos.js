import React from "react";

import Image from "next/image"
import ImageGallery from "react-image-gallery";

import styles from "../styles/Product.module.sass";

const ProductPhotos = ({ photos, startIndex }) => {
    // console.log(photos)

    let images = [];
    photos.map(photo => {
        images.push({
            original: photo,
            thumbnail: photo,
            originalClass: styles.original,
            thumbnailClass: styles.thumbnail,
        })
    })

    // console.log(images)

    return(
        <>
            {/* <Image 
                width={500}
                height={500}
                src="https://picsum.photos/id/1018/1000/600/"
                alt=""
            /> */}
            <ImageGallery 
                items={images} 
                showFullscreenButton={false}
                showPlayButton={false}
                startIndex={startIndex}
            />
        </>
    )
}

export default ProductPhotos;