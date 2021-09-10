// import markdownStyles from './markdown-styles.module.css'
import styles from '../../styles/Posts.module.sass';

export default function PostBody({ content }) {
  return (
    <div className={styles.postBody}>
      <div
        className={styles.postContent}
        dangerouslySetInnerHTML={{ __html: content }}
      />
    </div>
  )
};