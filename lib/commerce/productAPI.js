import { commerce } from './commerce';

export async function listProducts(){
    const { data: products } = await commerce.products.list();
    return products;
}

export async function listCategories(){
    const { data: categories } = await commerce.categories.list();
    return categories;
}

export async function getFeaturedProducts(){
    const { data: products } = await commerce.products.list({
        category_slug: ["featured"],
      });
      return products;
}

export async function getProductsByCategory(category_slug){
    const { data: products } = await commerce.products.list({
        category_slug: [category_slug],
      });
      return products;
}

export async function getCategoryFromSlug(slug){
    const category = await commerce.categories.retrieve(slug, {
        type: "slug",
      });
      return category;
}

export async function getCategoryFromID(category_id){
    const category = await commerce.categories.retrieve(category_id, {
        type: "id",
    });
    return category;
}

export async function getProductByPermalink(permalink){
    const product = await commerce.products.retrieve(permalink, {
        type: 'permalink'
    });
    return product;
}

