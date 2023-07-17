import { Link, Routes, useParams } from "react-router-dom"
import Posts from "./Posts"
import { useState } from "react"







const PostDetail = ({data,index}) => {

  const {slug} = useParams()


  const [dt,setDt] = useState(data)


  return(


<div className="container w-full md:max-w-3xl mx-auto pt-20">
  <div className="w-full px-4 md:px-6 text-xl text-gray-800 leading-normal" >
<div className="font-sans">


  <h1 className="font-bold font-sans break-normal text-gray-900 pt-6 pb-2 text-3xl md:text-4xl" >{data.title}</h1>
						<p className="text-sm md:text-base font-normal text-gray-600">Published 19 February 2019</p>

</div>
</div>
</div>







  )
}

export default PostDetail
