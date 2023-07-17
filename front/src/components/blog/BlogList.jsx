import { CheckCircleIcon, ChevronRightIcon, EnvelopeIcon } from "@heroicons/react/20/solid"
import SmallSetPagination from "@components/pagination/SmallSetPagination"
import BlogCardHorizontal from "./BlogCardHorizontal"

function BlogList({posts,get_blog_list_page,count}){

    return(
    <div className="overflow-hidden px-8 bg-white">
      
        {posts&&posts.map((post,index) => (
          <BlogCardHorizontal data={post} key={index} index={index}/>
        ))}
      
      <SmallSetPagination list_page={get_blog_list_page} list={posts} count={count} />
    </div>
    )
}
export default BlogList
