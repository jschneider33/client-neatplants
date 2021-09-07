import ProductList from "../../components/ProductsList";
import { getCategoyFromSlug, getProductsByCategory, listCategories } from '../../lib/commerce/productAPI';

export async function getStaticProps({ params }) {
  const { slug } = params;
  const category = getCategoyFromSlug(slug);
  const products = getProductsByCategory(slug);
  return {
    props: {
      category,
      products,
    },
  };
};

export async function getStaticPaths() {
    const categories = listCategories();
  
    return {
      paths: categories.map((category) => ({
        params: {
          slug: category.slug,
        },
      })),
      fallback: false,
    };
  }

  export default function CategoryPage({ category, products }) {
    return (
      <>
        <h1>{category.name}</h1>
  
        <ProductList products={products} />
      </>
    );
  }