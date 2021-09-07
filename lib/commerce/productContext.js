// import React, { useState, useEffect, useContext } from "react";

// export const ProductContext = React.createContext({});

// export const ProductProvider = ({ children }) => {
//     const [featuredProducts, setFeaturedProducts] = useState([])
//     const [products, setProducts] = useState({
//         one: "false",
//         two: "false",
//     });
//     const data = { products, setProducts };

//     const fetchFeaturedProducts = () => {
        
//     }

//     useEffect(() => console.log("ProductContext value: ", products));

//     return (
//         <ProductContext.Provider value={data}>
//             {children}
//         </ProductContext.Provider>
//     )
// };

// // export function useProductContext() {
// //     return useContext(ProviderContext)
// // }

// export const withProducts = WrappedComponent => props => {
//     const productContext = useContext(ProductContext);
//     // console.log("withProducts")
//     // console.log(productContext)
//     return(
//         <WrappedComponent
//             {...props}
//             products={productContext}
//         />
//     )
// }

