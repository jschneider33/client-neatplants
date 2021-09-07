import React from "react";
import BC from 'nextjs-breadcrumbs';
// import "../styles/breadcrumbs.css";

const formatTitle = (title, permalink) => {

    let newTitle = title;
    if(title !== permalink){
        newTitle = newTitle + "  >  "
    }
    return newTitle.toUpperCase();
}

const Breadcrumbs = ({ permalink }) => {
    console.log(permalink)
    return (
        <>
            <BC 
                containerClassName="breadcrumbs-container"
                listClassName="breadcrumbs-list"
                inactiveItemClassName="breadcrumbs-item breadcrumbs-item-inactive"
                activeItemClassName="breadcrumbs-item breadcrumbs-item-active"
                replaceCharacterList={[{from: '-', to: ' '}]}
                transformLabel={(title) => formatTitle(title, permalink)}
            />
        </>
    )
}

export default Breadcrumbs;