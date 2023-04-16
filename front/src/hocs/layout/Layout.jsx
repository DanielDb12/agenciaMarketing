
import { connect } from 'react-redux'


import React from 'react'

export const Layout = ({ children }) => {
  return (
    <div>{children}</div>
  )
}


const mapStateToTrops = state => ({})

export default connect(mapStateToTrops, {})(Layout)
