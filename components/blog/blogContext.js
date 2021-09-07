import React, { useState, useEffect, useContext } from 'react';

export const BlogContext = React.createContext({});

export const BlogProvider = ({children}) => {
    const [articles, setArticles] = useState({});

    const data = { articles, setArticles }

    useEffect(() => console.log("BlogContext value: ", articles));

    return(
        <BlogContext.Provider blog={data}>
            {children}
        </BlogContext.Provider>
    )
}

export const withBlog = WrappedComponent => props => {
    const blogContext = useContext(BlogContext)
    return(
        <WrappedComponent 
            {...props}
            articles={blogContext.articles}
            setArticles={blogContext.setArticles}
        />
    )
}