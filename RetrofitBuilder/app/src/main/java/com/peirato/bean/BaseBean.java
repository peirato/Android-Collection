package com.peirato.bean;

public class BaseBean {

	private String errmsg;
	
	private Integer recode;

	public String getErrmsg() {
		return errmsg;
	}

	public void setErrmsg(String errmsg) {
		this.errmsg = errmsg;
	}

	public Integer getRecode() {
		return recode;
	}

	public void setRecode(Integer recode) {
		this.recode = recode;
	}

	@Override
	public String toString() {
		return "BaseBean [errmsg=" + errmsg + ", recode=" + recode + "]";
	}
	
}
