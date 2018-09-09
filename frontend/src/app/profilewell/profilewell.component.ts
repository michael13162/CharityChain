import { Component, ChangeDetectionStrategy, Input, Output, EventEmitter } from '@angular/core';

@Component({
  selector: 'profile-well-component',
  templateUrl: './profilewell.component.html',
  styleUrls: ['./profilewell.component.css'],
  changeDetection: ChangeDetectionStrategy.OnPush
})
export class ProfileWellComponent {
  @Input() jsonProfile: any;
  @Input() overlay: boolean;
  @Output() overlayClosed: EventEmitter<void> = new EventEmitter<void>();
  @Output() donateClicked: EventEmitter<void> = new EventEmitter<void>();

  constructor() {}

  getOrganizationName(): string {
    if (this.jsonProfile) {
      return this.jsonProfile.charity_info.referenceOrganization.charityName;
    }
  }

  getOrganizationUrl(): string {
    if (this.jsonProfile) {
      return this.jsonProfile.charity_info.referenceOrganization.charityNavigatorURL;
    }
  }

  getRatingImage(): string {
    if (this.jsonProfile) {
      return this.jsonProfile.charity_info.ratingImage.large;
    }
  }

  getMissionStatement(): string {
    if (this.jsonProfile) {
      return this.jsonProfile.mission_statement;
    }
  }

  getAdministrationExpenseRatio(): string {
    if (this.jsonProfile) {
      return this.jsonProfile.charity_info.financialRating.performanceMetrics.administrationExpensesRatio;
    }
  }

  getFundraisingEfficiency(): string {
    if (this.jsonProfile) {
      return this.jsonProfile.charity_info.financialRating.performanceMetrics.fundraisingEfficiency;
    }
  }

  getLiabilitiesToAssetsRatio(): string {
    if (this.jsonProfile) {
      return this.jsonProfile.charity_info.financialRating.performanceMetrics.liabilitiesToAssetsRatio;
    }
  }

  getProgramExpensesGrowth(): string {
    if (this.jsonProfile) {
      return this.jsonProfile.charity_info.financialRating.performanceMetrics.programExpensesGrowth;
    }
  }

  getProgramExpensesRatio(): string {
    if (this.jsonProfile) {
      return this.jsonProfile.charity_info.financialRating.performanceMetrics.programExpensesRatio;
    }
  }

  getWorkingCapitalRatio(): string {
    if (this.jsonProfile) {
      return this.jsonProfile.charity_info.financialRating.performanceMetrics.workingCapitalRatio;
    }
  }

  auditedFinancialStatus(): boolean {
    if (this.jsonProfile) {
      return this.jsonProfile.charity_info.accountabilityRating.accountabilityTests.auditedFinancialStatus == "Pass";
    }
  }

  boardListStatus(): boolean {
    if (this.jsonProfile) {
      return this.jsonProfile.charity_info.accountabilityRating.accountabilityTests.boardListStatus == "Pass";
    }
  }

  boardMeetingMinutes(): boolean {
    if (this.jsonProfile) {
      return this.jsonProfile.charity_info.accountabilityRating.accountabilityTests.boardMeetingMinutes == "Pass";
    }
  }

  ceoCompensationProcedure(): boolean {
    if (this.jsonProfile) {
      return this.jsonProfile.charity_info.accountabilityRating.accountabilityTests.ceoCompensationProcedure == "Pass";
    }
  }

  compensatesBoard(): boolean {
    if (this.jsonProfile) {
      return this.jsonProfile.charity_info.accountabilityRating.accountabilityTests.compensatesBoard == "Pass";
    }
  }

  form990Status(): boolean {
    if (this.jsonProfile) {
      return this.jsonProfile.charity_info.accountabilityRating.accountabilityTests.form990Status == "Pass";
    }
  }

  independentAudit(): boolean {
    if (this.jsonProfile) {
      return this.jsonProfile.charity_info.accountabilityRating.accountabilityTests.independentAudit == "Pass";
    }
  }

  privacyStatus(): boolean {
    if (this.jsonProfile) {
      return this.jsonProfile.charity_info.accountabilityRating.accountabilityTests.privacyStatus == "Pass";
    }
  }

  reportsCEOAndSalary(): boolean {
    if (this.jsonProfile) {
      return this.jsonProfile.charity_info.accountabilityRating.accountabilityTests.reportsCEOAndSalary == "Pass";
    }
  }

  getBalance(): number {
    if (this.jsonProfile) {
      return this.jsonProfile.balance;
    }
  }
}
