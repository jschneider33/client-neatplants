import { useRouter } from 'next/router'
import ErrorPage from 'next/error'
import PostBody from '../../components/blog/PostBody'
import PostHeader from '../../components/blog/PostHeader'
import PostContainer from '../../components/containers/PostContainer';
import { getPostBySlug, getAllPosts } from '../../lib/blog/blogAPI'
import PostTitle from '../../components/blog/PostTitle'
import Head from 'next/head'
import markdownToHtml from '../../lib/blog/markdownToHtml.js'

export default function Post({ post, morePosts, preview, content }) {
  const router = useRouter()

  if (!router.isFallback && !post?.slug) {
    return <ErrorPage statusCode={404} />
  }
  return (
      <PostContainer>
        {router.isFallback ? (
          <PostTitle>Loading…</PostTitle>
        ) : (
          <>
            <article className="mb-32">
              <Head>
                <title>
                  {post.title} | Neat Houseplants Blog
                </title>
                <meta property="og:image" content={post.ogImage.url} />
              </Head>
              <PostHeader
                title={post.title}
                coverImage={post.coverImage}
                datetime={post.datetime}
              />
              <PostBody content={post.content} />
            </article>
          </>
        )}
      </PostContainer>
  )
}

export async function getStaticProps({ params }) {
  const post = getPostBySlug(params.slug, [
    'title',
    'datetime',
    'slug',
    'content',
    'ogImage',
    'coverImage',
    'content'
  ]);

  const content = await markdownToHtml(post.content || '');

  return {
    props: {
      post: {
        ...post,
        // post
        content,
      },
    },
  };
};

export async function getStaticPaths() {
  const posts = getAllPosts(['slug']);

  return {
    paths: posts.map((post) => {
      return {
        params: {
          slug: post.slug,
        },
      }
    }),
    fallback: false,
  };
};