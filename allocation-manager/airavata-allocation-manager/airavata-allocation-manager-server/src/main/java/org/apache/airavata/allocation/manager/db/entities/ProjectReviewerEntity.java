package org.apache.airavata.allocation.manager.db.entities;

import java.io.Serializable;
import javax.persistence.*;


/**
 * The persistent class for the PROJECT_REVIEWER database table.
 * 
 */
@Entity
@Table(name="PROJECT_REVIEWER")
@NamedQuery(name="ProjectReviewerEntity.findAll", query="SELECT p FROM ProjectReviewerEntity p")
public class ProjectReviewerEntity implements Serializable {
	private static final long serialVersionUID = 1L;

	@Id
	@Column(name="ID")
	private int id;

	@Column(name="PROJECT_ID")
	private String projectId;

	@Column(name="REVIEWER")
	private String reviewer;

	public ProjectReviewerEntity() {
	}

	public int getId() {
		return this.id;
	}

	public void setId(int id) {
		this.id = id;
	}

	public String getProjectId() {
		return this.projectId;
	}

	public void setProjectId(String projectId) {
		this.projectId = projectId;
	}

	public String getReviewer() {
		return this.reviewer;
	}

	public void setReviewer(String reviewer) {
		this.reviewer = reviewer;
	}

}