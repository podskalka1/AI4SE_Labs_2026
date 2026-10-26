# Software Requirements Specification

This document consolidates software requirements from the supplied corpus. Source locations refer to normalized extracted text, including normalized email bodies.

## Document overview

- Input corpus: C:\\Users\\luk20\\swai\\AI4SE\_Labs\_2026\\Week\_04\_Requirements\\Task\_1\\data\\corpus
- Source documents: 20
- Retained requirements: 497
- Discarded requirements: 14 (16 candidates)
- Review completion status: incomplete_review
- Latest review: needs_revision
- Revision passes: 3 / 3

## Priority scale

P1 Critical: essential for core operation, safety, security or mandatory<br>compliance\. P2 High: important functionality with substantial impact\. P3 Medium:<br>useful functionality not essential for basic operation\. P4 Low: optional<br>enhancements or convenience features\.

## Requirements

### REQ-001 — Staff Accounts Report Including Last Password Change Date

- Internal key: REQ-001d6b93e9041d3c5c1eba57986561225d75713aa85317ddc4777fb4413e1451
- Type: functional
- Priority: P2
- Priority basis: inferred
- Priority rationale: Password-change reporting supports administrative and security oversight, but no explicit priority is supplied\.
- Originating candidates: CAND-4ce1ed994be79d34ee7dff03169a107ac39133bc29b8f1694d0b754166f98354

The system shall provide a Staff Accounts report that includes the date of each staff account's last password change\.

Sources and evidence:

Source: [evergreen\_reference\_2009\.txt](<../data/corpus/evergreen_reference_2009.txt>); document ID: DOC-e6aa9f8c6308ab748459f87b578a0df9df9c865b7911bac3686e865963b7af6f; normalized lines 159–159.

> - Staff Accounts with date of last password change \(not available\)

### REQ-002 — Migrate Development and Training Configurations to Production

- Internal key: REQ-003021ae0a370d08050a95049f055465836ea7c94b3a2da32cdb59f2777222b2
- Type: nonfunctional
- Priority: P3
- Priority basis: explicitly specified
- Priority rationale: The supplied review identifies this as Medium Priority, which maps to P3; the priority is explicit in the review evidence\.
- Originating candidates: CAND-7ea2b48e4d5d6940db1111a179137bca63403d398de04459260cfacba9c2b393

The Management Processes shall provide development and training environments with the ability to migrate configurations to a production environment\.

Sources and evidence:

Source: [meeting\_minutes/meeting\_2009-07-20\_minutes\.txt](<../data/corpus/meeting_minutes/meeting_2009-07-20_minutes.txt>); document ID: DOC-5ab1dd8bc97af3b1ab2e378495f0e0d75fd501fcc19f923c0d8fda831074281b; normalized lines 114–118.

> CO-3: Management Processes shall provide a development and training environment
>       with the ability to migrate configurations to a production environment\.
>       \[Discussion: Katherine noted that Evergreen development follows this
>       pattern - developers have separate environments\. We need to make sure
>       report templates and configurations can be exported/imported\.\]

### REQ-003 — Transaction Reports by Organizational Scope

- Internal key: REQ-006b3492a2b761f611cbbcaa4ccfd246d7d09ec292a7e4fc3f03c091d3e92ea8
- Type: functional
- Priority: P2
- Priority basis: inferred
- Priority rationale: These transaction views support operational and management analysis, but no explicit priority is supplied\.
- Originating candidates: CAND-504307a404fa2b2858176138734414b4308de790d09ae77111b198a21648f85e

The system shall provide transaction reports showing holds placed, holds filled, and check-outs per patron, per library, per group of libraries, per system, and per county\.

Sources and evidence:

Source: [survey\_results\_2009\.txt](<../data/corpus/survey_results_2009.txt>); document ID: DOC-aac7bceef7a883652805583e98ec513b6ae2e7951e2ecfa18722127b1f12a5c4; normalized lines 124–126.

> 6\. Transactions report can show holds placed, holds filled, and check-outs per
>    patron, per library, per group of libraries, per system, per county\.
> 

### REQ-004 — Missing and Damaged Items Reports by Branch

- Internal key: REQ-00c33705380271f9f097fd43192a91fa776eeae0826e3a32f0134c438da149b5
- Type: functional
- Priority: P2
- Priority basis: inferred
- Priority rationale: The reports support inventory audits and collection management, but the sources do not assign a formal priority level\.
- Originating candidates: CAND-01d145faf148363b6616aa760e85d5e43147daa16ea7a43f9d758cd1dae8d514

The system shall provide reports of missing and damaged items for each branch\.

Sources and evidence:

Source: [conversations/conv\_pines019\_020\_missing\_intransit\.eml](<../data/corpus/conversations/conv_pines019_020_missing_intransit.eml>); document ID: DOC-b233b12122cae48b5821d685f6dc058d2d2e3cc8d7f77622fa4e7e55bddc5399; normalized lines 1–3.

> Every month I do a shelf reading and mark items as missing or damaged\.
> Right now I have no easy way to generate a report of all these items per
> branch\. I need this for my inventory audit and for collection management\.

Source: [conversations/conv\_pines019\_020\_missing\_intransit\.eml](<../data/corpus/conversations/conv_pines019_020_missing_intransit.eml>); document ID: DOC-b233b12122cae48b5821d685f6dc058d2d2e3cc8d7f77622fa4e7e55bddc5399; normalized lines 107–109.

> 1\. Missing and Damaged Items Report:
>    "System provides reports of missing and damaged items per branch\."
> 

### REQ-005 — Missing and Damaged Items by Branch Report

- Internal key: REQ-00c33705380271f9f097fd43192a91fa776eeae0826e3a32f0134c438da149b5-new
- Type: functional
- Priority: P2
- Priority basis: inferred
- Priority rationale: The report supports ongoing collection health monitoring and identification of operational patterns; no explicit source priority is provided\.
- Originating candidates: CAND-e7f4a40694e4f1b530955d4fd215c15b1c8c4b6a5cf7acfd5488db48de8f91a4

The system shall provide a report listing missing and damaged items per branch to support collection health monitoring and pattern identification\.

Sources and evidence:

Source: [interview\_cataloging\_2009-05-08\.txt](<../data/corpus/interview_cataloging_2009-05-08.txt>); document ID: DOC-a79fab45108210e6bce7d92153dfcf055f2ef6b2cdab49a3f6f5717a3e35f29f; normalized lines 59–62.

> THOMAS: We do monthly shelf reading and mark items as missing\. I need a report
> that shows all missing and damaged items per branch\. This helps me track
> collection health and identify patterns - if the same shelf always has missing
> items, we might need to relocate it\.

### REQ-006 — Explicit Presentation of Missing Optional Patron Data

- Internal key: REQ-00cfcd9e274e2beda7b8976f75522b15b9a2e83bbf449b3ca21610dfaf0505e6
- Type: nonfunctional
- Priority: P2
- Priority basis: inferred
- Priority rationale: Explicit treatment of missing data is important for accurate reporting; the source does not assign a priority\.
- Originating candidates: CAND-e7210799b1cf38e6327adf462f30c04ca8bc18be4eeb8e6bef7befe58066c67c

The system shall account for missing optional patron fields in reports and shall present missing values explicitly rather than silently excluding affected records\.

Sources and evidence:

Source: [conversations/conv\_pines023\_patron\_characteristics\.eml](<../data/corpus/conversations/conv_pines023_patron_characteristics.eml>); document ID: DOC-d2b26a6e7678ca4e82bfa7bb06566f329dea692ea22e8987b516fa8bc98c544b; normalized lines 72–76.

> I think we should also consider what data is available\. Some of these
> fields might not be consistently populated\. For example, not all patrons
> provide their zip code or county\.
> 
> Should the report show nulls for missing data, or exclude those records?

Source: [conversations/conv\_pines023\_patron\_characteristics\.eml](<../data/corpus/conversations/conv_pines023_patron_characteristics.eml>); document ID: DOC-d2b26a6e7678ca4e82bfa7bb06566f329dea692ea22e8987b516fa8bc98c544b; normalized lines 95–98.

> One consideration: if patrons haven't provided optional fields, they'll
> show up as null\. We should include them in the report \(with null values\)
> rather than excluding them, because excluding data silently can lead to
> misleading results\.

### REQ-007 — Last Copy Reporting and Volume/Copy Deletion Cleanup

- Internal key: REQ-012944e973cc481c9f218b200036126c08c5d6d52b1f23770d88491598165415
- Type: functional
- Priority: P1
- Priority basis: inferred
- Priority rationale: The candidate includes last-copy protection against accidental deletion of the only consortium copy and effective catalog cleanup operations; the source does not assign a separate priority to the cleanup behavior\.
- Originating candidates: CAND-c532dd68f6aa5bf872b59a635d7c50d39d4129ad78ab912efddd1ef17e47a9fd

The system shall provide a last copy report that singles out a library system's last copies and shall provide a quick, effective method for deleting volume entries together with their copy entries and for deleting records with no items attached\.

Sources and evidence:

Source: [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>); document ID: DOC-091180de9b2d4ea83267d989411ac89f415d4def3bbf7cd51651fb7fda8d8bf9; normalized lines 383–387.

> status to another\. The system should provide a last copy report that singles
> out a library system's last copies, to assist catalogers who need to edit
> WorldCat entries\. The system should provide a quick effective method of
> deleting volume entries along with copy entries, as well as records with no
> items attached\.

### REQ-008 — Patron and Material Use Statistics

- Internal key: REQ-0132b810f72302c145e0b929e6f52a3ef093e4029eaf69f01e1b30883ba61f22
- Type: functional
- Priority: P2
- Priority basis: inferred
- Priority rationale: Inferred as important strategic and operational analysis functionality; no explicit source priority is supplied\.
- Originating candidates: CAND-7027a266c65f9ec37a9dbed0d91aa886cf0a99ad45d6da59fd2cc973c20de579

The system shall produce statistics that support understanding and prediction of patron behavior and use of materials\.

Sources and evidence:

Source: [survey\_results\_2009\.txt](<../data/corpus/survey_results_2009.txt>); document ID: DOC-aac7bceef7a883652805583e98ec513b6ae2e7951e2ecfa18722127b1f12a5c4; normalized lines 130–131.

> 8\. System produces statistics to understand/predict patron behavior and use
>    of materials\.

### REQ-009 — Deletion Audit Fields

- Internal key: REQ-0134f0fed99c1e9a521fb285371cdadf320cd08885cbdb7d9144cb77f5aae13e
- Type: functional
- Priority: P1
- Priority basis: inferred
- Priority rationale: Deletion tracking supports accountability and safe operation of record management, but no explicit priority is supplied\.
- Originating candidates: CAND-5f14ff99a1c539854a4c289c2e134f09fe3d2988ed15430743e7626683f13ad7

The system shall record, for each deletion, the record type, timestamp, user who performed the deletion, and location of the user\.

Sources and evidence:

Source: [conversations/conv\_pines022\_deletions\.eml](<../data/corpus/conversations/conv_pines022_deletions.eml>); document ID: DOC-7b8da7c05931fc99bc80d4a4bb0c8563e690e0c415b57f5ca1ae394462dc26c8; normalized lines 104–110.

> The system should count and track record deletions \(e\.g\., item records,
> patron records\) per location and per system\. Tracking should include:
> - Record type
> - Timestamp
> - User who performed the deletion
> - Location of the user
> 

### REQ-010 — Repeated and scheduled saved query execution

- Internal key: REQ-013c4361595619bea95b9311ed36e61497c8a00ac5bd45e3efd2a71c778b355c
- Type: functional
- Priority: P2
- Priority basis: inferred
- Priority rationale: Recurring query execution supports repeated operational workflows and reduces manual effort; the source does not establish a more specific priority\.
- Originating candidates: CAND-8df2af985b0865f6c841b7458be78c405e329d54cd07b169e206ff941ceb2c7e

The system shall support repeated or scheduled use of saved queries, including recurring use such as monthly operations on items matching specified criteria\.

Sources and evidence:

Source: [conversations/conv\_pines018\_item\_transfer\.eml](<../data/corpus/conversations/conv_pines018_item_transfer.eml>); document ID: DOC-a47eb1f11286ff9099687b72a901e4a6ed2455b431087c0742aa78583c5bd80a; normalized lines 28–29.

> The "save queries for repeated use" is crucial\. We do this monthly - move
> all items in genre X that haven't circulated in 6 months\.

### REQ-011 — Generate Items Currently Checked Out Report

- Internal key: REQ-0194ede2e2e348ff5c24cbfb604872c53ec777610a44f5d10f7b15d7efbf8be9
- Type: functional
- Priority: P2
- Priority basis: inferred
- Priority rationale: The report is a specific operational reporting capability, but the source does not assign an explicit priority\.
- Originating candidates: CAND-af2620caa2835352f8c4f10988413f8cd94287039f98f29d7bd9acbd6e9485d5

The system shall provide an Items Currently Checked Out report\.

Sources and evidence:

Source: [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>); document ID: DOC-091180de9b2d4ea83267d989411ac89f415d4def3bbf7cd51651fb7fda8d8bf9; normalized lines 518–518.

> - Items Currently Checked Out

### REQ-012 — Relational database backend

- Internal key: REQ-019b1d41cf92a548a2780a8efac86580c234ac6b42313092caced1503dea0d40
- Type: nonfunctional
- Priority: P2
- Priority basis: explicitly specified
- Priority rationale: The source explicitly marks the fully relational database backend as High Priority; under the supplied priority scale, High Priority maps to P2\.
- Originating candidates: CAND-8817d2fe09b0632e6a2738ff06836dc4ff1ba348ad96a5d67d3588c3864256ce, CAND-89f83065ae1742a1bf1677e89beba3078f3a05a6c9e521b56167ec6f95834de1

The system shall use a fully relational database backend and shall work with the relational structure rather than against it\.

Sources and evidence:

Source: [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>); document ID: DOC-091180de9b2d4ea83267d989411ac89f415d4def3bbf7cd51651fb7fda8d8bf9; normalized lines 153–153.

> CO-1: The system must use a fully relational database back-end\. \[\* High Priority\]

Source: [meeting\_tech\_subcommittee\_2009-06-30\.txt](<../data/corpus/meeting_tech_subcommittee_2009-06-30.txt>); document ID: DOC-e081aa7bd57bf5e59c75a8a86f592124757b74dff1ee0df4badc10c025092d96; normalized lines 31–34.

> Robert confirmed that the system must use a fully relational database back-end\.
> He noted that PostgreSQL is the current choice for PINES and it meets this
> requirement\. The reporting system must work WITH the relational structure,
> not against it\.

### REQ-013 — Patron Balance Reports by Patron, Home Library, and System

- Internal key: REQ-024b618d9579d5dab0f0805011eaa804fd2bbe9c076bf2408113263bd866340f
- Type: functional
- Priority: P2
- Priority basis: inferred
- Priority rationale: Financial account reporting is important management functionality; no explicit source priority is provided\.
- Originating candidates: CAND-f0b3763da289ca2f75066fc05cdae98561d4bdf0bc87e103a5d70d6227b32e95

The system shall provide reports of patron account balances by patron, by home library, and for the entire system\.

Sources and evidence:

Source: [email\_financial\_reports\.eml](<../data/corpus/email_financial_reports.eml>); document ID: DOC-8b6cfb3cf368b794d82567933f9c85062740814819b1e28b4837f6021cbcbee6; normalized lines 15–17.

> 2\. Financial reports - staff need reports on:
>    - Patron account balances by patron, home library, and system
>    - Fines and charges accrued per time period \(last 12 months, YTD, last month\)

Source: [email\_financial\_reports\.eml](<../data/corpus/email_financial_reports.eml>); document ID: DOC-8b6cfb3cf368b794d82567933f9c85062740814819b1e28b4837f6021cbcbee6; normalized lines 124–125.

>    - Patron account balances by patron, home library, and system
>    - Fines and charges accrued per time period \(last 12 months, YTD, last month\)

### REQ-014 — Shelf Space Utilization Reports

- Internal key: REQ-041e44cb0ab21fc97625e408d3c290f7fb2d6215567cbed11cf43b296e11ff5a
- Type: functional
- Priority: P2
- Priority basis: explicitly specified
- Priority rationale: The source explicitly identifies shelf space utilization reports as important\.
- Originating candidates: CAND-8f79679d7c9152728fa6b7ab88b4930af8d60c41eb21c6363f24b7133fcb58a5

The system shall provide shelf space utilization reports\.

Sources and evidence:

Source: [meeting\_minutes/meeting\_2009-07-20\_minutes\.txt](<../data/corpus/meeting_minutes/meeting_2009-07-20_minutes.txt>); document ID: DOC-5ab1dd8bc97af3b1ab2e378495f0e0d75fd501fcc19f923c0d8fda831074281b; normalized lines 52–52.

>   - Shelf space utilization reports are important

### REQ-015 — Detailed Payments Received Report

- Internal key: REQ-04b6c2cc1e3847ea8aec226d7758663c58c059545dd9f0869422a8f15a3c28fe
- Type: functional
- Priority: P2
- Priority basis: inferred
- Priority rationale: Inferred as high priority because the evidence explicitly enumerates this required report\.
- Originating candidates: CAND-7c45d8d40c7c07636307b9d374b6f33502471ca6f48b546e7ec8e438657cbf5d

The system shall provide a Detailed Payments Received report\.

Sources and evidence:

Source: [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>); document ID: DOC-091180de9b2d4ea83267d989411ac89f415d4def3bbf7cd51651fb7fda8d8bf9; normalized lines 583–583.

> - Detailed Payments Received

### REQ-016 — Anonymized Demographic Statistics

- Internal key: REQ-05cb4e757788e452d3584a452b53cc757d16291bf6ea9a5f44ca511bfc3eb4a9
- Type: functional
- Priority: P2
- Priority basis: inferred
- Priority rationale: The capability supports demographic analysis while protecting privacy, but the source does not assign a formal priority level\.
- Originating candidates: CAND-0e506deb9a1e647ba46c6f66c60adee87babf6202235c41162ee1a6ef047a7ec

The system shall produce anonymized demographic statistics, including transactions by geographical region and age range, without exposing information that could identify an individual\.

Sources and evidence:

Source: [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>); document ID: DOC-091180de9b2d4ea83267d989411ac89f415d4def3bbf7cd51651fb7fda8d8bf9; normalized lines 316–319.

> 9\.2 Demographic Statistics
> The system should produce useful demographic statistics, including transactions
> by geographical regions, age ranges, etc\. The data used to produce these
> statistics must be anonymized - information that could be used to identify a

### REQ-017 — Provide Pivot Table Report Output Option

- Internal key: REQ-0631fd069698385e9c3b2f3e4c8d5296606d6c85e891b30749bd4878a49a6ddc
- Type: functional
- Priority: P3
- Priority basis: inferred
- Priority rationale: Pivot output is a useful analytical enhancement but is not identified as essential for basic operation\.
- Originating candidates: CAND-aee2451b88e390dd75447951414b1e52caed944ff12830dabaf9dc79d2b41aff

The system shall provide pivot table output as a report output option\.

Sources and evidence:

Source: [survey\_results\_2009\.txt](<../data/corpus/survey_results_2009.txt>); document ID: DOC-aac7bceef7a883652805583e98ec513b6ae2e7951e2ecfa18722127b1f12a5c4; normalized lines 97–97.

>   - "Pivot table output would be great"

### REQ-018 — Bib Records Edited Count Report

- Internal key: REQ-06ae1f2fbdbe44800091725474b0d8aefac31f56f51976ab43bb88ae220dae93
- Type: functional
- Priority: P2
- Priority basis: inferred
- Priority rationale: The report is explicitly identified as a necessary report type; the source does not assign a priority\.
- Originating candidates: CAND-dc31594e5bcbf6a30328cb898e8f4ed7896529776ad662c13cae0b0c75bd97af

The system shall provide a Bib Records Edited Count report\.

Sources and evidence:

Source: [evergreen\_reference\_2009\.txt](<../data/corpus/evergreen_reference_2009.txt>); document ID: DOC-e6aa9f8c6308ab748459f87b578a0df9df9c865b7911bac3686e865963b7af6f; normalized lines 151–151.

> - Bib Records Edited Count \(not available\)

### REQ-019 — Optional Address Book for Report Email Distribution

- Internal key: REQ-06cc288fe67ae0505b0dc4c9c8a62b23e08949626b7622e8651532a9715cd159
- Type: nonfunctional
- Priority: P4
- Priority basis: explicitly specified
- Priority rationale: The source characterizes this as desirable, indicating a convenience enhancement\.
- Originating candidates: CAND-d79cf16557191fa22451a45abaf6d3d9c8df88ab8b3fa2e4cf6e0177e25b5380

The system may provide an address book of regularly used email addresses for report distribution\.

Sources and evidence:

Source: [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>); document ID: DOC-091180de9b2d4ea83267d989411ac89f415d4def3bbf7cd51651fb7fda8d8bf9; normalized lines 626–627.

> - Ability to enter email addresses for report to be sent to - would be great to
>   have an address book of regularly used addresses

### REQ-020 — Periodic Report Availability or Scheduling for Quarterly Reviews

- Internal key: REQ-074d068b280ae3a2b37e9afc518c9ba66dfee641e23891167c0ecc377a82c38c
- Type: nonfunctional
- Priority: P3
- Priority basis: inferred
- Priority rationale: Quarterly management review support is useful but is not shown to be essential to basic operation; the source does not specify a scheduling mechanism\.
- Originating candidates: CAND-4efc0e79a646d5645dbd5d456af0a1680850ed231d2d81ebdf61d8673d07eb8b

The system shall support regular or periodic, including quarterly, availability or scheduling of the relevant report data to support directors' quarterly reviews\.

Sources and evidence:

Source: [conversations/conv\_pines016\_shelf\_space\.eml](<../data/corpus/conversations/conv_pines016_shelf_space.eml>); document ID: DOC-b507e8abe1ba7c996c1d86d688e90bcf2404694ec00528c8361f26dfc8bd82f1; normalized lines 84–85.

> I want this broken down per library AND per system\. Our directors review
> this data quarterly and need both views\.

### REQ-021 — Privacy-Preserving Transaction Archiving with Demographic Statistics

- Internal key: REQ-07c3ee473dadac84817b2277e6cb3656891b88832d1024f4951332ddbb8e2059
- Type: nonfunctional
- Priority: P1
- Priority basis: inferred
- Priority rationale: The requirement combines statutory patron-privacy protection with controlled statistical usefulness, making it critical privacy and compliance functionality\.
- Originating candidates: CAND-b0de2230c4d55b6714a05b648933e437a4d20e7d5e9c329bf6c22c9d95584991

The system shall archive transaction data in a form that preserves patron privacy as defined by State Law while still providing useful demographic statistics\.

Sources and evidence:

Source: [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>); document ID: DOC-091180de9b2d4ea83267d989411ac89f415d4def3bbf7cd51651fb7fda8d8bf9; normalized lines 271–274.

> 8\.6 Transaction Data Archiving
> Transactions should be archived in a form that protects patron privacy as
> defined by State Law, while providing useful demographic statistics\.
> 

### REQ-022 — Controlled and Ad Hoc Report Folders

- Internal key: REQ-0801480f36cb42d3178d8ca7b553d847b3826ba62e4e1e91738f9646c6674988
- Type: functional
- Priority: P2
- Priority basis: inferred
- Priority rationale: Controlled report access and ad hoc reporting are important administrative capabilities\.
- Originating candidates: CAND-cd1224310883a1f4707e1175c2590445bc7a6acad0a720f8e316cd4f8f7bb80c

The system shall allow system administrators to create shared folders that allow or disallow staff from running specified reports and that support ad hoc reports on specified sets of data\.

Sources and evidence:

Source: [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>); document ID: DOC-091180de9b2d4ea83267d989411ac89f415d4def3bbf7cd51651fb7fda8d8bf9; normalized lines 244–247.

> who can create and clone reports\. All permissions should be easy to administer\.
> System administrators should be able to create shared folders to allow or
> disallow staff from running specific reports, and/or to run ad hoc reports on
> specific sets of data\.

### REQ-023 — Report Output Formats

- Internal key: REQ-0a5e692f9e97183dabad28474e381b91d2923904c84b752bb58586ded73f718f
- Type: functional
- Priority: P2
- Priority basis: inferred
- Priority rationale: Multiple output formats support staff reporting workflows, but the source does not assign an explicit priority\.
- Originating candidates: CAND-29c4ba01d2f9cf6e200dd59ee871794c2b033f63c1f5b5f11c2bf0fc9dc63dcc

The system shall provide report output in Excel, HTML, and CSV formats\.

Sources and evidence:

Source: [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>); document ID: DOC-091180de9b2d4ea83267d989411ac89f415d4def3bbf7cd51651fb7fda8d8bf9; normalized lines 625–625.

> - Output would be in Excel, HTML, and CSV format

### REQ-024 — Management Specification Scope

- Internal key: REQ-0b0f974518fad561b3186d4d04ecd426b248cf8f333c1b059b441dfda7c795b9
- Type: nonfunctional
- Priority: P2
- Priority basis: inferred
- Priority rationale: Avoids conflicting or duplicated module specifications\.
- Originating candidates: CAND-d3d04a98c617e7a4f045ae31e00f8360416d7f5a7ba1e9fe9b0cf2526cec6bf4

The management-process specification shall include only requirements that directly or indirectly relate to management activities and shall not duplicate specifications developed separately for Acquisitions and Cataloging modules\.

Sources and evidence:

Source: [meeting\_minutes/meeting\_2009-03-15\_minutes\.txt](<../data/corpus/meeting_minutes/meeting_2009-03-15_minutes.txt>); document ID: DOC-defef992db2ae0e10167fd94902eac93f82c59c4c070df030ca2f77811082818; normalized lines 65–69.

> Susan Sexton-Cooley noted that the current specification presupposes the
> general data structures and functionality of a full-fledged ILS\. She said
> PINES is currently working on separate specifications for Acquisitions and
> Cataloging modules\. The group agreed to specify only those requirements that
> directly or indirectly relate to management activities\.

### REQ-025 — Save Item-Transfer Queries for Repeated Use

- Internal key: REQ-0b13b445a2eea4822fe4aa71a6fc4706a1cbdb82433a90a6b3593ec1cf27a0bc
- Type: functional
- Priority: P2
- Priority basis: inferred
- Priority rationale: Inferred as high priority because the evidence specifically requires repeated-use queries in the item transfer utility\.
- Originating candidates: CAND-7cd525708cf99590b441535f77c6ae1c06d208270c855478e877dc391d16d19e

The item transfer utility shall allow queries to be saved for repeated use\.

Sources and evidence:

Source: [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>); document ID: DOC-091180de9b2d4ea83267d989411ac89f415d4def3bbf7cd51651fb7fda8d8bf9; normalized lines 359–362.

> The utility should include:
>   - Ability to query for candidate materials
>   - Ability to save queries for repeated use
>   - Ability to manually select titles from query results

### REQ-026 — Timed Reversion of Item Location After Transfer

- Internal key: REQ-0b4f2cddd3f199e2f2faaefc355fc07c824110bec7cc88e02132b9a73e372204
- Type: functional
- Priority: P2
- Priority basis: inferred
- Priority rationale: Reversion supports item-transfer operations, but the source does not assign a priority or specify how the period is configured\.
- Originating candidates: CAND-aab216802cf265e16e28c51729a8002f33796469b76d259d756e9d0c7db117b2

The item transfer utility shall provide the ability to revert items to their original location after a set period of time\.

Sources and evidence:

Source: [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>); document ID: DOC-091180de9b2d4ea83267d989411ac89f415d4def3bbf7cd51651fb7fda8d8bf9; normalized lines 364–365.

>   - Mechanisms for moving items: changing location field, generating pull lists
>   - Ability to revert items to original location after a set period of time

### REQ-027 — Support Consortium Scale for Locations and Annual Volumes

- Internal key: REQ-0bf369c574dd1446c301fefbc8244c1b9e738fa6e8d93751bb992c2297455f05
- Type: nonfunctional
- Priority: P1
- Priority basis: inferred
- Priority rationale: The stated scale is a core operating constraint and is essential to system viability; no explicit source priority is provided\.
- Originating candidates: CAND-fae7c1b6bb14749f9bd236a1111e847138a52bacd7925f28671ae4e4e0a3f354

Management Processes shall support a library consortium with 286 locations, 17 million annual circulations, and purchasing and processing over 900,000 items per year\.

Sources and evidence:

Source: [meeting\_minutes/meeting\_2009-07-20\_minutes\.txt](<../data/corpus/meeting_minutes/meeting_2009-07-20_minutes.txt>); document ID: DOC-5ab1dd8bc97af3b1ab2e378495f0e0d75fd501fcc19f923c0d8fda831074281b; normalized lines 66–69.

> OE-1: Management Processes must support the needs of a large, multiple-system
>       library consortium\. Specifically, the system must support a library
>       consortium with 286 locations, 17 million annual circulations,
>       purchasing and processing over 900,000 items per year\. It is highly

### REQ-028 — Printable Transit Labels With Barcodes

- Internal key: REQ-0c113d026df68f16729ac7a566d781131b697eee2df934e938acc760322cec36
- Type: functional
- Priority: P3
- Priority basis: inferred
- Priority rationale: Printable labels are useful for transfer operations but are not identified as essential to basic operation\.
- Originating candidates: CAND-58e875ceaaa779afc7bcb7d8ad05cc618a66e02c52c68bc772ddf0bbb868b950

The system shall generate printable transit labels, including barcodes, for items being transferred\.

Sources and evidence:

Source: [conversations/conv\_pines018\_item\_transfer\.eml](<../data/corpus/conversations/conv_pines018_item_transfer.eml>); document ID: DOC-a47eb1f11286ff9099687b72a901e4a6ed2455b431087c0742aa78583c5bd80a; normalized lines 84–85.

> Also, can we generate transit labels? Like, printable barcodes for the
> items being transferred?

### REQ-029 — Capacity Status Color Coding in Interface

- Internal key: REQ-0cd60684d308634bc7ff6bb24e1a577c13868ead64ab9f65a38fb0227bac654b
- Type: functional
- Priority: P3
- Priority basis: inferred
- Priority rationale: Inferred as a useful interface enhancement; the source presents color-coding as suggested rather than mandatory\.
- Originating candidates: CAND-6f5cec804e36605c002a5e55e8ef7ddc3955f92a0ea7d8d1b5b945a71969313d

The system shall use interface color-coding to indicate capacity status, using green for under capacity, yellow for getting full, and red for at or over capacity\.

Sources and evidence:

Source: [conversations/conv\_pines015\_capacity\_interface\.eml](<../data/corpus/conversations/conv_pines015_capacity_interface.eml>); document ID: DOC-4acf2fdb375b86d49420e5743267e19b3f0af9ebe8bd764c1a88379aa9f5b662; normalized lines 36–37.

> 3\. Maybe color-coding - green for under capacity, yellow for getting full,
>    red for at/over capacity

### REQ-030 — Customizable item weeding reports

- Internal key: REQ-0cd6e2d32e669a0e764e5bbfc47fc544bff20080d82cb787b3a6c1b16f3514dc
- Type: functional
- Priority: P2
- Priority basis: inferred
- Priority rationale: The source identifies weeding reports as a most-used report type and requests customizable purge identification\.
- Originating candidates: CAND-8c652bc3345ea74741eb6655a3f950d14ae7d84725e80a46c4cca63b4fffdc9a, CAND-90765e8428262b81ed25442a788311ec6450ccc4302b3b96c06d09e6c3d517f8

The system shall provide utilities and reports to identify item records for purging based on customizable criteria, including criteria such as an item remaining in Missing status for more than X months or having Discard/Weed status\.

Sources and evidence:

Source: [conversations/conv\_pines021\_item\_purging\.eml](<../data/corpus/conversations/conv_pines021_item_purging.eml>); document ID: DOC-74ccbb6ac77183c0d1b34b1e79ed8fcbbfb4e7525cb33798c3af832fed733ad8; normalized lines 3–9.

> We're doing our annual weeding and I need better reporting\. Specifically:
> 
> 1\. I need to identify item records to purge based on customizable criteria\.
>    For example:
>    - Item has been in status "missing" for more than X months
>    - Item has status "discard/weed"
> 

Source: [conversations/conv\_pines021\_item\_purging\.eml](<../data/corpus/conversations/conv_pines021_item_purging.eml>); document ID: DOC-74ccbb6ac77183c0d1b34b1e79ed8fcbbfb4e7525cb33798c3af832fed733ad8; normalized lines 121–126.

> Summarizing the item record purging requirements:
> 
> The system should provide a utility and reports for identifying item records
> to purge, based on customizable criteria such as:
> - An item has been in status "missing" for more than X months
> - An item has status "discard/weed"

Source: [interview\_cataloging\_2009-05-08\.txt](<../data/corpus/interview_cataloging_2009-05-08.txt>); document ID: DOC-a79fab45108210e6bce7d92153dfcf055f2ef6b2cdab49a3f6f5717a3e35f29f; normalized lines 72–76.

> THOMAS: Weeding reports are my most-used report type\. I need to identify items
> for purging based on customizable criteria\. For example:
> - Item has been in status "missing" for more than X months
> - Item has status "discard/weed"
> 

### REQ-031 — Separate Edit and Circulation Dates on Reports

- Internal key: REQ-0d6669b08c08f44c8cfbfa02c634c6005dcba584ee6a8d0e6dfe7a3d308f16e8
- Type: functional
- Priority: P2
- Priority basis: inferred
- Priority rationale: Accurate timestamps are important for report interpretation, but no explicit priority is supplied\.
- Originating candidates: CAND-5ccf114ce994ef24a37962a6d9d0f4b4cb5accfa420990571cb5e65f3badcd6a

The system shall display the last edit date on reports based only on edits to the bibliographic or item record and shall keep the edit timestamp separate from the last circulation date\.

Sources and evidence:

Source: [interview\_cataloging\_2009-05-08\.txt](<../data/corpus/interview_cataloging_2009-05-08.txt>); document ID: DOC-a79fab45108210e6bce7d92153dfcf055f2ef6b2cdab49a3f6f5717a3e35f29f; normalized lines 116–118.

> 4\. I need to be able to see the last edit date on reports, but it should be
>    only when the item is edited and not include the last circulation\. The
>    current system combines these dates\.

### REQ-032 — Undo Function for Mistaken Transfers

- Internal key: REQ-0e6c5261b0a1640d933fe9a3c80151623177b25eb91529c956c4fecd8fb648cf
- Type: functional
- Priority: P2
- Priority basis: inferred
- Priority rationale: Undo capability protects against operational mistakes and has substantial impact, but the source does not establish it as critical\.
- Originating candidates: CAND-c742cd2b1d1d299cb25523530d924d851bc17c0d21b0a8390f2c1985e58974b5

The system shall provide an undo function to revert mistaken transfers\.

Sources and evidence:

Source: [conversations/conv\_pines018\_item\_transfer\.eml](<../data/corpus/conversations/conv_pines018_item_transfer.eml>); document ID: DOC-a47eb1f11286ff9099687b72a901e4a6ed2455b431087c0742aa78583c5bd80a; normalized lines 103–103.

> And we need an undo function\! What if someone clicks the wrong button?

### REQ-033 — Missing and Damaged Counts Report

- Internal key: REQ-0f1181ddc427c4dbfe0fdd104eec5740906fb43ff085e68c6bfd2b6a897d5b9d
- Type: functional
- Priority: P2
- Priority basis: inferred
- Priority rationale: The source identifies auditing and collection decisions as uses for these counts, indicating substantial operational impact\.
- Originating candidates: CAND-29dc146fbfab9452c3e062d94c0c4494280e1ebaef4bad6677bff8a9d99d8c70

The system shall provide a missing/damaged report that shows counts of items reported missing or damaged\.

Sources and evidence:

Source: [conversations/conv\_pines019\_020\_missing\_intransit\.eml](<../data/corpus/conversations/conv_pines019_020_missing_intransit.eml>); document ID: DOC-b233b12122cae48b5821d685f6dc058d2d2e3cc8d7f77622fa4e7e55bddc5399; normalized lines 14–16.

> Second this\. We use the data for two purposes:
> 1\. Auditing - showing how many items went missing/were damaged
> 2\. Collection decisions - if we keep losing the same titles, maybe we need

### REQ-034 — Temporary Event Transfers

- Internal key: REQ-0f2df5fec52e41fa3683855f47c8a7bbe69e0b0e6231f03c0594a53e780da514
- Type: functional
- Priority: P2
- Priority basis: inferred
- Priority rationale: Temporary transfers support an identified outreach use case, but no explicit priority is supplied\.
- Originating candidates: CAND-5a8bccc70d8bad6722fecaf52001868994ddff8e762fb963e4733978f3dd48f3

The system shall allow items to be transferred to a temporary location for a specific event or program and reverted after the event\.

Sources and evidence:

Source: [conversations/conv\_pines018\_item\_transfer\.eml](<../data/corpus/conversations/conv_pines018_item_transfer.eml>); document ID: DOC-a47eb1f11286ff9099687b72a901e4a6ed2455b431087c0742aa78583c5bd80a; normalized lines 134–137.

> Also, for the outreach program use case - can we transfer items to a
> temporary location for a specific event or program? Like, move 20 biographies
> to the community center for their genealogy workshop, then revert them
> after the event\.

### REQ-035 — Store Check-In and Renewal Timestamps Separately

- Internal key: REQ-0f7d0c19e19070f9e9cf6b47dbe31b8efcc082a2c9d843ceee779e04f169cb3a
- Type: functional
- Priority: P2
- Priority basis: inferred
- Priority rationale: Separate timestamps are important for accurate circulation reporting\.
- Originating candidates: CAND-1b4af7271a734267072ececbc204022f41cb142f17cafaa0aa494d0d7ae41355

The system shall store check-in date and time separately from renewals so that reports can obtain check-in timestamps without conflating them with renewal timestamps\.

Sources and evidence:

Source: [evergreen\_reference\_2009\.txt](<../data/corpus/evergreen_reference_2009.txt>); document ID: DOC-e6aa9f8c6308ab748459f87b578a0df9df9c865b7911bac3686e865963b7af6f; normalized lines 202–203.

> - Checkin Date/time not including renewals - checkin and renewal timestamps
>   are stored together

### REQ-036 — Material Volume Report by Library and Custom Categories

- Internal key: REQ-104449e9d557f36a5702fd2cb149c56e7c2d7b0e2d2f703ba162babef3fc3ddb
- Type: functional
- Priority: P2
- Priority basis: inferred
- Priority rationale: The sources describe collection-volume reporting and its operational breakdowns but do not assign a formal priority level\.
- Originating candidates: CAND-0afeca455dbfc1369bbcf9b9e5f79e64a642060dd5a480acfc44ed24d865ef39, CAND-2ae75acd187869ad6e351b5d95e51b57f8bb0981288135f19c7d3a0eb4ad9220, CAND-3a2f5351b9d878d8624a7eecb4280977e040a1be97398e2f3bf6ce2eb43d182f, CAND-629713e3c077bf3bedf37177ad2da63a8652375ccf9476eac77861123a9a4d63, CAND-af44c77e71c4d09def9032d41935558b89e1699a2fc782938e053a0298542fc3

The system shall provide a material volume report for a given branch at any point in time, including separate counts for new acquisitions, items on the shelf that are checked in, and items out in circulation that are checked out\. The report shall allow volume to be broken down by categories such as total items in the branch, number of holds, adult fiction, board books, and other customizable categories\.

Sources and evidence:

Source: [conversations/conv\_pines014\_material\_volume\.eml](<../data/corpus/conversations/conv_pines014_material_volume.eml>); document ID: DOC-f10d646016479a881ae8ff4ab4043844ee55a671d71f1943623db3fbb5589d8a; normalized lines 3–6.

> Quick question - how do I get a report that tells me how many items we have
> at Dalton-Whitman at any given moment? Not just total count, but broken down
> by categories\. Like total items in library, number of holds, number of adult
> fiction, number of board books\.\.\.

Source: [conversations/conv\_pines014\_material\_volume\.eml](<../data/corpus/conversations/conv_pines014_material_volume.eml>); document ID: DOC-f10d646016479a881ae8ff4ab4043844ee55a671d71f1943623db3fbb5589d8a; normalized lines 30–36.

> Yes, George has a good point\. The volume should include:
> 1\. New acquisitions \(items recently added\)
> 2\. Items on the shelf \(checked in\)
> 3\. Items out in circulation \(checked out\)
> 
> I think Maria is asking for all three counts separately plus a total\. That
> makes sense for collection management\.

Source: [conversations/conv\_pines014\_material\_volume\.eml](<../data/corpus/conversations/conv_pines014_material_volume.eml>); document ID: DOC-f10d646016479a881ae8ff4ab4043844ee55a671d71f1943623db3fbb5589d8a; normalized lines 88–96.

> Thanks everyone for the input\. Here's what I'm hearing for the "Material
> Volume Report" requirement:
> 
> The system should provide the ability to report on the volume of material
> in a given library at any point in time, based on:
> - New acquisitions
> - Items on the shelf \(checked in\)
> - Items out in circulation \(checked out\)
> 

Source: [conversations/conv\_pines014\_material\_volume\.eml](<../data/corpus/conversations/conv_pines014_material_volume.eml>); document ID: DOC-f10d646016479a881ae8ff4ab4043844ee55a671d71f1943623db3fbb5589d8a; normalized lines 91–96.

> The system should provide the ability to report on the volume of material
> in a given library at any point in time, based on:
> - New acquisitions
> - Items on the shelf \(checked in\)
> - Items out in circulation \(checked out\)
> 

Source: [conversations/conv\_pines014\_material\_volume\.eml](<../data/corpus/conversations/conv_pines014_material_volume.eml>); document ID: DOC-f10d646016479a881ae8ff4ab4043844ee55a671d71f1943623db3fbb5589d8a; normalized lines 97–102.

> The report should allow breaking down volume in categories such as:
> - Total items in library
> - Number of holds
> - Number of adult fiction
> - Number of board books
> - Other customizable categories

Source: [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>); document ID: DOC-091180de9b2d4ea83267d989411ac89f415d4def3bbf7cd51651fb7fda8d8bf9; normalized lines 326–331.

> 10\.1 Material Volume Report
> Ability to report on the volume of material in a given library at any point in
> time, based on new acquisitions, items on the shelf, and items out in
> circulation\. The report should allow breaking down volume in categories such
> as: total items in library, number of holds, number of adult fiction, number
> of board books, etc\.

Source: [interview\_cataloging\_2009-05-08\.txt](<../data/corpus/interview_cataloging_2009-05-08.txt>); document ID: DOC-a79fab45108210e6bce7d92153dfcf055f2ef6b2cdab49a3f6f5717a3e35f29f; normalized lines 107–110.

> 2\. The material volume report helps me understand how much we have\. I need to
>    report on volume based on acquisitions, items on shelf, and items in
>    circulation, broken down by categories like total items, holds, adult
>    fiction, board books, etc\.

### REQ-037 — Director-Level Financial Reports

- Internal key: REQ-10a2c5b7e4fb128df54d02b40b9d402527a628d6113f91d50b40b8b4a6a5fe76
- Type: functional
- Priority: P2
- Priority basis: inferred
- Priority rationale: Director-level financial reporting is an identified business need, but no explicit source priority is provided\.
- Originating candidates: CAND-e884e6ababfe41fe3c05f8b878305dd255452e3b528e52451aca76cfd1760ad7

The system shall provide financial reports tailored to director-level needs\.

Sources and evidence:

Source: [meeting\_minutes/meeting\_2009-07-20\_minutes\.txt](<../data/corpus/meeting_minutes/meeting_2009-07-20_minutes.txt>); document ID: DOC-5ab1dd8bc97af3b1ab2e378495f0e0d75fd501fcc19f923c0d8fda831074281b; normalized lines 35–36.

>   - Inventory and capacity reports are used daily
>   - Financial report needs are understood at the director level

### REQ-038 — Aged In-Transit Items Report

- Internal key: REQ-112bc6169b74f99b74669890aa6112c9a3cde4f1092a37f1183ba8a7bca59929
- Type: functional
- Priority: P2
- Priority basis: inferred
- Priority rationale: The report supports delivery follow-up and includes a configurable operational threshold, but the source does not assign a formal priority level\.
- Originating candidates: CAND-0ffd6b9e640006b755ac309601feb5ceba01b917e171cb7b6f16c7a79a51e3bc

The system shall generate a report listing items that have been in transit for more than a configurable number of days, available by branch and by system, merging transit-to and transit-from items into one report\.

Sources and evidence:

Source: [conversations/conv\_pines019\_020\_missing\_intransit\.eml](<../data/corpus/conversations/conv_pines019_020_missing_intransit.eml>); document ID: DOC-b233b12122cae48b5821d685f6dc058d2d2e3cc8d7f77622fa4e7e55bddc5399; normalized lines 86–89.

> 2\. IN-TRANSIT ITEMS REPORT:
>    System generates a list of items that have been in-transit for more than
>    X days \(X configurable\), per branch and per system\. The report merges
>    transit-to and transit-from into one report for ease of front-line staff\.

Source: [conversations/conv\_pines019\_020\_missing\_intransit\.eml](<../data/corpus/conversations/conv_pines019_020_missing_intransit.eml>); document ID: DOC-b233b12122cae48b5821d685f6dc058d2d2e3cc8d7f77622fa4e7e55bddc5399; normalized lines 111–113.

>    "System generates a list of items in-transit for more than X days \(X
>    configurable\), per branch and per system\. Report merges transit-to and
>    transit-from into one report\."

### REQ-039 — Batch operations and data-quality workflows

- Internal key: REQ-1174f75bc65d73fc20211bb38a545ccba560146803442678a7ee33c8c7712c24
- Type: nonfunctional
- Priority: P2
- Priority basis: inferred
- Priority rationale: The source emphasizes batch operations and data quality as actionable requirements with substantial operational impact\.
- Originating candidates: CAND-8bd6179a138ba10b91aea9abee7c8b881663f85f63e559dbaef7928c0e8ad896

The system shall support batch operations and data-quality features and workflows across reporting and cataloging functions\.

Sources and evidence:

Source: [interview\_cataloging\_2009-05-08\.txt](<../data/corpus/interview_cataloging_2009-05-08.txt>); document ID: DOC-a79fab45108210e6bce7d92153dfcf055f2ef6b2cdab49a3f6f5717a3e35f29f; normalized lines 123–124.

> - Thomas provided very specific, actionable requirements
> - He emphasized the importance of batch operations and data quality

### REQ-040 — Staff Productivity and Workflow Reporting

- Internal key: REQ-11be320c3e87894730bd0c6d08942c810e2cf75770097faae1e03d027e821485
- Type: functional
- Priority: P2
- Priority basis: inferred
- Priority rationale: The source identifies staff productivity and workflow analysis as a required analytical capability; the source does not assign a priority\.
- Originating candidates: CAND-dc8acbb37eb0428634745aa31b7f901db91bc335085a8d865c8e921eba2f5cbd

The system shall provide reporting and analysis capabilities for staff productivity and workflow\.

Sources and evidence:

Source: [meeting\_minutes/meeting\_2009-03-15\_minutes\.txt](<../data/corpus/meeting_minutes/meeting_2009-03-15_minutes.txt>); document ID: DOC-defef992db2ae0e10167fd94902eac93f82c59c4c070df030ca2f77811082818; normalized lines 62–62.

>   - Analyzing staff productivity and workflow

### REQ-041 — Payment Method Reporting for Financial Reconciliation

- Internal key: REQ-132114c65eee111425a4573ea3d23198475d2956c7a12a851178775a9096cfff
- Type: functional
- Priority: P2
- Priority basis: inferred
- Priority rationale: Payment-method recording supports financial control and daily reconciliation\.
- Originating candidates: CAND-42c57e31eea5838c8b279921de7b6512425150bcd8962ff0d8c9b308882ec0ba

The system shall record payment method details, including cash, credit card, and check, to support financial reporting and daily reconciliation\.

Sources and evidence:

Source: [email\_financial\_reports\.eml](<../data/corpus/email_financial_reports.eml>); document ID: DOC-8b6cfb3cf368b794d82567933f9c85062740814819b1e28b4837f6021cbcbee6; normalized lines 71–72.

> - The financial reports need to show payments by method - cash, credit card,
>   check, etc\. This helps with daily reconciliation\.

Source: [email\_financial\_reports\.eml](<../data/corpus/email_financial_reports.eml>); document ID: DOC-8b6cfb3cf368b794d82567933f9c85062740814819b1e28b4837f6021cbcbee6; normalized lines 129–130.

>    - Payments made per time period and per payment method \(staff desk,
>      self-check station, OPAC\)

### REQ-042 — Patron Count by Home Library Report

- Internal key: REQ-140c8dff3bef72b3bc3db8c25d0bb367fff8760336ab23a3c306c8c6a54d4372
- Type: functional
- Priority: P2
- Priority basis: inferred
- Priority rationale: This is a specific demographic and branch-analysis report requested by the source\.
- Originating candidates: CAND-44e028a885fd0ceaab543ea135fcd42c9f7a10b089b81588c10e1200f16a12f6

The system shall provide a report counting patrons by home library\.

Sources and evidence:

Source: [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>); document ID: DOC-091180de9b2d4ea83267d989411ac89f415d4def3bbf7cd51651fb7fda8d8bf9; normalized lines 549–549.

> - Patron Count by Home Library

### REQ-043 — Role-Based Report Permissions

- Internal key: REQ-1542ab7fef252056a50f9108296a50c609ab1c7798ddc69c24d50aacb02ccaca
- Type: nonfunctional
- Priority: P2
- Priority basis: inferred
- Priority rationale: Access control materially affects secure and manageable operation\.
- Originating candidates: CAND-ccd7ea4ab293e2721bef79847565cf04bf4655fb6d860e061b8be67f3bdfc49f

The system shall administer report permissions through roles, and changing a user's role shall automatically update that user's report permissions\.

Sources and evidence:

Source: [email\_report\_features\.eml](<../data/corpus/email_report_features.eml>); document ID: DOC-d9e168e0c03903021bf9e636e1d8e5f56dfcb79cc110d3839e38175a7c54344e; normalized lines 55–57.

> The permissions need to be easy to administer\. If I change someone from "Staff"
> to "Manager," their report permissions should update automatically based on
> the role\.

### REQ-044 — Background Report Processing with Cached Results When Needed

- Internal key: REQ-1672aa797f51ac49051ee329dbe173d2fb7a4ee576ee1421ded739bb790e1a71
- Type: nonfunctional
- Priority: P2
- Priority basis: inferred
- Priority rationale: Inferred as high priority because the evidence identifies background processing and caching to address slow queries on large datasets\.
- Originating candidates: CAND-76e7503afd5e401e1a131565a66493c42801cc78fe902a9bc5cabbae0181a2bf

The system shall execute reports as background processes and cache their results when needed to mitigate performance impact for large datasets\.

Sources and evidence:

Source: [conversations/conv\_pines024\_inactive\_patrons\.eml](<../data/corpus/conversations/conv_pines024_inactive_patrons.eml>); document ID: DOC-705ab8a51bf22b7b619dae61bf8d2be1cf2487e749f13e7ac55fdde430357793; normalized lines 99–101.

> One performance note: for 3\.5 million patrons, this query could be slow\.
> We should run it as a background report and cache results\.
> 

Source: [conversations/conv\_pines024\_inactive\_patrons\.eml](<../data/corpus/conversations/conv_pines024_inactive_patrons.eml>); document ID: DOC-705ab8a51bf22b7b619dae61bf8d2be1cf2487e749f13e7ac55fdde430357793; normalized lines 143–143.

> - Background processing for performance

### REQ-045 — Consortium Scale Support

- Internal key: REQ-16ae6ac8c8645e39f59bb3b5e0ab454b414b354fa1062b27fb64d892e424ae3c
- Type: nonfunctional
- Priority: P1
- Priority basis: inferred
- Priority rationale: The stated scale is a mandatory capacity condition for the target consortium, although no formal priority label is supplied\.
- Originating candidates: CAND-5529179bb446f31d0b366c23743f0decc38ba0eca4383169bfb4591892cdca6e

The system shall support a library consortium with 286 locations, 17 million annual circulations, and purchasing and processing of more than 900,000 items per year\.

Sources and evidence:

Source: [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>); document ID: DOC-091180de9b2d4ea83267d989411ac89f415d4def3bbf7cd51651fb7fda8d8bf9; normalized lines 126–127.

> OE-1: The system must support a library consortium with 286 locations, 17 million
>       annual circulations, and purchasing/processing over 900,000 items per year\.

### REQ-046 — In-Transit Items With Outstanding Holds

- Internal key: REQ-1727ffbefccf46e0885013da826069199d8e0e41eedf69f52c48d433ecc98ddf
- Type: functional
- Priority: P2
- Priority basis: inferred
- Priority rationale: This report supports important item and hold management\.
- Originating candidates: CAND-13523719220bb248315f5b1c8930e7efa88fc53bf60aea1eccff1896406fe6f0

The system shall provide a report of in-transit items with outstanding holds\.

Sources and evidence:

Source: [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>); document ID: DOC-091180de9b2d4ea83267d989411ac89f415d4def3bbf7cd51651fb7fda8d8bf9; normalized lines 281–283.

>   - In-transit items with outstanding hold
>   - Items that have been in-transit for more than X days
>   - Items that are the last copy in the system

### REQ-047 — Fines Stopped Reason Report

- Internal key: REQ-1993897f0cc8a87078b872ed55cd076825df08ab489dfd4d052efe3ba6ae0e7a
- Type: functional
- Priority: P3
- Priority basis: inferred
- Priority rationale: The report fills an identified reporting gap, but the source does not indicate that it is essential to core operation\.
- Originating candidates: CAND-31c7966ec2d46c14333f51369be84647d74fbc4988bce381e79465292a352d2f

The system shall provide a List of Items by Fines Stopped Reason report\.

Sources and evidence:

Source: [evergreen\_reference\_2009\.txt](<../data/corpus/evergreen_reference_2009.txt>); document ID: DOC-e6aa9f8c6308ab748459f87b578a0df9df9c865b7911bac3686e865963b7af6f; normalized lines 142–142.

> - List of Items by Fines Stopped Reason \(not available\)

### REQ-048 — Read-Only OPAC Reporting Access

- Internal key: REQ-1a2eddfe406759457c40f392749961f439007051a7492c01ac3d0b97fb964f6e
- Type: functional
- Priority: P2
- Priority basis: inferred
- Priority rationale: OPAC integration supplies required reporting data while preserving source-system data integrity; no explicit source priority is provided\.
- Originating candidates: CAND-efa36da8c136b37b661a9a364466bfb4cb6c053746405bac285350f7a23f056f

The reporting system shall interact with the OPAC to query patron-created holds and circulation transactions but shall not modify OPAC data\.

Sources and evidence:

Source: [meeting\_tech\_subcommittee\_2009-06-30\.txt](<../data/corpus/meeting_tech_subcommittee_2009-06-30.txt>); document ID: DOC-e081aa7bd57bf5e59c75a8a86f592124757b74dff1ee0df4badc10c025092d96; normalized lines 152–156.

> 4\.5 OPAC INTEGRATION
> DE-3: Management Processes interact with a patron interface \(OPAC\)\.
> 
> "Patrons create holds and circulation transactions through the OPAC," Robert
> said\. "The reporting system queries this data, but doesn't modify it\."

### REQ-049 — Schedule Reports at Multiple Frequencies

- Internal key: REQ-1a585170f6200d72a170a9d5ab26b4788941d8a63df21131ccfcb07d6d035754
- Type: functional
- Priority: P2
- Priority basis: inferred
- Priority rationale: Scheduled reporting is important operational functionality, while the sources do not establish that it is essential for core operation\.
- Originating candidates: CAND-3bdeff3f1151aca3fb45a0106dd29435d2b71b907f7687fd4c507c9b79b3ee77

The system shall support scheduling reports at regular intervals, including daily, weekly, monthly, hourly, and other frequencies\.

Sources and evidence:

Source: [evergreen\_reference\_2009\.txt](<../data/corpus/evergreen_reference_2009.txt>); document ID: DOC-e6aa9f8c6308ab748459f87b578a0df9df9c865b7911bac3686e865963b7af6f; normalized lines 73–79.

> 2\.3 REPORT SCHEDULING
> Some reports can be scheduled to run at regular intervals \(daily, weekly,
> monthly\)\. However, scheduling options are limited:
> 
> - No hourly scheduling
> - No ability to check multiple reports to run at the same time
> - No email delivery \(reports can only be downloaded from the web interface\)

### REQ-050 — Centralized Multi-Location Management

- Internal key: REQ-1ab543c0a25babe1fd371782db199fca173a295ba6715d96727b4aa895042f0f
- Type: nonfunctional
- Priority: P2
- Priority basis: inferred
- Priority rationale: Centralized operation is an explicit architectural assumption supporting multiple locations; the source does not assign a priority\.
- Originating candidates: CAND-da02cd5a6ab15e849c36876ebd1b3b7fac8cebc91409999913c95c18209bc998

The system shall consolidate Management Processes at a central location that accepts input from and provides services to multiple locations\.

Sources and evidence:

Source: [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>); document ID: DOC-091180de9b2d4ea83267d989411ac89f415d4def3bbf7cd51651fb7fda8d8bf9; normalized lines 208–209.

> AS-2: Management Processes are consolidated at a central location, and accept
>       input and provide services to multiple locations\.

### REQ-051 — Regular Expression Query Support

- Internal key: REQ-1b9c1ad416aef54b2aafdf7381ad663c89d97c803be3ceb2d3f4a385f7094d2c
- Type: functional
- Priority: P3
- Priority basis: inferred
- Priority rationale: Regular expression support is a useful query capability but is not identified as essential to basic operation\.
- Originating candidates: CAND-5cdf7eff611619932cd7b1e37e71c100a5fc2b261bb374e6bef861b9b3e79458

The system shall support regular expression use in queries\.

Sources and evidence:

Source: [evergreen\_reference\_2009\.txt](<../data/corpus/evergreen_reference_2009.txt>); document ID: DOC-e6aa9f8c6308ab748459f87b578a0df9df9c865b7911bac3686e865963b7af6f; normalized lines 41–41.

> - No regular expression support

### REQ-052 — Predefined Board and Executive Reports for Annual Reporting

- Internal key: REQ-1bb2dc57368dcf2ef1fa46aee853dc91f05efe385ba78341e58d96448bf9b72e
- Type: functional
- Priority: P2
- Priority basis: inferred
- Priority rationale: Inferred as high priority because the evidence explicitly requires reports for boards, executive use, and state reporting\.
- Originating candidates: CAND-8365541838de5641c57ab2a1833631d40f67a64f715995902d7862a274f79dce

The system shall provide pre-defined Board and Executive reports, including basic statistics required by the Georgia Annual Report and Application for State Aid\.

Sources and evidence:

Source: [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>); document ID: DOC-091180de9b2d4ea83267d989411ac89f415d4def3bbf7cd51651fb7fda8d8bf9; normalized lines 260–263.

> 8\.5 Board Reports / Executive Reports
> The system should provide pre-defined reports for consumption by library boards
> and other external consumers\. These should include basic statistics like those
> required by the Georgia Annual Report and Application for State Aid\.

### REQ-053 — Configurable Inactive Patron Report by Organizational Level

- Internal key: REQ-1bd4de4fce7952b990a84b0ced6483a560f44842c7a50ad1a4cc8ef8184650ee
- Type: functional
- Priority: P2
- Priority basis: inferred
- Priority rationale: Inactive-patron reporting is an important administrative capability with an explicitly configurable threshold, but no formal priority is supplied\.
- Originating candidates: CAND-4d37e3d4bb54e2d43a3f7417f6520aed696c9eeb12007c263f51bb80e5cb8f74

The system shall generate a configurable list of inactive patrons with no circulation or electronic activity in the last X days, where X is configurable, and shall support configuration by System, Home Library, County, and other stated organizational levels\.

Sources and evidence:

Source: [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>); document ID: DOC-091180de9b2d4ea83267d989411ac89f415d4def3bbf7cd51651fb7fda8d8bf9; normalized lines 407–411.

> 11\.2 Inactive Patrons Report
> The system should generate a list of patrons with no circulation or electronic
> activity in the last X days \(X configurable\)\. The list should be configurable
> to System, Home Library, County, etc\.
> 

### REQ-054 — Centralized Multi-Location Management

- Internal key: REQ-1c06a018874f68e74b6bb3d354549d34ccdc7ca19631c46ae69ea925c822b010
- Type: nonfunctional
- Priority: P2
- Priority basis: inferred
- Priority rationale: Centralization is identified as important for providing a single source of truth for reporting; the source does not establish a higher priority\.
- Originating candidates: CAND-9139c6ef9d904680f4d9ae9939444cbae16c1cecb88660072540a3d961348d30

Management Processes shall be consolidated at a central location and shall accept input from and provide services to multiple locations\.

Sources and evidence:

Source: [meeting\_tech\_subcommittee\_2009-06-30\.txt](<../data/corpus/meeting_tech_subcommittee_2009-06-30.txt>); document ID: DOC-e081aa7bd57bf5e59c75a8a86f592124757b74dff1ee0df4badc10c025092d96; normalized lines 127–133.

> 4\.2 CENTRAL CONSOLIDATION
> AS-2: Management Processes are consolidated at a central location, and accept
> input and provide services to multiple locations\.
> 
> "Centralization is good for reporting," Katherine noted\. "We get a single
> source of truth\. The challenge is making sure data from all locations is complete
> and current\."

### REQ-055 — Report Scheduling Options

- Internal key: REQ-1f32e45a08417bb5fa4738861a2718e80c3bb3f2215486380c3f1534f13cc331
- Type: functional
- Priority: P2
- Priority basis: inferred
- Priority rationale: Scheduling supports recurring operational reporting, but no explicit source priority is provided\.
- Originating candidates: CAND-e86ce8b434d47af8fdd6d4246d3fe39317c438e18675de1ed40c5ec9fe23833e

The system shall allow users to select Run ASAP, Hourly, Daily, Weekly, Monthly, or Yearly scheduling for reports\.

Sources and evidence:

Source: [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>); document ID: DOC-091180de9b2d4ea83267d989411ac89f415d4def3bbf7cd51651fb7fda8d8bf9; normalized lines 624–624.

> - Ability to select Run ASAP, Hourly, Daily, Weekly, Monthly, Yearly

### REQ-056 — Transaction Grouping by Hour, Terminal, Branch, and System

- Internal key: REQ-1fc20f70bb4490befccf8582e07e2f381f07a8f3553e194d079d88d32c95799c
- Type: functional
- Priority: P2
- Priority basis: inferred
- Priority rationale: Inferred as important operational and financial analysis functionality; no explicit source priority is supplied\.
- Originating candidates: CAND-68ff94d2b19db868ef439a55726c2aced5231bf23cdb9a42ee93b91209fdf19e

The system shall allow transactions to be grouped by hour, terminal, branch, and system\.

Sources and evidence:

Source: [survey\_results\_2009\.txt](<../data/corpus/survey_results_2009.txt>); document ID: DOC-aac7bceef7a883652805583e98ec513b6ae2e7951e2ecfa18722127b1f12a5c4; normalized lines 112–113.

> 2\. Transactions can be grouped by hour, terminal, branch, and system\.
> 

### REQ-057 — Reporting Permissions and Reporting Template Management

- Internal key: REQ-21e2586cf7d27ad176e7b5433dbae3a7879f3f3a5139bc7d3807a7eb0057fdcc
- Type: functional
- Priority: P2
- Priority basis: inferred
- Priority rationale: Management-level reporting control is important functionality, but the source does not assign a formal priority level\.
- Originating candidates: CAND-06a160839031bbc48ca34208ff86cf1025843496af82bbb0a84b7b640071879e

The system shall provide fine-grained permissions and template management for reporting\.

Sources and evidence:

Source: [evergreen\_reference\_2009\.txt](<../data/corpus/evergreen_reference_2009.txt>); document ID: DOC-e6aa9f8c6308ab748459f87b578a0df9df9c865b7911bac3686e865963b7af6f; normalized lines 215–215.

> 2\. Implement fine-grained permissions and template management

### REQ-058 — Configurable Item Purge Criteria

- Internal key: REQ-21eb547e8be2f8c2710dfa12df27614f5242422bc931082d6d5154b093c538d7
- Type: functional
- Priority: P2
- Priority basis: inferred
- Priority rationale: Supports controlled collection maintenance and record lifecycle management\.
- Originating candidates: CAND-d3cad322c5d4485132df7b22ca4e3d7ccc175da4072706569d4b33d99efcff2d

The system shall provide status-based, time-based, and activity-based criteria for identifying item records to purge, and shall allow multiple criteria to be combined, including a status-duration condition and a last-circulated condition joined by AND\.

Sources and evidence:

Source: [conversations/conv\_pines021\_item\_purging\.eml](<../data/corpus/conversations/conv_pines021_item_purging.eml>); document ID: DOC-74ccbb6ac77183c0d1b34b1e79ed8fcbbfb4e7525cb33798c3af832fed733ad8; normalized lines 50–56.

> For the purging criteria - can we make them really customizable? Like,
> I might want to purge items:
> - That haven't circulated in 5\+ years
> - With status "missing" for 2\+ years
> - That are damaged AND haven't circulated in 2\+ years
> 
> The system should let us combine criteria\.

Source: [conversations/conv\_pines021\_item\_purging\.eml](<../data/corpus/conversations/conv_pines021_item_purging.eml>); document ID: DOC-74ccbb6ac77183c0d1b34b1e79ed8fcbbfb4e7525cb33798c3af832fed733ad8; normalized lines 89–96.

> I want the customizable criteria for purging to include:
> - Status-based criteria \(missing, discard/weed, damaged\)
> - Time-based criteria \(in status for X months/years\)
> - Activity-based criteria \(last circulated X days/months/years ago\)
> 
> Can we combine these? Like "items with status 'missing' for more than 6
> months AND haven't circulated in 2 years"?
> 

Source: [conversations/conv\_pines021\_item\_purging\.eml](<../data/corpus/conversations/conv_pines021_item_purging.eml>); document ID: DOC-74ccbb6ac77183c0d1b34b1e79ed8fcbbfb4e7525cb33798c3af832fed733ad8; normalized lines 121–126.

> Summarizing the item record purging requirements:
> 
> The system should provide a utility and reports for identifying item records
> to purge, based on customizable criteria such as:
> - An item has been in status "missing" for more than X months
> - An item has status "discard/weed"

### REQ-059 — Inactive Patrons with Fines Tracking

- Internal key: REQ-226422db6abcad9f3cb4f46f9ef39d15ad2680b11f8021bb63b6bc76675b568e
- Type: functional
- Priority: P2
- Priority basis: inferred
- Priority rationale: Separate handling of inactive accounts with outstanding fines affects financial and patron-account operations, but no explicit priority is supplied\.
- Originating candidates: CAND-2a70be31526eceaaf09300c8cd94ae2121dd968807211542caca1f1e6641545c

The system shall identify and track inactive patrons who still owe fines separately from other inactive patrons\.

Sources and evidence:

Source: [conversations/conv\_pines024\_inactive\_patrons\.eml](<../data/corpus/conversations/conv_pines024_inactive_patrons.eml>); document ID: DOC-705ab8a51bf22b7b619dae61bf8d2be1cf2487e749f13e7ac55fdde430357793; normalized lines 44–46.

> Also, should we flag patrons who are inactive but still owe fines? We
> should probably handle those differently\.
> 

Source: [conversations/conv\_pines024\_inactive\_patrons\.eml](<../data/corpus/conversations/conv_pines024_inactive_patrons.eml>); document ID: DOC-705ab8a51bf22b7b619dae61bf8d2be1cf2487e749f13e7ac55fdde430357793; normalized lines 140–141.

> - Track inactive patrons with outstanding fines separately
> - Allow exclusion of certain patron types

### REQ-060 — Deletion Reports by Scope and Criteria

- Internal key: REQ-22d99f9f29ddea2ba6dc1111c64c1e95ec393f943e42e56f85f9f2590a5a00eb
- Type: functional
- Priority: P2
- Priority basis: inferred
- Priority rationale: This supports operational oversight and investigation of deletion activity\.
- Originating candidates: CAND-9c52f6c79ce2ece8dba0511c945710b48d1f15f20beaab834054706322272f4f

The system shall provide reports showing deletions per location and per system, with aggregation by date range, user, and record type\.

Sources and evidence:

Source: [conversations/conv\_pines022\_deletions\.eml](<../data/corpus/conversations/conv_pines022_deletions.eml>); document ID: DOC-7b8da7c05931fc99bc80d4a4bb0c8563e690e0c415b57f5ca1ae394462dc26c8; normalized lines 43–44.

> The report should show deletions per location and per system\. We can
> aggregate by date range, by user, by record type\.

### REQ-061 — Circulations by Genre and Format Percentage-of-Total Metric

- Internal key: REQ-2300bcf8038e7ded85f55e018f5bcb974d53c5e40a931fafaa2e01e3de610d66
- Type: functional
- Priority: P2
- Priority basis: inferred
- Priority rationale: This supports collection-use analysis with a specified calculation basis\.
- Originating candidates: CAND-451e368af09b4f0999863202e1a0dea7ef9a2c2e4dbabfa3617262b7979fecba

The system shall sum checkouts or circulations by genre and format to produce the percentage-of-total-circulations metric\.

Sources and evidence:

Source: [conversations/conv\_pines016\_shelf\_space\.eml](<../data/corpus/conversations/conv_pines016_shelf_space.eml>); document ID: DOC-b507e8abe1ba7c996c1d86d688e90bcf2404694ec00528c8361f26dfc8bd82f1; normalized lines 66–69.

> From a data perspective, we need to:
> 1\. Count items per genre/format \(this is the "percentage of collection"\)
> 2\. Sum checkouts per genre/format \(this is the "percentage of circulations"\)
> 3\. Estimate shelf space per genre/format \(this is the "percentage of shelf space"\)

### REQ-062 — Patron-Characteristic Filters for Queries and Grouping

- Internal key: REQ-234b530eab753fc65bb8c02bc4f4a8c83b7df21636af1365b52df906e4376043
- Type: functional
- Priority: P2
- Priority basis: inferred
- Priority rationale: These dimensions are important for patron analysis and report segmentation\.
- Originating candidates: CAND-18940d55b2311d0b4d83cf089c9f6a1303f3964cda14363e3de1b305ed225f3e

The system shall allow queries and reports to be limited or grouped by patron age range, zip code, county of residence, home branch, patron type, and preferred language\.

Sources and evidence:

Source: [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>); document ID: DOC-091180de9b2d4ea83267d989411ac89f415d4def3bbf7cd51651fb7fda8d8bf9; normalized lines 397–406.

> 11\.1 Patron Characteristics
> Queries and reports can be limited or grouped by various patron characteristics,
> including:
>   - age range
>   - zip code
>   - county of residence
>   - home branch
>   - patron type
>   - preferred language
> 

### REQ-063 — Manual Title Selection for Item Transfers

- Internal key: REQ-24199549b50e10e76152e30aba2abf48577af8ef296fa73d4eeebb29afb56103
- Type: functional
- Priority: P2
- Priority basis: inferred
- Priority rationale: Manual selection provides operational control for item transfers, but no explicit priority is supplied\.
- Originating candidates: CAND-513284f7c6f23040d68eda7869715544e96a9816ade06e8e077338be94d5f995

The item transfer utility shall allow users to manually select titles from query results\.

Sources and evidence:

Source: [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>); document ID: DOC-091180de9b2d4ea83267d989411ac89f415d4def3bbf7cd51651fb7fda8d8bf9; normalized lines 359–362.

> The utility should include:
>   - Ability to query for candidate materials
>   - Ability to save queries for repeated use
>   - Ability to manually select titles from query results

### REQ-064 — Manually Select Titles from Query Results

- Internal key: REQ-24a38bf6f293220c6fdbfd62cedc381f5a594a32a919c1048fff680b2bd1d328
- Type: functional
- Priority: P3
- Priority basis: inferred
- Priority rationale: The source requests targeted selection but does not indicate that it is essential to core operation\.
- Originating candidates: CAND-bb0ea6a9f1a403fe1ec786606e3b6a4737ab5527e3e6d59315ba74205d8af4bd

The system shall allow users to manually select titles from query results so that users can target specific items\.

Sources and evidence:

Source: [interview\_cataloging\_2009-05-08\.txt](<../data/corpus/interview_cataloging_2009-05-08.txt>); document ID: DOC-a79fab45108210e6bce7d92153dfcf055f2ef6b2cdab49a3f6f5717a3e35f29f; normalized lines 50–51.

> manually select titles from query results if we want to be more targeted\.
> 

### REQ-065 — Detailed Voids Report

- Internal key: REQ-2575b458130a875a2f3aa3f2903d078f6ab5eb22cb1de3680189b30ac50c8d85
- Type: functional
- Priority: P3
- Priority basis: inferred
- Priority rationale: This is a useful specialized report and is not identified as essential to basic operation\.
- Originating candidates: CAND-a6a32ad9dad04495906a314aaf805acd9790c236fb16c3994bd292736d145560

The system shall provide a Detailed Voids report\.

Sources and evidence:

Source: [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>); document ID: DOC-091180de9b2d4ea83267d989411ac89f415d4def3bbf7cd51651fb7fda8d8bf9; normalized lines 585–585.

> - Detailed Voids

### REQ-066 — Local Admin Branch-Level Reporting and Configuration

- Internal key: REQ-258be826194ebfa112611c657f7ba15df59c1774ba05a615d240a909c94e7783
- Type: functional
- Priority: P2
- Priority basis: inferred
- Priority rationale: Branch-level administration is important for decentralized operations; the source does not assign a priority\.
- Originating candidates: CAND-ddef7bf56f650d087d2268ab1f42bbda89ba7c00dc85fe49396ba349230aff20

The system shall support a Local Admin role with branch-level reporting and configuration capabilities\.

Sources and evidence:

Source: [meeting\_tech\_subcommittee\_2009-06-30\.txt](<../data/corpus/meeting_tech_subcommittee_2009-06-30.txt>); document ID: DOC-e081aa7bd57bf5e59c75a8a86f592124757b74dff1ee0df4badc10c025092d96; normalized lines 69–70.

> - Local Admin: Branch-level reporting and configuration
> - Library Manager: Run approved reports, limited template modification

### REQ-067 — Payment Reports by Time and Method

- Internal key: REQ-26177571770f5142eedbee22e4bec89acff23a275da9ac3f082d3c22575179f4
- Type: functional
- Priority: P2
- Priority basis: inferred
- Priority rationale: Payment reporting supports financial reconciliation and operational accountability, but no explicit priority is supplied\.
- Originating candidates: CAND-5ce0d1e400764d5bf7de9beb9ed6999ed95bb5cd963c2dc304c1a72fc794eeda

The system shall provide reports of payments made by time period and payment method, including methods such as staff desk, self-check station, OPAC, cash, credit card, and check\.

Sources and evidence:

Source: [email\_financial\_reports\.eml](<../data/corpus/email_financial_reports.eml>); document ID: DOC-8b6cfb3cf368b794d82567933f9c85062740814819b1e28b4837f6021cbcbee6; normalized lines 19–20.

>    - Payments made per time period and per payment method \(staff desk,
>      self-check, OPAC\)

Source: [email\_financial\_reports\.eml](<../data/corpus/email_financial_reports.eml>); document ID: DOC-8b6cfb3cf368b794d82567933f9c85062740814819b1e28b4837f6021cbcbee6; normalized lines 71–72.

> - The financial reports need to show payments by method - cash, credit card,
>   check, etc\. This helps with daily reconciliation\.

Source: [email\_financial\_reports\.eml](<../data/corpus/email_financial_reports.eml>); document ID: DOC-8b6cfb3cf368b794d82567933f9c85062740814819b1e28b4837f6021cbcbee6; normalized lines 129–130.

>    - Payments made per time period and per payment method \(staff desk,
>      self-check station, OPAC\)

### REQ-068 — Separate Check-In Timestamp Reporting

- Internal key: REQ-262943d09c57181db20a03519ae9c661cf2ca6604fff253c417fbe263b0613b3
- Type: functional
- Priority: P2
- Priority basis: inferred
- Priority rationale: Accurate event reporting is important for operational records, but the source does not provide an explicit priority\.
- Originating candidates: CAND-253c14c36bffcbcaa58457ef151f9cb0351293fb57a1707cf846bdc855e0301a

The system shall report check-in dates and times separately from renewals and shall not include renewals in check-in date/time values\.

Sources and evidence:

Source: [survey\_results\_2009\.txt](<../data/corpus/survey_results_2009.txt>); document ID: DOC-aac7bceef7a883652805583e98ec513b6ae2e7951e2ecfa18722127b1f12a5c4; normalized lines 103–103.

>   - "Checkin date/time should not include renewals"

### REQ-069 — Historical Reporting via Reporting Warehouse by Date Range

- Internal key: REQ-262e4ae00b36db862a9ee8753879427865a3c136fafed0fe4c2691637dca76ab
- Type: functional
- Priority: P2
- Priority basis: inferred
- Priority rationale: Historical reporting supports longitudinal analysis and is explicitly identified as needed; the source does not assign a priority\.
- Originating candidates: CAND-e73112df4c4e1e104d9691ddaf67a7996e0f09e1b85cc72e61c7fed5d276b0de

The system shall support historical reporting through a reporting warehouse from which data can be acquired for a specified date or date range\.

Sources and evidence:

Source: [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>); document ID: DOC-091180de9b2d4ea83267d989411ac89f415d4def3bbf7cd51651fb7fda8d8bf9; normalized lines 656–657.

> - Ability to have historical reporting - a reporting warehouse such that data
>   can be acquired on a given date or date range

### REQ-070 — Real-Time and Historical Reporting Support

- Internal key: REQ-26c40fa365956e4272fc695a8371aae04ca3584ef6f957602cfb7061ae2d30bb
- Type: functional
- Priority: P2
- Priority basis: inferred
- Priority rationale: Both current-state and historical reporting support important operational and management decisions; the source does not establish a critical priority\.
- Originating candidates: CAND-c6141814d98fe5b0a8f0ba46201ae3cb8b8711b5346ffd046fcb2479d1301195

The reporting capability shall support real-time reporting for current states \(for example, what is overdue today\) and shall support historical reporting for past points in time; the provided source suggests that a reporting warehouse may be needed for historical data but this implementation is not established as mandatory by the requirement\.

Sources and evidence:

Source: [meeting\_tech\_subcommittee\_2009-06-30\.txt](<../data/corpus/meeting_tech_subcommittee_2009-06-30.txt>); document ID: DOC-e081aa7bd57bf5e59c75a8a86f592124757b74dff1ee0df4badc10c025092d96; normalized lines 167–171.

> 5\.2 REAL-TIME vs HISTORICAL REPORTING
> "Some reports need to be real-time - like 'what's overdue today,'" Robert said\.
> "Others are historical - 'what was the bill amount on June 30th?' We probably
> need a reporting warehouse for historical data\."
> 

### REQ-071 — Report Inactive Patrons by Organizational Level

- Internal key: REQ-26e9b5d56720d9ade801e5aff799b889cd990d00147524e131e7aacbbf7bc817
- Type: functional
- Priority: P2
- Priority basis: inferred
- Priority rationale: The capability supports branch-level cleanup management and system-wide prioritization, but the source does not assign an explicit priority\.
- Originating candidates: CAND-b80c7a667f93d247ba5f74eea78e6986f4b2331bbc8241a0937f3c9dfb06590c

The system shall allow the report to be viewed at the System level to identify which branches have the most inactive patrons and at the Home Library level to provide lists usable for assigning cleanup tasks to specific branches\.

Sources and evidence:

Source: [conversations/conv\_pines024\_inactive\_patrons\.eml](<../data/corpus/conversations/conv_pines024_inactive_patrons.eml>); document ID: DOC-705ab8a51bf22b7b619dae61bf8d2be1cf2487e749f13e7ac55fdde430357793; normalized lines 22–24.

> For the configurable levels - I'd want System and Home Library\. At the
> system level, I can see which branches have the most inactive patrons\.
> At the home library level, I can assign cleanup tasks to specific branches\.

### REQ-072 — Export Reports in Excel, HTML, and CSV Formats

- Internal key: REQ-26ec0f186e788c756d098aa0a72bf088cb9b9e08c9a8b73d3e1e19de8b9eef88
- Type: functional
- Priority: P2
- Priority basis: inferred
- Priority rationale: Inferred as important reporting interoperability functionality; no explicit source priority is supplied\.
- Originating candidates: CAND-71fd9dc7bf25f15245653567b30a00349a3e085c4188a4c2665ceee72f27ebbb

The system shall support report export or output in Excel, HTML, and CSV formats\.

Sources and evidence:

Source: [meeting\_tech\_subcommittee\_2009-06-30\.txt](<../data/corpus/meeting_tech_subcommittee_2009-06-30.txt>); document ID: DOC-e081aa7bd57bf5e59c75a8a86f592124757b74dff1ee0df4badc10c025092d96; normalized lines 162–165.

> 5\.1 OUTPUT FORMATS
> Excel, HTML, and CSV formats are required\. Robert noted that CSV is the most
> reliable for data export, Excel is preferred by business users for pivot tables,
> and HTML is needed for web display\.

### REQ-073 — Patron exclusion filters for reports

- Internal key: REQ-2718971e8588d933e255e76ac2d68a8c5bc0cca599cf883e8f9e95af52156d82
- Type: functional
- Priority: P2
- Priority basis: inferred
- Priority rationale: Exclusion controls protect patron preferences and support appropriate report use; the source does not establish a more specific priority\.
- Originating candidates: CAND-8d42b838447f80ffe8cc776bca106392a12014ef06a61e58c2c906efd9b8ae42

The report shall provide exclusion filters that allow specified patrons to be excluded, including patrons with do-not-disturb flags, VIP patrons, staff members, and patrons who have opted out of communications\.

Sources and evidence:

Source: [conversations/conv\_pines024\_inactive\_patrons\.eml](<../data/corpus/conversations/conv_pines024_inactive_patrons.eml>); document ID: DOC-705ab8a51bf22b7b619dae61bf8d2be1cf2487e749f13e7ac55fdde430357793; normalized lines 110–116.

> One more thing - we should be able to EXCLUDE certain patrons from the
> inactive report\. For example:
> - Patrons with "do not disturb" flags
> - VIP patrons
> - Staff members
> - Patrons who have opted out of communications
> 

Source: [conversations/conv\_pines024\_inactive\_patrons\.eml](<../data/corpus/conversations/conv_pines024_inactive_patrons.eml>); document ID: DOC-705ab8a51bf22b7b619dae61bf8d2be1cf2487e749f13e7ac55fdde430357793; normalized lines 141–141.

> - Allow exclusion of certain patron types

### REQ-074 — Patron Demographic and Interest Reporting

- Internal key: REQ-279724ab69bc0d638d84fc9089b9a9ca3a21a9c871565f6e55936a2e5a953c58
- Type: functional
- Priority: P3
- Priority basis: inferred
- Priority rationale: This supports useful analysis but is not identified as essential to basic operation\.
- Originating candidates: CAND-60dadb8062c1e2de076b05f5433c60e27baf7d8f133d0a9daeb1a437e6c9be95

The system shall provide reporting and analysis capabilities for patron demographics and interests\.

Sources and evidence:

Source: [meeting\_minutes/meeting\_2009-03-15\_minutes\.txt](<../data/corpus/meeting_minutes/meeting_2009-03-15_minutes.txt>); document ID: DOC-defef992db2ae0e10167fd94902eac93f82c59c4c070df030ca2f77811082818; normalized lines 61–61.

>   - Analyzing demographics and interests of patrons

### REQ-075 — Patron Payment Audit Ledger

- Internal key: REQ-27cc9512436bfa663fc1b96d788ece69cc7d845f2e852c2eadf1e0aa42859291
- Type: functional
- Priority: P1
- Priority basis: inferred
- Priority rationale: Financial reconciliation and auditability are core payment controls\.
- Originating candidates: CAND-d69e39e1039b4090a0f926bcead7974b5ebd2827f174d281313bf5a8b47bc9fe

The system shall maintain a financial audit ledger of patron payments that records which charges each payment is applied to, to facilitate reconciliation\.

Sources and evidence:

Source: [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>); document ID: DOC-091180de9b2d4ea83267d989411ac89f415d4def3bbf7cd51651fb7fda8d8bf9; normalized lines 483–485.

> 13\.5 Financial Audit Trail
> The system maintains a ledger of patron payments, including which charges
> payments are applied to, to facilitate reconciliation\.

### REQ-076 — Management Process Data Specifications

- Internal key: REQ-27d474f2bac7a0762149523421b16972fc4b40b653ea9758dc128184eb3da09f
- Type: nonfunctional
- Priority: P2
- Priority basis: inferred
- Priority rationale: Complete data specifications support implementation and verification of important system functionality; no explicit source priority is provided\.
- Originating candidates: CAND-ed9641d456143ab968495db7ebff977a362658fbfb083c72630d9a4b0d5182c0

The developer shall provide complete data specifications for authority, bibliographic, order, item, hold/request, and other records maintained or accessed by Management Processes\.

Sources and evidence:

Source: [meeting\_tech\_subcommittee\_2009-06-30\.txt](<../data/corpus/meeting_tech_subcommittee_2009-06-30.txt>); document ID: DOC-e081aa7bd57bf5e59c75a8a86f592124757b74dff1ee0df4badc10c025092d96; normalized lines 83–90.

> 3\.1 DATA SPECIFICATIONS
> The developer must provide complete data specifications for:
> - Authority records
> - Bibliographic records
> - Order records
> - Item records
> - Hold/request records
> - Other records maintained or accessed by Management Processes

### REQ-077 — Patron Report Filtering and Aggregation

- Internal key: REQ-286c5a869b7870b652c4fa583d39628483ffaab45f98cf74f310c163143f7f45
- Type: functional
- Priority: P2
- Priority basis: inferred
- Priority rationale: Important capabilities for producing usable patron reports\.
- Originating candidates: CAND-d31bf409015246295898c44e0976f4ae015f0928934685591e6f00cdd3bcf030

The system shall support LIMIT filtering and GROUP BY aggregation for patron reports\.

Sources and evidence:

Source: [conversations/conv\_pines023\_patron\_characteristics\.eml](<../data/corpus/conversations/conv_pines023_patron_characteristics.eml>); document ID: DOC-d2b26a6e7678ca4e82bfa7bb06566f329dea692ea22e8987b516fa8bc98c544b; normalized lines 119–121.

> - Both LIMIT \(filter\) and GROUP BY \(aggregate\) should be supported
> - Filters can be combined with AND/OR logic
> - Null values should be included in results

### REQ-078 — Group Reports by Patron Characteristics

- Internal key: REQ-29c4b814561f3df4373983fae140f570aa3ac86f726e88ac56bcf8c72c750702
- Type: functional
- Priority: P2
- Priority basis: inferred
- Priority rationale: Inferred as high priority because the evidence explicitly requires grouping by the listed patron characteristics\.
- Originating candidates: CAND-7e450a7847586de3f40f3f805e7d1bf61eab75d0008424b16872024b182e1e85

The system shall allow queries and reports to be grouped by patron characteristics including age range, zip code, county of residence, home branch, patron type, and preferred language\.

Sources and evidence:

Source: [conversations/conv\_pines023\_patron\_characteristics\.eml](<../data/corpus/conversations/conv_pines023_patron_characteristics.eml>); document ID: DOC-d2b26a6e7678ca4e82bfa7bb06566f329dea692ea22e8987b516fa8bc98c544b; normalized lines 109–121.

> The system should allow queries and reports to be limited or grouped by
> various patron characteristics, including:
> - Age range
> - Zip code
> - County of residence
> - Home branch
> - Patron type
> - Preferred language
> 
> Key points:
> - Both LIMIT \(filter\) and GROUP BY \(aggregate\) should be supported
> - Filters can be combined with AND/OR logic
> - Null values should be included in results

### REQ-079 — Role-Based Staff Permissions at Login

- Internal key: REQ-29e2133460b5f10eb2fc01616feb60b47b529b3a23e45564406967e3cf848384
- Type: functional
- Priority: P1
- Priority basis: inferred
- Priority rationale: Authorization at login is essential to security and access control, so it is critical under the supplied priority scale\.
- Originating candidates: CAND-e2fb31d228e8ece8e3a7e46c0d8553337222b4c7e9181b9b8209560325e5e146

When a staff member logs in by any method, the system shall determine the staff member's permissions from the assigned security group or role\.

Sources and evidence:

Source: [email\_staff\_login\.eml](<../data/corpus/email_staff_login.eml>); document ID: DOC-64b10e94c42508c5aea1af877ec9d2fe34485b099b29994b8b1a76cadc55e8b3; normalized lines 49–51.

> the login requirement - when a staff member logs in \(by any method\), their
> permissions should be determined by their assigned security group/role\.
> Administrators should be able to create and manage these groups\.

### REQ-080 — Document Major Processes and Standard Reports

- Internal key: REQ-29e59c70f4114d2d61a2625aa91cff01d28a4d1fb10ed048842b07b922af32f0
- Type: nonfunctional
- Priority: P2
- Priority basis: inferred
- Priority rationale: The requirement specifies developer documentation needed to describe major system processes\.
- Originating candidates: CAND-3e8af1e576bd07fa9a6c08a56b861662f98bca9aafef437000d8ee817dab9a5e

The developer shall provide a high-level description of major processes, including bibliographic record import and export, validation against internal and external authority sources, and standard reports\.

Sources and evidence:

Source: [meeting\_tech\_subcommittee\_2009-06-30\.txt](<../data/corpus/meeting_tech_subcommittee_2009-06-30.txt>); document ID: DOC-e081aa7bd57bf5e59c75a8a86f592124757b74dff1ee0df4badc10c025092d96; normalized lines 95–102.

> 3\.2 PROCESS DESCRIPTIONS
> The developer must provide a thorough high-level description of major processes,
> including:
> - Bibliographic record import and export
> - Validation of bibliographic records against internal and external authority
>   sources
> - Standard reports
> 

### REQ-081 — Non-Disruptive Report Processing

- Internal key: REQ-2a34a6ca032b3f61e6310bf246589b4aaae1403d54a7c9f4d1cd903d1176acac
- Type: nonfunctional
- Priority: P1
- Priority basis: inferred
- Priority rationale: Protecting normal operations during open hours is essential to service continuity; no explicit source priority is provided\.
- Originating candidates: CAND-ec7dd567916e089c22a612cbecef7342ca89343549fc3e24a7670de7b36e14dc

The system shall process searches and reports during open hours without disrupting other system functions, including during peak times\.

Sources and evidence:

Source: [interview\_sysadmin\_2009-05-10\.txt](<../data/corpus/interview_sysadmin_2009-05-10.txt>); document ID: DOC-b1738fd7a6de9498f19ede6747ba156ecb29ead86ad1c9a2768b53e862ece1a9; normalized lines 41–44.

> need to make sure reports can be queued and processed in the background\. Or we
> need read-only reporting replicas\. The key requirement is that searches and
> reports can be processed during open hours without disrupting other system
> functions\.

### REQ-082 — Legacy Browser Support for IE and Firefox

- Internal key: REQ-2abde3d3fc149f3792ee098af3876d9a6f6ddf7dcad59c12b745af4715467273
- Type: nonfunctional
- Priority: P3
- Priority basis: explicitly specified
- Priority rationale: The review identifies browser compatibility as Medium Priority, which maps to P3; this priority is explicit in the supplied review feedback\.
- Originating candidates: CAND-694dd7331a22c4a9248dcea707d3fad37b520aa29f54055e88832fdf9298c0aa

The system shall support Microsoft Internet Explorer 6\.0 and newer and Firefox 2\.0 and newer\.

Sources and evidence:

Source: [interview\_sysadmin\_2009-05-10\.txt](<../data/corpus/interview_sysadmin_2009-05-10.txt>); document ID: DOC-b1738fd7a6de9498f19ede6747ba156ecb29ead86ad1c9a2768b53e862ece1a9; normalized lines 48–52.

> ROBERT: It's a mixed bag\. Most of our libraries standardize on Microsoft
> Internet Explorer, but many have moved to Firefox\. IE 6 is still common in
> our environment - I know it's old, but upgrading browsers on 200\+ library
> computers is expensive and time-consuming\. Firefox 2\.0 is also still in use
> at some locations\. So we need to support IE 6\.0\+ and Firefox 2\.0\+\.

### REQ-083 — High-Level Major Process Description

- Internal key: REQ-2b20da6ffe2e5d2f5ac0d476581e05654ddab0be0c7819c933c133557ec2c095
- Type: nonfunctional
- Priority: P3
- Priority basis: inferred
- Priority rationale: Documentation is useful for delivery and maintenance but is not itself essential to runtime operation; no explicit source priority is provided\.
- Originating candidates: CAND-f0404cbb13127656a1cf20e19e54cd6d0cb0176996f9bfaabb5afe358b6d74ad, CAND-fb67462b82ce634ccb46ff2a4be799937873bd3257803d9c0527b319b13e2b84

The software developer shall provide a thorough high-level description of major processes, including bibliographic record import and export, validation of bibliographic records against internal and external authority sources, and standard reports\.

Sources and evidence:

Source: [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>); document ID: DOC-091180de9b2d4ea83267d989411ac89f415d4def3bbf7cd51651fb7fda8d8bf9; normalized lines 182–185.

> UD-2: The developer must provide a thorough high-level description of major
>       processes, including bibliographic record import and export, validation
>       of bibliographic records against internal and external authority sources,
>       and standard reports\.

Source: [meeting\_minutes/meeting\_2009-07-20\_minutes\.txt](<../data/corpus/meeting_minutes/meeting_2009-07-20_minutes.txt>); document ID: DOC-5ab1dd8bc97af3b1ab2e378495f0e0d75fd501fcc19f923c0d8fda831074281b; normalized lines 144–147.

> UD-2: The software developer shall provide a thorough high-level description
>       of major processes, including bibliographic record import and export,
>       validation of bibliographic records against internal and external
>       authority sources, and standard reports\.

### REQ-084 — Cataloged In-House Use Count Report

- Internal key: REQ-2b59c53f90acb3288b70f7f08af14dac9ce88284fc392695bf5a211e6267a09b
- Type: functional
- Priority: P3
- Priority basis: inferred
- Priority rationale: This is a useful specific report and is not identified as essential to core operation\.
- Originating candidates: CAND-9611f851f8d14d9faab8c48ac0c624980d4ab2848fb112d7f63845c04b735a95

The system shall provide a Cataloged In-House Use Count report\.

Sources and evidence:

Source: [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>); document ID: DOC-091180de9b2d4ea83267d989411ac89f415d4def3bbf7cd51651fb7fda8d8bf9; normalized lines 575–575.

> - Cataloged In House Use Count

### REQ-085 — Compatibility with Existing PostgreSQL Database

- Internal key: REQ-2c377ae15450567ec55b3d92f63445302a6fa60279f2e1bd7b924f3e0684e7d8
- Type: nonfunctional
- Priority: P2
- Priority basis: inferred
- Priority rationale: Compatibility with the existing relational database structure is important to operating the reporting system in the stated environment; the supplied evidence does not establish PostgreSQL 8\.3 as a mandatory version constraint\.
- Originating candidates: CAND-1e24e587c59c6661c57067e6ccd780ded1ebc6669917891dadd951cfcc32b8b9

The reporting system shall operate with the existing PostgreSQL relational database structure\.

Sources and evidence:

Source: [interview\_sysadmin\_2009-05-10\.txt](<../data/corpus/interview_sysadmin_2009-05-10.txt>); document ID: DOC-b1738fd7a6de9498f19ede6747ba156ecb29ead86ad1c9a2768b53e862ece1a9; normalized lines 31–33.

> ROBERT: Our main server is a Red Hat Enterprise Linux 5 box with dual quad-core
> processors and 32GB of RAM\. It runs PostgreSQL 8\.3 for the database\. We also
> have a secondary site that runs Solaris 10 on SPARC hardware for disaster

Source: [interview\_sysadmin\_2009-05-10\.txt](<../data/corpus/interview_sysadmin_2009-05-10.txt>); document ID: DOC-b1738fd7a6de9498f19ede6747ba156ecb29ead86ad1c9a2768b53e862ece1a9; normalized lines 68–72.

> ROBERT: We're using PostgreSQL now, which is a fully relational database\.
> That's good - it means we can write complex joins\. The reporting system needs
> to work with the relational structure, not fight against it\. Some systems try
> to use denormalized reporting schemas, but that creates sync issues\. I'd
> prefer to keep everything in the main relational database\.

### REQ-086 — Data Quality Reports for Invalid or Missing Data

- Internal key: REQ-2c734477c16b9da1697067852b5c63069c087a75a0a5c6389f0cb3ac783cb4ea
- Type: functional
- Priority: P2
- Priority basis: inferred
- Priority rationale: These reports support maintenance of data integrity and have substantial operational impact\.
- Originating candidates: CAND-9d3ffb182d868c5a797e4d73f942ee6e8cd15de363fa4669d02f0fa63b32cdbf

The system shall provide data quality reports identifying items with invalid item types, items with excessively long call numbers, and bibliographic records with no item records\.

Sources and evidence:

Source: [interview\_cataloging\_2009-05-08\.txt](<../data/corpus/interview_cataloging_2009-05-08.txt>); document ID: DOC-a79fab45108210e6bce7d92153dfcf055f2ef6b2cdab49a3f6f5717a3e35f29f; normalized lines 112–114.

> 3\. Data quality reports - items with invalid item type, items with long call
>    numbers, bibliographic records with no item records\. These help me maintain
>    data integrity\.

### REQ-087 — Accessible Reporting Interface Compliance

- Internal key: REQ-2d6d7027d970d64ac8b668881cbfdffe97ee8238e57666edd6313965aa981791
- Type: nonfunctional
- Priority: P1
- Priority basis: inferred
- Priority rationale: Accessibility compliance is a stated requirement, and mandatory compliance is critical under the priority scale\.
- Originating candidates: CAND-bb3152cacd82ed2b60616520472f537544339d2e56077b4d1211f25a44f9f82d

The reporting interface shall comply with applicable accessibility requirements\.

Sources and evidence:

Source: [evergreen\_reference\_2009\.txt](<../data/corpus/evergreen_reference_2009.txt>); document ID: DOC-e6aa9f8c6308ab748459f87b578a0df9df9c865b7911bac3686e865963b7af6f; normalized lines 218–218.

> 5\. Implement accessibility compliance

### REQ-088 — Overall Report Totals Including Total Library Items

- Internal key: REQ-2d7565d050f266ba2d57fbc8de84f46aab2b4515a8744c3d87a07e77532b2778
- Type: functional
- Priority: P2
- Priority basis: inferred
- Priority rationale: Inferred as important reporting functionality; no explicit source priority is supplied\.
- Originating candidates: CAND-6b8a3978207838c5ae4ae42703c6c421672d3c6d481c1a8e8ef81c23793d933b

The system shall include overall totals in reports, including the total number of items in the library\.

Sources and evidence:

Source: [conversations/conv\_pines014\_material\_volume\.eml](<../data/corpus/conversations/conv_pines014_material_volume.eml>); document ID: DOC-f10d646016479a881ae8ff4ab4043844ee55a671d71f1943623db3fbb5589d8a; normalized lines 3–6.

> Quick question - how do I get a report that tells me how many items we have
> at Dalton-Whitman at any given moment? Not just total count, but broken down
> by categories\. Like total items in library, number of holds, number of adult
> fiction, number of board books\.\.\.

Source: [conversations/conv\_pines014\_material\_volume\.eml](<../data/corpus/conversations/conv_pines014_material_volume.eml>); document ID: DOC-f10d646016479a881ae8ff4ab4043844ee55a671d71f1943623db3fbb5589d8a; normalized lines 98–99.

> - Total items in library
> - Number of holds

### REQ-089 — Management Process Data Specifications for Managed/Accessed Records

- Internal key: REQ-2e5b3f3719980a9e0e3981b2727a9c3c0b57b1efe7e39a23ccd5e3ed0ac5507b
- Type: nonfunctional
- Priority: P2
- Priority basis: explicitly specified
- Priority rationale: The source marks this documentation requirement as high priority\.
- Originating candidates: CAND-45e6c8a56b7d685969e4e7d566f32c4faf4a433148a29b93ed59c83bebe186ab

The developer shall provide complete data specifications for authority records, bibliographic records, order records, item records, hold or request records, and other records maintained or accessed by the Management Processes\.

Sources and evidence:

Source: [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>); document ID: DOC-091180de9b2d4ea83267d989411ac89f415d4def3bbf7cd51651fb7fda8d8bf9; normalized lines 176–179.

> UD-1: The developer must provide complete data specifications for authority
>       records, bibliographic records, order records, item records, hold/request
>       records, and other records maintained or accessed by the Management
>       Processes\.

### REQ-090 — Item Use Counts by Date Range

- Internal key: REQ-2f0b2a4e587a13a0d36c20cc5a8b7d27dc301b4759455c4873f00a8a0da0b1c9
- Type: functional
- Priority: P2
- Priority basis: inferred
- Priority rationale: Usage reporting supports collection management, but the source does not assign a formal priority level\.
- Originating candidates: CAND-0cd068b39f1827d787a7f3d37546305bcbe3d5a6dcb80b25c2375c0c238d77e8

The system shall provide item use counts, including total use counts and use counts broken down by a usage date range such as a fiscal year or month\.

Sources and evidence:

Source: [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>); document ID: DOC-091180de9b2d4ea83267d989411ac89f415d4def3bbf7cd51651fb7fda8d8bf9; normalized lines 642–643.

> - Ability to have a total use count on items as well as a use count broken down
>   by usage date range such as an FY use count or monthly use count

### REQ-091 — Local system administrator local configuration

- Internal key: REQ-2f233809631a3784fa8f496f33d69b9e5670375ac95f57e54eb631bca2327fe9
- Type: functional
- Priority: P2
- Priority basis: inferred
- Priority rationale: Local configuration is important to branch and library administration; the source does not establish a more specific priority\.
- Originating candidates: CAND-8ae508337d91d13e0e2b5e565e1e20dd9a335c2087cf4788ff9bdb8a8f92211b

The system shall provide Local System Administrators with the ability to configure the system locally\.

Sources and evidence:

Source: [meeting\_minutes/meeting\_2009-03-15\_minutes\.txt](<../data/corpus/meeting_minutes/meeting_2009-03-15_minutes.txt>); document ID: DOC-defef992db2ae0e10167fd94902eac93f82c59c4c070df030ca2f77811082818; normalized lines 92–95.

>   Local System Administrators: Management staff who oversee Library processes\.
>                                 They configure the system locally\.
>                                 \[Susan: These are branch managers / assistant
>                                 directors\]

### REQ-092 — Integrated Online Hierarchical HTML Help for System Functions

- Internal key: REQ-2f9d588489198ee3df69cd29804622656d27de492ddf4ca53b2b3304ed5d47ee
- Type: nonfunctional
- Priority: P2
- Priority basis: explicitly specified
- Priority rationale: The source explicitly marks the online help requirement as High Priority; under the supplied priority scale, High Priority maps to P2\.
- Originating candidates: CAND-12f84f0d7c3b77bad76223c56690c0652f94edbd0612d9cc927e047a9e2fdb7a, CAND-5f7f363b71f413c56dd01778e709803ac4fdb5489e2948765109f021f164564b, CAND-6d2d3a69800ac11cb523b8b50d3d183cc4e5272c6987aaf059fbf29d7411bdb8, CAND-8ecc856417c12f521731dfb71943884d8e92e580a2921a44499eec767f7c1c19, CAND-93788a162aa928e99d3f586f49037960838a578c3b127910a6401f57cecc4b95

The system shall provide an online, hierarchical, cross-linked help system in HTML that describes and illustrates all system functions, is searchable, is easy to navigate, and is integrated with the reports interface\.

Sources and evidence:

Source: [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>); document ID: DOC-091180de9b2d4ea83267d989411ac89f415d4def3bbf7cd51651fb7fda8d8bf9; normalized lines 188–190.

> UD-3: The system must provide an online, hierarchical, and cross-linked help
>       system in HTML that describes and illustrates all system functions\.
>       \[\* High Priority\]

Source: [evergreen\_reference\_2009\.txt](<../data/corpus/evergreen_reference_2009.txt>); document ID: DOC-e6aa9f8c6308ab748459f87b578a0df9df9c865b7911bac3686e865963b7af6f; normalized lines 189–189.

> - No online help system integrated with reports

Source: [interview\_sysadmin\_2009-05-10\.txt](<../data/corpus/interview_sysadmin_2009-05-10.txt>); document ID: DOC-b1738fd7a6de9498f19ede6747ba156ecb29ead86ad1c9a2768b53e862ece1a9; normalized lines 106–108.

> Also, the help system needs to be online, hierarchical, and cross-linked\.
> Staff shouldn't have to call IT every time they want to know how to run a
> report\. The HTML help needs to be searchable and easy to navigate\.

Source: [meeting\_minutes/meeting\_2009-07-20\_minutes\.txt](<../data/corpus/meeting_minutes/meeting_2009-07-20_minutes.txt>); document ID: DOC-5ab1dd8bc97af3b1ab2e378495f0e0d75fd501fcc19f923c0d8fda831074281b; normalized lines 152–156.

> UD-3: The system shall provide an online, hierarchical, and cross-linked help
>       system in HTML that describes and illustrates all system functions\.
> 
>       \[Discussion: Context-sensitive help is critical\. Staff shouldn't have
>       to leave the system to find documentation\.\]

Source: [meeting\_tech\_subcommittee\_2009-06-30\.txt](<../data/corpus/meeting_tech_subcommittee_2009-06-30.txt>); document ID: DOC-e081aa7bd57bf5e59c75a8a86f592124757b74dff1ee0df4badc10c025092d96; normalized lines 103–106.

> 3\.3 ONLINE HELP SYSTEM
> The system shall provide an online, hierarchical, and cross-linked help system
> in HTML\.
> 

### REQ-093 — Custom Local Reports

- Internal key: REQ-2fa5c45c1afcb2d8ef921cd1868fc04a1c1a7aa4b18908f1be005bce3debfc56
- Type: functional
- Priority: P3
- Priority basis: inferred
- Priority rationale: These reports support local staff activities but are not identified as essential for basic system operation\.
- Originating candidates: CAND-2a25edb11d5b427c5c90666e206bb433c459facee8f85ea23156761b154b23de

The system shall support custom or local reports, including collection development reports, program attendance tracking, and staff productivity reports\.

Sources and evidence:

Source: [survey\_results\_2009\.txt](<../data/corpus/survey_results_2009.txt>); document ID: DOC-aac7bceef7a883652805583e98ec513b6ae2e7951e2ecfa18722127b1f12a5c4; normalized lines 77–83.

> QUESTION 7: "Do you use any custom or local reports?"
>   - Yes: 38%
>   - No: 62%
>   Among those who use custom reports, the most common are:
>   - Collection development reports
>   - Program attendance tracking
>   - Staff productivity reports \(time spent per transaction\)

### REQ-094 — Immediately Updatable Financial Information

- Internal key: REQ-30ef99ab0e984fab20b5d47a4dd43b43319cf24f0746ee4910c420df76b99c92
- Type: nonfunctional
- Priority: P2
- Priority basis: inferred
- Priority rationale: Timely and usable financial updates materially affect front-desk operations and account accuracy\.
- Originating candidates: CAND-9f018efc5c88627cbc3659dcc9e04f9f9380795405eb72c2f48cda3bfa32d7ad

The system shall allow staff users to update financial information easily, and shall reflect changes such as patron payments immediately\.

Sources and evidence:

Source: [email\_financial\_reports\.eml](<../data/corpus/email_financial_reports.eml>); document ID: DOC-8b6cfb3cf368b794d82567933f9c85062740814819b1e28b4837f6021cbcbee6; normalized lines 89–91.

> - Financial information needs to be easily updatable\. When a patron makes a
>   payment at the front desk, we need the system to reflect that immediately\.
> 

Source: [email\_financial\_reports\.eml](<../data/corpus/email_financial_reports.eml>); document ID: DOC-8b6cfb3cf368b794d82567933f9c85062740814819b1e28b4837f6021cbcbee6; normalized lines 119–121.

>    Financial information can be updated easily\. A staff user can easily query
>    patron accounts with balances greater than X dollars\.
> 

### REQ-095 — Stale Holds Report

- Internal key: REQ-32c1a6f5a798d7817741962e04e0fd75676bba88896506bb9f53699659445f3e
- Type: functional
- Priority: P2
- Priority basis: inferred
- Priority rationale: Stale-hold reporting supports important hold management, while the source does not define a duration threshold\.
- Originating candidates: CAND-1eb2be6e31853b5d2690b1d4440db9098424b99c11c54b6233099aabbeee403f

The system shall provide a report of holds that have remained on the hold shelf waiting for pickup for too long\.

Sources and evidence:

Source: [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>); document ID: DOC-091180de9b2d4ea83267d989411ac89f415d4def3bbf7cd51651fb7fda8d8bf9; normalized lines 571–571.

> - Stale Holds \(holds sitting on hold shelf waiting for pickup for too long\)

### REQ-096 — Staff Role for Running Reports Within Assigned Permissions

- Internal key: REQ-333a244430151ec3ce30f53536237448bfacc5b35b20b31c71ab9482c30f6b79
- Type: functional
- Priority: P2
- Priority basis: inferred
- Priority rationale: Staff reporting access is important functionality, but the source does not assign a formal priority level\.
- Originating candidates: CAND-06a2fbeb406f29ddb0592cd5d0b6e33368dc54f0ff91c110c6770b2fc5b8986d

The system shall provide a Staff role that can run reports within assigned permissions\.

Sources and evidence:

Source: [meeting\_tech\_subcommittee\_2009-06-30\.txt](<../data/corpus/meeting_tech_subcommittee_2009-06-30.txt>); document ID: DOC-e081aa7bd57bf5e59c75a8a86f592124757b74dff1ee0df4badc10c025092d96; normalized lines 71–71.

> - Staff: Run reports within assigned permissions

### REQ-097 — Cancel Scheduled or Running Reports

- Internal key: REQ-342f3a69f00fab04f26b49133990668495d3564788200c918993798de90fe495
- Type: functional
- Priority: P2
- Priority basis: inferred
- Priority rationale: Cancellation supports control of report execution and resource use, but no explicit priority is supplied\.
- Originating candidates: CAND-49907d16099c747de7c369ac72a2d06e02104762b0f9bbbac5bd4b5ab1480362, CAND-54c5e09b3c32679ee73dbbc10673c654f92416e11f5b16d9daed8ade76966dbf

The system shall allow users to cancel a scheduled or currently running report and shall check for cancellation signals during report processing\.

Sources and evidence:

Source: [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>); document ID: DOC-091180de9b2d4ea83267d989411ac89f415d4def3bbf7cd51651fb7fda8d8bf9; normalized lines 651–652.

> - Ability to cancel a report that has already been scheduled to run or is
>   currently running

Source: [meeting\_tech\_subcommittee\_2009-06-30\.txt](<../data/corpus/meeting_tech_subcommittee_2009-06-30.txt>); document ID: DOC-e081aa7bd57bf5e59c75a8a86f592124757b74dff1ee0df4badc10c025092d96; normalized lines 172–176.

> 5\.3 REPORT CANCELLATION
> The ability to cancel a scheduled or running report is technically feasible,
> but requires the system to check for cancellation signals during report
> processing\.
> 

### REQ-098 — Support Defined Reporting User Classes

- Internal key: REQ-34659944a82365513d0dd1846a4afdd53bc62048c1c0f107bd731c46aee40e28
- Type: functional
- Priority: P2
- Priority basis: inferred
- Priority rationale: The defined user classes establish the audiences and access needs for the reporting system and are important to its operation, but the source does not identify them as critical or mandatory compliance controls\.
- Originating candidates: CAND-a83bf47f7f6aa94e2c174ae11a8639be1e6735baa3d1767abf2f06d2b068c796

The reporting system shall support the following user classes: Patron, Staff, Local System Administrators, Library Managers, Library Directors, and Global System Administrator, addressing the responsibilities and needs of each role\.

Sources and evidence:

Source: [meeting\_minutes/meeting\_2009-03-15\_minutes\.txt](<../data/corpus/meeting_minutes/meeting_2009-03-15_minutes.txt>); document ID: DOC-defef992db2ae0e10167fd94902eac93f82c59c4c070df030ca2f77811082818; normalized lines 77–110.

> 4\. USER CLASSES AND CHARACTERISTICS
> --------------------------------------------------------------------------------
> The group discussed the different types of users who would interact with
> Management Processes:
> 
>   Patron: A resident of the State of Georgia, either possessing a library card
>           or not, utilizing the resources of a PINES member library\.
>           \[Note from Katherine: Patrons interact through OPAC; they may use
>           reports indirectly through displays/screens at libraries\]
> 
>   Staff: Paid employees of PINES member libraries involved in designing and
>          providing services\. This includes front-line circulation staff,
>          supervisors, etc\.
>          \[Jenny: Staff are our primary content creators for reports\]
> 
>   Local System Administrators: Management staff who oversee Library processes\.
>                                 They configure the system locally\.
>                                 \[Susan: These are branch managers / assistant
>                                 directors\]
> 
>   Library Managers: Supervise a single organizational unit and provide input to
>                    design and implementation of Library services\.
>                    \[LaToya: Directors and assistant directors in this role\]
> 
>   Library Directors: Members of the Library Executive Team who plan and direct
>                      Library services and priorities\.
>                      \[George: These are our board-level stakeholders\]
> 
>   Global System Administrator: Manages PINES at the consortium level,
>                                implementing software changes and configurations,
>                                and generating statistical reports for PINES as
>                                a whole\.
>                                \[Katherine: This is the PINES central IT team\]
> 

### REQ-099 — Missing and Damaged Reports with Date Filtering

- Internal key: REQ-34a1eaa1900a594cac5cddf13c714446576eeb94b38765a0355143c101731d7b
- Type: functional
- Priority: P3
- Priority basis: inferred
- Priority rationale: Date-range trending is useful reporting analysis but is not shown to be essential to basic operation; no explicit source priority is provided\.
- Originating candidates: CAND-ea1b01fdd99d1e6192c5ad85e8695295da619a1d79c905196004279917ef9048

The missing and damaged report shall support date-range filtering, including ranges such as the last 30 days and last quarter, to support trending\.

Sources and evidence:

Source: [conversations/conv\_pines019\_020\_missing\_intransit\.eml](<../data/corpus/conversations/conv_pines019_020_missing_intransit.eml>); document ID: DOC-b233b12122cae48b5821d685f6dc058d2d2e3cc8d7f77622fa4e7e55bddc5399; normalized lines 69–71.

> Both reports are technically feasible\. The missing/damaged report can
> include date ranges \(e\.g\., last 30 days, last quarter, etc\.\) which would
> be useful for trending\.

### REQ-100 — Filter Reports by Available Fields

- Internal key: REQ-35aa884d8e4aff3cc0adfc00c502811576ad4bf68543ab9b73bbe9185ec5267f
- Type: functional
- Priority: P2
- Priority basis: inferred
- Priority rationale: Filtering by available report fields is important report usability functionality; the source does not assign a priority\.
- Originating candidates: CAND-e024e581f97344a28220dcff0c702142f6ab5e180624d98eee19c50d0ee4a4a4

The system shall allow users to filter reports by fields that are available in the reports\.

Sources and evidence:

Source: [survey\_results\_2009\.txt](<../data/corpus/survey_results_2009.txt>); document ID: DOC-aac7bceef7a883652805583e98ec513b6ae2e7951e2ecfa18722127b1f12a5c4; normalized lines 74–74.

>   - "Can't filter by some fields that should be available"

### REQ-101 — Batch Update Item Location Records

- Internal key: REQ-366acd8de9991f7b1b902f62eb16b4c7d116a95773340ac451aa82a39b46c40f
- Type: functional
- Priority: P2
- Priority basis: inferred
- Priority rationale: Batch location maintenance supports important inventory operations; no explicit source priority is provided\.
- Originating candidates: CAND-e7dc48f1f7486b08729be4d9c9a963cd75edda81fcc0d6154b90e05a132072bb, CAND-f8a00a933039e350d051618f0403572471fa3724798adb494f5251c15d3248ee

The system shall allow users to change the location records of selected items in a batch update to move those items to a new location\.

Sources and evidence:

Source: [conversations/conv\_pines018\_item\_transfer\.eml](<../data/corpus/conversations/conv_pines018_item_transfer.eml>); document ID: DOC-a47eb1f11286ff9099687b72a901e4a6ed2455b431087c0742aa78583c5bd80a; normalized lines 9–9.

> - Change records of selected items to new location

Source: [conversations/conv\_pines018\_item\_transfer\.eml](<../data/corpus/conversations/conv_pines018_item_transfer.eml>); document ID: DOC-a47eb1f11286ff9099687b72a901e4a6ed2455b431087c0742aa78583c5bd80a; normalized lines 54–55.

> 3\. Batch update of location field - straightforward database update with
>    transaction safety\.

Source: [interview\_cataloging\_2009-05-08\.txt](<../data/corpus/interview_cataloging_2009-05-08.txt>); document ID: DOC-a79fab45108210e6bce7d92153dfcf055f2ef6b2cdab49a3f6f5717a3e35f29f; normalized lines 52–55.

> Fourth, we need to change records of selected items to move them to a new
> location\. And there should be mechanisms for reverting items back to their
> original location after a set period of time - like when a mobile library
> returns to base\.

### REQ-102 — Run Canned Reports for Standard Date Ranges

- Internal key: REQ-37103089c88f5232dfc39c363dcc36f2c1ab1a2c3bedba0d86e04074836cf84f
- Type: functional
- Priority: P2
- Priority basis: inferred
- Priority rationale: Inferred as high priority because the evidence specifies these standard date ranges for canned reports\.
- Originating candidates: CAND-7b96dba9e8b242de1165edea5425b8f3237fd2c85d722793a4a5c50eb86f0d8a

The system shall allow canned reports to run for the data ranges yesterday, last week, last month, or last year\.

Sources and evidence:

Source: [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>); document ID: DOC-091180de9b2d4ea83267d989411ac89f415d4def3bbf7cd51651fb7fda8d8bf9; normalized lines 607–608.

> delivered with the product\. Will have the ability for it to run by yesterday's
> data, last week's, last month's, or last year's\. Canned reports can be checked

### REQ-103 — Authorized Item Transfers Restricted by Role

- Internal key: REQ-372718b91bcf891c549cb877aba944e6ef70f32a059e3c0d8fd66c601e415e1e
- Type: functional
- Priority: P1
- Priority basis: inferred
- Priority rationale: Restricting transfer authority protects collection operations and access control\.
- Originating candidates: CAND-1e6aaedd25c5edf80c44de4d95c4e3be16db0017f209f2d85e06ef29bf08a167

The system shall restrict item transfers to authorized roles, such as managers, administrators, and transfer coordinators\.

Sources and evidence:

Source: [conversations/conv\_pines018\_item\_transfer\.eml](<../data/corpus/conversations/conv_pines018_item_transfer.eml>); document ID: DOC-a47eb1f11286ff9099687b72a901e4a6ed2455b431087c0742aa78583c5bd80a; normalized lines 95–97.

> We need to be careful about permissions here\. Not every staff member
> should be able to transfer items between branches\. This should be limited
> to certain roles \(managers, administrators, transfer coordinators\)\.

### REQ-104 — Report Scheduling Options \(Run ASAP to Yearly\)

- Internal key: REQ-3753a58491e0435248647e735e6d290759afdc222f5e161c2933d3ee858d361a
- Type: functional
- Priority: P2
- Priority basis: inferred
- Priority rationale: Scheduling is important for recurring reporting workflows, but the source does not identify it as critical or mandatory compliance\.
- Originating candidates: CAND-bf07a55a9de5edf14234f3021361bf7b3a2c572f0796cd0501188b41e6df1e0e

The system shall provide report scheduling options including Run ASAP, Hourly, Daily, Weekly, Monthly, and Yearly\.

Sources and evidence:

Source: [evergreen\_reference\_2009\.txt](<../data/corpus/evergreen_reference_2009.txt>); document ID: DOC-e6aa9f8c6308ab748459f87b578a0df9df9c865b7911bac3686e865963b7af6f; normalized lines 172–172.

> - No ability to select Run ASAP, Hourly, Daily, Weekly, Monthly, Yearly

### REQ-105 — Role-Appropriate Functionality by Security Roles

- Internal key: REQ-38689a78b31d9ea480f209d34eac46a9d829d49cf401506d743febe76495c08b
- Type: functional
- Priority: P2
- Priority basis: inferred
- Priority rationale: Role-appropriate functionality affects all major user groups and access to important system capabilities\.
- Originating candidates: CAND-9f0783ad949c6c6c534033bcc04bee2656d09541c1117cadd924da59d80708db

The system shall support the user types and roles Patron, Staff, Local System Administrator, Library Manager, Library Administrator, and Global System Administrator, and shall provide functionality and access appropriate to each role\.

Sources and evidence:

Source: [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>); document ID: DOC-091180de9b2d4ea83267d989411ac89f415d4def3bbf7cd51651fb7fda8d8bf9; normalized lines 96–121.

> The following user types have been identified:
> 
> \* Patron: A person utilizing the resources of a library, either as a member
>   of the public with a library card or as a member of the public without a
>   card\. Patrons may interact with the system through the OPAC\.
> 
> \* Staff: Employees of the library system who are involved in designing and
>   providing services to the public\. This includes circulation staff, reference
>   staff, and specialized staff\.
> 
> \* Local System Administrators: Individuals \(typically library managers\) who
>   oversee library processes and have elevated permissions within the system\.
>   They can configure local settings and run system reports\.
> 
> \* Library Managers: Individuals who supervise organizational units and provide
>   input to the design and implementation of library services\. They use reports
>   for planning and evaluation\.
> 
> \* Library Administrators: Senior leadership who plan and direct library services
>   and priorities\. They require aggregated, high-level reports for strategic
>   planning and board presentations\.
> 
> \* Global System Administrator: The individual\(s\) who manage the ILS at the
>   consortium level, implementing software changes and configurations, and
>   generating statistical reports for the entire system\.
> 

### REQ-106 — Filter Reports Using Uploaded Text Files

- Internal key: REQ-38715fba26491d543d05df19e4e068aa17ccbd3e5c5bc8e613d6c7499b109837
- Type: functional
- Priority: P2
- Priority basis: inferred
- Priority rationale: Inferred as high priority because the evidence explicitly requires text-file filtering for reports\.
- Originating candidates: CAND-7ff3df2cd1ab48d85ed5b2a87f45e8eafe978f2ba1f32b447d82753c98350297

The system shall allow a text file, such as a file containing barcodes or TCNs, to be uploaded and used to filter a report\.

Sources and evidence:

Source: [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>); document ID: DOC-091180de9b2d4ea83267d989411ac89f415d4def3bbf7cd51651fb7fda8d8bf9; normalized lines 646–647.

> - Ability to upload a text file such as barcodes or TCN to use for filtering
>   on a report

### REQ-107 — Immediate Payment Updates for Reconciliation

- Internal key: REQ-38908c17dbfe657f8bcc17896465ebd62dff56e741e92d669b089771cbc12276
- Type: nonfunctional
- Priority: P2
- Priority basis: inferred
- Priority rationale: Immediate financial updates support accurate operational reconciliation, but the source does not assign a formal priority level\.
- Originating candidates: CAND-0d0505711a88919d8fc649aeba575aabb9fcb9f3fe1216ae6bbee236ca33088f

When a patron makes a payment, including a front-desk payment, the system shall reflect that payment immediately to support real-time reconciliation\.

Sources and evidence:

Source: [email\_financial\_reports\.eml](<../data/corpus/email_financial_reports.eml>); document ID: DOC-8b6cfb3cf368b794d82567933f9c85062740814819b1e28b4837f6021cbcbee6; normalized lines 90–91.

>   payment at the front desk, we need the system to reflect that immediately\.
> 

Source: [email\_financial\_reports\.eml](<../data/corpus/email_financial_reports.eml>); document ID: DOC-8b6cfb3cf368b794d82567933f9c85062740814819b1e28b4837f6021cbcbee6; normalized lines 119–120.

>    Financial information can be updated easily\. A staff user can easily query
>    patron accounts with balances greater than X dollars\.

### REQ-108 — Item Transfer Utility

- Internal key: REQ-38ed7b3651926eddb0e7b728a5b9324d4d18b6fd3823c964976f89a492dff1db
- Type: functional
- Priority: P2
- Priority basis: inferred
- Priority rationale: Item movement is an important operational capability, but the sources do not assign a P-level priority\.
- Originating candidates: CAND-23684841540a2b28d39121747c26d1422265fef96bd82c1e9f9fe6f85ce7b73b, CAND-2c1ac17b11772eddc760b9316d81562b5df03409400e8a1635777bfa806c20fa

The system shall provide an item transfer utility that allows staff to select items, change their location records to move them to a new location, and generate pull lists\.

Sources and evidence:

Source: [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>); document ID: DOC-091180de9b2d4ea83267d989411ac89f415d4def3bbf7cd51651fb7fda8d8bf9; normalized lines 362–364.

>   - Ability to manually select titles from query results
>   - Ability to change records of selected items to move to new location
>   - Mechanisms for moving items: changing location field, generating pull lists

Source: [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>); document ID: DOC-091180de9b2d4ea83267d989411ac89f415d4def3bbf7cd51651fb7fda8d8bf9; normalized lines 363–364.

>   - Ability to change records of selected items to move to new location
>   - Mechanisms for moving items: changing location field, generating pull lists

### REQ-109 — Aged In-Transit Items Report

- Internal key: REQ-393e43f8baabd53a0bc1d6dc59a76eb92b0c45fbf20a7cb81a1f9f440398697e
- Type: functional
- Priority: P2
- Priority basis: inferred
- Priority rationale: Supports significant branch and system operations\.
- Originating candidates: CAND-caee8ea06096c3f103509ea080a24b00f9c565a4dd4a604061c42e326b4350c8

The system shall generate a report listing items that have been in transit for more than X days, where X is configurable, per branch and per system, and shall merge transit-to and transit-from items into a single report\.

Sources and evidence:

Source: [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>); document ID: DOC-091180de9b2d4ea83267d989411ac89f415d4def3bbf7cd51651fb7fda8d8bf9; normalized lines 370–374.

> 10\.7 In-Transit Items Report
> The system should generate a list of items that have been in-transit for more
> than X days \(X configurable\), per branch and per system\. The report should
> merge the transit-to and transit-from into one report for ease of front-line
> staff use\.

### REQ-110 — Revert Selected Items to Original Location

- Internal key: REQ-395bac6a71d09fb251fbc5caaddd5f405e0d0b540f69db7f83843f375075fe70
- Type: functional
- Priority: P3
- Priority basis: inferred
- Priority rationale: Location reversal is useful administrative functionality but is not identified as essential to basic operation\.
- Originating candidates: CAND-e39c0ae6b96bf38e1f06af791143eacd0741bb6a021ad5470e26e0156d1b9a91

The system shall provide the ability to revert selected items to their original location\.

Sources and evidence:

Source: [survey\_results\_2009\.txt](<../data/corpus/survey_results_2009.txt>); document ID: DOC-aac7bceef7a883652805583e98ec513b6ae2e7951e2ecfa18722127b1f12a5c4; normalized lines 90–90.

>   - Revert items to original location: 18%

### REQ-111 — Payment Audit Trail Linked to Applied Charges

- Internal key: REQ-39642b8eda3fee136e34f247e078cc9156e505ad21d38aff7ff1fe0879455753
- Type: functional
- Priority: P1
- Priority basis: explicitly specified
- Priority rationale: The source explicitly identifies the financial audit trail as critical to reconciliation\.
- Originating candidates: CAND-695c1810eb76dff409ae00f571f17bcb0ab32a686c2f786412fc7fd293e629a9

The system shall maintain an audit trail or ledger of patron payments that records the specific charges to which each payment was applied, enabling reconciliation and tracing each payment to its charge\.

Sources and evidence:

Source: [email\_financial\_reports\.eml](<../data/corpus/email_financial_reports.eml>); document ID: DOC-8b6cfb3cf368b794d82567933f9c85062740814819b1e28b4837f6021cbcbee6; normalized lines 22–24.

> 3\. Audit trail - system must maintain a ledger of patron payments, including
>    which charges payments are applied to, to facilitate reconciliation\.
> 

Source: [email\_financial\_reports\.eml](<../data/corpus/email_financial_reports.eml>); document ID: DOC-8b6cfb3cf368b794d82567933f9c85062740814819b1e28b4837f6021cbcbee6; normalized lines 42–44.

> - The financial audit trail is CRITICAL for our finance department\. They need
>   to be able to trace every payment back to the specific charge it was applied
>   to\. Without this, we can't reconcile our accounts properly\.

Source: [email\_financial\_reports\.eml](<../data/corpus/email_financial_reports.eml>); document ID: DOC-8b6cfb3cf368b794d82567933f9c85062740814819b1e28b4837f6021cbcbee6; normalized lines 132–134.

> 5\. AUDIT TRAIL:
>    The system maintains a ledger of patron payments, including which charges
>    payments are applied to, to facilitate reconciliation\.

### REQ-112 — Section 508 Accessibility Compliance

- Internal key: REQ-39774cae3d3ee660f182703d232d92e9ad3976734feb6db96f39414355d3ecfa
- Type: nonfunctional
- Priority: P1
- Priority basis: explicitly specified
- Priority rationale: The source explicitly describes Section 508 compliance as mandatory and non-negotiable for the public institution\.
- Originating candidates: CAND-305233fb98b5e408bac226e8caa51a64bf48c6c730f5fb6e23f51a906d108d64

The system shall comply with Section 508 accessibility requirements\.

Sources and evidence:

Source: [interview\_sysadmin\_2009-05-10\.txt](<../data/corpus/interview_sysadmin_2009-05-10.txt>); document ID: DOC-b1738fd7a6de9498f19ede6747ba156ecb29ead86ad1c9a2768b53e862ece1a9; normalized lines 56–56.

> ROBERTY: This is non-negotiable\. As a public institution, we MUST comply with

Source: [interview\_sysadmin\_2009-05-10\.txt](<../data/corpus/interview_sysadmin_2009-05-10.txt>); document ID: DOC-b1738fd7a6de9498f19ede6747ba156ecb29ead86ad1c9a2768b53e862ece1a9; normalized lines 61–64.

> 
> We can't have blind staff members unable to run reports\. The HTML output
> needs to be properly structured with alt tags, ARIA labels, and proper
> semantic HTML\. And the system needs to produce standards-compliant HTML\.

### REQ-113 — Optional Streamlined Staff Login Without Mandatory Infrastructure

- Internal key: REQ-397b067f8434592807aa035f151791afca49fdc9b8050386071fc66a710586c4
- Type: nonfunctional
- Priority: P2
- Priority basis: inferred
- Priority rationale: The requirement preserves access for branches without specialized infrastructure, but the source does not assign a formal priority level\.
- Originating candidates: CAND-06a0e9425321185a882fbcf9f10b62169d11fb29380e8ab0e91cdef9cc588f2c

The system shall support streamlined staff login methods, such as card readers, without requiring them, so that branches lacking the necessary infrastructure can use traditional username-and-password login exclusively\.

Sources and evidence:

Source: [email\_staff\_login\.eml](<../data/corpus/email_staff_login.eml>); document ID: DOC-64b10e94c42508c5aea1af877ec9d2fe34485b099b29994b8b1a76cadc55e8b3; normalized lines 43–46.

> Also - and this is important - the system should not REQUIRE the streamlined
> login\. Some of our smaller branches may not have the infrastructure for card
> readers\. So the requirement should be: "The system supports \(but does not
> require\) streamlined staff login methods\."

### REQ-114 — Run Multiple Canned Reports Concurrently into One Document

- Internal key: REQ-399a1800f44501f2eb83c88c74b40ec0a04d5a4dc209b28add9a9a84aabb65e8
- Type: functional
- Priority: P3
- Priority basis: inferred
- Priority rationale: Combined report execution is a convenience and productivity enhancement rather than a core operational necessity\.
- Originating candidates: CAND-467101f54bbe6e3325f4f1fd83d695fd7f75eab5fec60fd15085f8104fc6d64a

The system shall allow users to select multiple canned reports to run at the same time and shall present them within one document\.

Sources and evidence:

Source: [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>); document ID: DOC-091180de9b2d4ea83267d989411ac89f415d4def3bbf7cd51651fb7fda8d8bf9; normalized lines 608–609.

> data, last week's, last month's, or last year's\. Canned reports can be checked
> off from a list to run at the same time and will be viewed within one document\.

### REQ-115 — Reporting Data Dictionary for Fields and Relationships

- Internal key: REQ-3a89f0685c9ca2a243f211a3513ee0cbb0535b7b746e75f7b813d74be6697bf8
- Type: nonfunctional
- Priority: P2
- Priority basis: inferred
- Priority rationale: The data dictionaries support effective query creation by staff and therefore materially affect reporting usability, but the source does not assign an explicit priority\.
- Originating candidates: CAND-a8a4c3002bf5ed0f128f43d803a29357986105d50dcb22b33156b7fa279318c5

The system shall provide data dictionaries describing reporting field names, data types, and relationships to enable staff to write effective queries\.

Sources and evidence:

Source: [meeting\_tech\_subcommittee\_2009-06-30\.txt](<../data/corpus/meeting_tech_subcommittee_2009-06-30.txt>); document ID: DOC-e081aa7bd57bf5e59c75a8a86f592124757b74dff1ee0df4badc10c025092d96; normalized lines 92–93.

> Katherine: "Staff need to understand the data structures to write effective
> queries\. We need data dictionaries - field names, data types, relationships\."

### REQ-116 — Report Queue Position and Status Visibility

- Internal key: REQ-3af0b484058c2db4bac3c37131ff0b9a9211d8cb2030d11cf68dd7ca16736bf7
- Type: functional
- Priority: P2
- Priority basis: inferred
- Priority rationale: The sources identify report queue position and processing-status visibility as important operational capabilities but do not assign a formal priority level\.
- Originating candidates: CAND-0f71d6ae4a2f21a35cbc3fb37df177e7ee2ac6faf5d6329d991875f2dab95ae1, CAND-200915cb8e62a43b75ba68dbce47aa9ee2a0d143d0c8119ea3601874f9658605, CAND-40de2f446078e78eeb0d93ac9779a18b5b498031a49e0ebd19f37b04c758e5f9, CAND-8460e580561c835a4376c2b7475b737a8d19e4cedf0997859fda03965df1b8ad, CAND-a182d27c59420b2d39c368b1da24b3dc42c24d0a707de73064803d3abdc38573, CAND-c1640a340428f3c1ae9f0cbf3a802f3b709d235645676901be42d8e7de484e7b, CAND-ee4c2da9030b1c4d91bd3a6cea039204e6fcb4df7ee122dde1831e0828ff6ba3, CAND-f08e64a9bc1879f0e10d659ac465d9abec5a4b65eadbd32708bc79ed2662f381

The system shall provide report queue visibility so users can see that their report is queued, how many reports are ahead of it, when it was submitted, whether it is still processing, its status as waiting, running, completed, or failed, and its queue priority when provided\.

Sources and evidence:

Source: [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>); document ID: DOC-091180de9b2d4ea83267d989411ac89f415d4def3bbf7cd51651fb7fda8d8bf9; normalized lines 293–295.

> 8\.9 Report Queue
> Staff should be able to see where their report is in the queue of reports
> waiting to run\.

Source: [email\_report\_features\.eml](<../data/corpus/email_report_features.eml>); document ID: DOC-d9e168e0c03903021bf9e636e1d8e5f56dfcb79cc110d3839e38175a7c54344e; normalized lines 36–37.

> 7\. REPORTS QUEUING: Ability to see where your report is in the queue\.
> 

Source: [email\_report\_features\.eml](<../data/corpus/email_report_features.eml>); document ID: DOC-d9e168e0c03903021bf9e636e1d8e5f56dfcb79cc110d3839e38175a7c54344e; normalized lines 66–71.

> One more thing on report queuing - staff get frustrated when they submit a
> report and never hear back\. They need to see:
> - That their report is in the queue
> - How many reports are ahead of theirs
> - When their report was submitted
> - Status \(waiting, running, completed, failed\)

Source: [email\_report\_features\.eml](<../data/corpus/email_report_features.eml>); document ID: DOC-d9e168e0c03903021bf9e636e1d8e5f56dfcb79cc110d3839e38175a7c54344e; normalized lines 116–117.

> 
> 7\. REPORTS QUEUING: See position in queue, status, priority\.

Source: [evergreen\_reference\_2009\.txt](<../data/corpus/evergreen_reference_2009.txt>); document ID: DOC-e6aa9f8c6308ab748459f87b578a0df9df9c865b7911bac3686e865963b7af6f; normalized lines 42–42.

> - No query queue visibility

Source: [evergreen\_reference\_2009\.txt](<../data/corpus/evergreen_reference_2009.txt>); document ID: DOC-e6aa9f8c6308ab748459f87b578a0df9df9c865b7911bac3686e865963b7af6f; normalized lines 165–166.

> 4\.2 MISSING FEATURES
> - No report queue visibility \(staff can't see where their report is in queue\)

Source: [evergreen\_reference\_2009\.txt](<../data/corpus/evergreen_reference_2009.txt>); document ID: DOC-e6aa9f8c6308ab748459f87b578a0df9df9c865b7911bac3686e865963b7af6f; normalized lines 216–216.

> 3\. Add report queue visibility and status indicators

Source: [meeting\_minutes/meeting\_2009-07-20\_minutes\.txt](<../data/corpus/meeting_minutes/meeting_2009-07-20_minutes.txt>); document ID: DOC-5ab1dd8bc97af3b1ab2e378495f0e0d75fd501fcc19f923c0d8fda831074281b; normalized lines 41–42.

>   - Report queue visibility is important
>   - Board/executive reports need to be pre-defined

Source: [survey\_results\_2009\.txt](<../data/corpus/survey_results_2009.txt>); document ID: DOC-aac7bceef7a883652805583e98ec513b6ae2e7951e2ecfa18722127b1f12a5c4; normalized lines 71–71.

>   - "I can't see if my report is still processing"

Source: [survey\_results\_2009\.txt](<../data/corpus/survey_results_2009.txt>); document ID: DOC-aac7bceef7a883652805583e98ec513b6ae2e7951e2ecfa18722127b1f12a5c4; normalized lines 139–139.

> 12\. Ability to see where your report is in the queue\.

### REQ-117 — In-Transit Reports for Delivery Coordination

- Internal key: REQ-3b213e28192a44128ced93d988e8d0b9d968dfab5d71699f10f9d912a049fbc2
- Type: functional
- Priority: P1
- Priority basis: explicitly specified
- Priority rationale: The source explicitly describes in-transit item reports as critical for delivery coordination\.
- Originating candidates: CAND-0d9c44a06081f598aac73c876b5af8787a3bc509b100190099b746341dad8838

The system shall provide in-transit item reports to support delivery coordination\.

Sources and evidence:

Source: [meeting\_minutes/meeting\_2009-07-20\_minutes\.txt](<../data/corpus/meeting_minutes/meeting_2009-07-20_minutes.txt>); document ID: DOC-5ab1dd8bc97af3b1ab2e378495f0e0d75fd501fcc19f923c0d8fda831074281b; normalized lines 47–47.

>   - In-transit item reports are critical for delivery coordination

### REQ-118 — Run Management Processes on Linux or Solaris Server

- Internal key: REQ-3bf07cb0143e38bb1d75c52bd48bae63c9b707541478f3f7d77086352a6ca180
- Type: nonfunctional
- Priority: P2
- Priority basis: inferred
- Priority rationale: The source identifies Linux and Solaris as acceptable server platforms, making this an important deployment constraint, but it is not identified as safety-critical or compliance-critical\.
- Originating candidates: CAND-b3cc501f18bdd27a060b221548d9ac3c38dc03bd134d0bf2fcbff54d4556467c

Management Processes shall operate on a Linux or Solaris server\.

Sources and evidence:

Source: [meeting\_minutes/meeting\_2009-07-20\_minutes\.txt](<../data/corpus/meeting_minutes/meeting_2009-07-20_minutes.txt>); document ID: DOC-5ab1dd8bc97af3b1ab2e378495f0e0d75fd501fcc19f923c0d8fda831074281b; normalized lines 78–81.

> OE-2: Management Processes shall operate on a Linux or Solaris server\.
>       \[Consensus: Both Linux and Solaris are acceptable\. Most PINES
>       installations use Linux, but some larger systems use Solaris\.\]
> 

### REQ-119 — Enterprise Library Automation System Dependency

- Internal key: REQ-3d202b858d32bd0ca9658fdf2f6fb50255ff8ec608ac4cc650000085dac6cf4a
- Type: nonfunctional
- Priority: P2
- Priority basis: inferred
- Priority rationale: This is an explicit architectural dependency for Management Processes; no P1–P4 priority is supplied\.
- Originating candidates: CAND-e82deb9bad228f3245534e34cc11e37cf4c7b3ffe8670334309009e7914c6cf7, CAND-e97ab96d3d7908c20e128f7287bb05f4d17905935ab5ab00d8ec1cba750db89b

Management Processes shall rely on the data structures and functionality of an enterprise-level Library Automation System, including Acquisitions and Cataloging modules\.

Sources and evidence:

Source: [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>); document ID: DOC-091180de9b2d4ea83267d989411ac89f415d4def3bbf7cd51651fb7fda8d8bf9; normalized lines 204–206.

> DE-1: Management Processes rely on the data structures and functionality of an
>       enterprise-level Library Automation System, including Acquisitions and
>       Cataloging modules\.

Source: [meeting\_minutes/meeting\_2009-07-20\_minutes\.txt](<../data/corpus/meeting_minutes/meeting_2009-07-20_minutes.txt>); document ID: DOC-5ab1dd8bc97af3b1ab2e378495f0e0d75fd501fcc19f923c0d8fda831074281b; normalized lines 177–181.

> DE-1: Management Processes rely on the data structures and functionality of an
>       enterprise-level Library Automation System, including Acquisitions and
>       Cataloging modules\.
>       \[Discussion: The data we report on comes from the ILS\. We don't manage
>       acquisitions or cataloging ourselves\.\]

### REQ-120 — Transaction Context Reports by Date/Time, Workstation, or Staff

- Internal key: REQ-3dc810ade1a2b2ec3588905fa4fb2b7352152c75c2bc715cdddc74c8f13b382c
- Type: functional
- Priority: P2
- Priority basis: inferred
- Priority rationale: This supports operational investigation and transaction analysis using explicitly requested filters\.
- Originating candidates: CAND-42e202ad68ba22aefd289dde1d471446f2f437b14e4be84d70afc2a38609de3e

The system shall provide reports of transactions occurring on a specified date and time, at a specified workstation, or by a specified staff member\.

Sources and evidence:

Source: [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>); document ID: DOC-091180de9b2d4ea83267d989411ac89f415d4def3bbf7cd51651fb7fda8d8bf9; normalized lines 665–666.

> - Ability to run a report on transactions that occurred on x date and time on x
>   workstation or by x staff

### REQ-121 — Deletion Reports Broken Down by Record Type

- Internal key: REQ-3de91974e63c5e566c18239444e0cea7bdf96e8eaf6e7fddc7fb785dcf37db7d
- Type: functional
- Priority: P2
- Priority basis: inferred
- Priority rationale: Deletion auditing supports administrative oversight, but no explicit priority is supplied\.
- Originating candidates: CAND-4980a6242cca693c0a0cdd0670902b125d612a318bbfc24e00f168213b3d0556

The system shall provide deletion reports broken down by record type, including item, patron, and other record types\.

Sources and evidence:

Source: [conversations/conv\_pines022\_deletions\.eml](<../data/corpus/conversations/conv_pines022_deletions.eml>); document ID: DOC-7b8da7c05931fc99bc80d4a4bb0c8563e690e0c415b57f5ca1ae394462dc26c8; normalized lines 71–72.

> - Deletions by type \(item vs patron vs other\)
> - Deletions by location

### REQ-122 — Transfer History Reporting for Item Transfer Counts by Period

- Internal key: REQ-3e49c8b537afa6ce741017e6e9c21a6b9c39c90187db38f7044260b40ef113ba
- Type: functional
- Priority: P3
- Priority basis: inferred
- Priority rationale: This supports diagnostic collection management and is useful but not identified as essential for basic operation\.
- Originating candidates: CAND-08e04c8a9f19b91aeb06b44abf6183ca7a64bf13e951c5b371deef86385d5c86

The system shall track item transfer history and support reporting how many times an item has been transferred during a specified period\.

Sources and evidence:

Source: [conversations/conv\_pines018\_item\_transfer\.eml](<../data/corpus/conversations/conv_pines018_item_transfer.eml>); document ID: DOC-a47eb1f11286ff9099687b72a901e4a6ed2455b431087c0742aa78583c5bd80a; normalized lines 130–132.

> Can we track transfer history? Like, "this item has been transferred 5
> times in the past year\." That might indicate a problem with the item
> being in the wrong location\.

### REQ-123 — Report Users with Highest Deletion Counts

- Internal key: REQ-3f2e043f9b40b51c37127bb669d26c2ba6aed07bfc48ce7c8e113a1b8fdcd815
- Type: functional
- Priority: P3
- Priority basis: inferred
- Priority rationale: This is a useful audit-analysis capability but is not stated as essential to basic operation\.
- Originating candidates: CAND-3d32dc0af13b53200ebab059507c3d08e6e523ee85804d09da15c1b723bfd643

The system shall provide reporting that identifies users who delete the most records by deletion count\.

Sources and evidence:

Source: [conversations/conv\_pines022\_deletions\.eml](<../data/corpus/conversations/conv_pines022_deletions.eml>); document ID: DOC-7b8da7c05931fc99bc80d4a4bb0c8563e690e0c415b57f5ca1ae394462dc26c8; normalized lines 73–73.

> - Top users who delete the most records

### REQ-124 — Transaction-Safe Batch Updates to Location Field

- Internal key: REQ-3f713a839858bba3c17eb2601f1e9bc2e829bc7746d169628bba5576ab5bc651
- Type: nonfunctional
- Priority: P1
- Priority basis: inferred
- Priority rationale: Transaction safety protects data integrity during batch updates and is critical to reliable system operation\.
- Originating candidates: CAND-c6b17d5e787a0ca9b49073d30959b0f0558e5e16f10878bbdd3af0332fd33c3d

The system shall ensure transaction safety when performing batch updates to the location field\.

Sources and evidence:

Source: [conversations/conv\_pines018\_item\_transfer\.eml](<../data/corpus/conversations/conv_pines018_item_transfer.eml>); document ID: DOC-a47eb1f11286ff9099687b72a901e4a6ed2455b431087c0742aa78583c5bd80a; normalized lines 54–55.

> 3\. Batch update of location field - straightforward database update with
>    transaction safety\.

### REQ-125 — Report Error Feedback for High-Level and Query-Specific Details

- Internal key: REQ-3fd9b55e518abf077ca655659d2be48c202adab908f3cb71f3ae730ca0fa7425
- Type: functional
- Priority: P2
- Priority basis: inferred
- Priority rationale: Meaningful failure feedback is important for operating and troubleshooting reports, but the source does not assign an explicit priority\.
- Originating candidates: CAND-a942896713be0071e1f2784394f893f3a1f420ed0c9023e1ed37544ca36a8565

The system shall provide thorough high-level error reporting and feedback and shall allow Local System Administrators and the Global System Administrator to obtain low-level query-specific feedback from the front-end interface\.

Sources and evidence:

Source: [meeting\_minutes/meeting\_2009-07-20\_minutes\.txt](<../data/corpus/meeting_minutes/meeting_2009-07-20_minutes.txt>); document ID: DOC-5ab1dd8bc97af3b1ab2e378495f0e0d75fd501fcc19f923c0d8fda831074281b; normalized lines 158–163.

> UD-4: The system shall provide thorough high-level error reporting and feedback
>       and shall allow low-level query-specific feedback for Local and Global
>       System Administrators from the front-end interface\.
> 
>       \[Discussion: When reports fail, staff need to understand why\. Error
>       messages should be meaningful\.\]

### REQ-126 — Deletion Compliance Reporting

- Internal key: REQ-40626f32b12f2d6e58dd91a375db01bedf6ad72564a1408881a54547119f2442
- Type: functional
- Priority: P1
- Priority basis: inferred
- Priority rationale: Supports retention-schedule audits and compliance verification\.
- Originating candidates: CAND-d73d76a7a303eb099f5778ba95feebc9eb4231f0a6016b80af1abb9e7f71ff06

The system shall support compliance reporting that states the number of patron records deleted and the date of deletion\.

Sources and evidence:

Source: [conversations/conv\_pines022\_deletions\.eml](<../data/corpus/conversations/conv_pines022_deletions.eml>); document ID: DOC-7b8da7c05931fc99bc80d4a4bb0c8563e690e0c415b57f5ca1ae394462dc26c8; normalized lines 88–91.

> This also helps with compliance\. Some libraries need to prove they're
> handling data according to retention schedules\. Being able to show
> "we deleted 500 patron records on X date" is important for audits\.
> 

### REQ-127 — Transaction Reports for Holds and Check-Outs with Subtotals by Holds Type

- Internal key: REQ-41c168e28bc9f42f2118a88855ca61268ae666b1b0c8a66e3ab8cd2a8a266125
- Type: functional
- Priority: P2
- Priority basis: inferred
- Priority rationale: The report covers substantial circulation and holds analysis across several organizational scopes, but the source does not assign an explicit priority\.
- Originating candidates: CAND-b9de88da4a2a6a1449fad30414db6f69f115d002bd852fdb9af0ee10cfea38cb

The system shall generate transaction reports for holds placed, holds filled, and check-outs per patron, per library, per selected group of libraries, per system, and per county; display the number of check-outs and placed holds per patron; and subtotal holds by type, including active, frozen, and frozen-until\.

Sources and evidence:

Source: [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>); document ID: DOC-091180de9b2d4ea83267d989411ac89f415d4def3bbf7cd51651fb7fda8d8bf9; normalized lines 446–451.

> 12\.6 Transactions Report
> The system can generate a report of transactions \(holds placed, holds filled,
> and check-outs\) per patron, per library, per selected group of libraries,
> per system, per county\. The system displays the number of check-outs and
> placed holds per patron\. Holds are subtotaled by type, e\.g\., active, frozen,
> and frozen-until holds\.

### REQ-128 — Branch Grouping for Location Displays

- Internal key: REQ-4253b851b4ccc8507247fc35654eb718832f15a36063f840ef3780cb3fa766d5
- Type: functional
- Priority: P3
- Priority basis: inferred
- Priority rationale: Grouping improves usability for large location sets but is not identified as essential to basic operation\.
- Originating candidates: CAND-6487a6e31bce657f5f66ab93908852be7812aa44794b01cf882b3771ea654c5f

The system shall allow branches to be grouped, for example by system or region, to reduce crowding when displaying many locations\.

Sources and evidence:

Source: [conversations/conv\_pines015\_capacity\_interface\.eml](<../data/corpus/conversations/conv_pines015_capacity_interface.eml>); document ID: DOC-4acf2fdb375b86d49420e5743267e19b3f0af9ebe8bd764c1a88379aa9f5b662; normalized lines 49–51.

> One consideration: with 286 locations, the overview might get crowded\.
> Maybe we should group by system/region? Or allow filtering?
> 

### REQ-129 — Generate Pre-Overdue, Overdue, and Holds Notice Reports

- Internal key: REQ-42618db7e795451bf5d8659b55422ce247db23533c3d2ee50cae20d55409245f
- Type: functional
- Priority: P3
- Priority basis: inferred
- Priority rationale: These reports support operational oversight but are not shown to be essential to basic operation\.
- Originating candidates: CAND-4b791422a65411fbcb36535fce939b380327eb66c475a5777568292a75c9d3d8

The system shall provide reports for pre-overdue notices, overdue notices, and holds notices sent\.

Sources and evidence:

Source: [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>); document ID: DOC-091180de9b2d4ea83267d989411ac89f415d4def3bbf7cd51651fb7fda8d8bf9; normalized lines 648–648.

> - Ability to run reports for pre-overdue, overdue, and holds notices sent

### REQ-130 — Accessible Management Processes Comply with Section 508

- Internal key: REQ-43e5e92e2408a724dbbdb56548f4f3ce38d4f6cbf35c13249c060347cbb35b03
- Type: nonfunctional
- Priority: P1
- Priority basis: explicitly specified
- Priority rationale: The source explicitly identifies accessibility and Section 508 compliance as mandatory legal requirements\.
- Originating candidates: CAND-e6412b0ca42a6d9f6226689adb8800cb150f5d721ba08bf5b7b5c51702aadd7f

Management Processes shall be accessible with screen-reading software, screen-magnification software, and other assistive technologies, including products such as JAWS, NVDA, and ZoomText, and shall comply with Section 508\.

Sources and evidence:

Source: [meeting\_minutes/meeting\_2009-07-20\_minutes\.txt](<../data/corpus/meeting_minutes/meeting_2009-07-20_minutes.txt>); document ID: DOC-5ab1dd8bc97af3b1ab2e378495f0e0d75fd501fcc19f923c0d8fda831074281b; normalized lines 95–100.

> OE-5: Management Processes shall be accessible with screen-reading software,
>       screen-magnification software, and other software programs designed to
>       increase accessibility\.
>       \[Discussion: Susan emphasized this is a legal requirement for public
>       institutions\. We need to support JAWS, NVDA, ZoomText, and other
>       assistive technologies\. Section 508 compliance is mandatory\.\]

### REQ-131 — Fines Waived Reports by Time Period and Branch

- Internal key: REQ-451641be1b31209b34c27ab707627d3a3836b414f57ebcdda48f39bc3c1e18ae
- Type: functional
- Priority: P2
- Priority basis: inferred
- Priority rationale: Branch- and time-based waived-fine reporting supports financial oversight; no explicit source priority is supplied\.
- Originating candidates: CAND-fd57729a1d264b5f4314ca99ec831188df4fc12727598d04794a6410f72d2b5a

The system shall provide reports of fines waived by time period and by branch\.

Sources and evidence:

Source: [email\_financial\_reports\.eml](<../data/corpus/email_financial_reports.eml>); document ID: DOC-8b6cfb3cf368b794d82567933f9c85062740814819b1e28b4837f6021cbcbee6; normalized lines 74–75.

> - Fines waived should be tracked per library because each library has its own
>   budget for waived fines\.

Source: [email\_financial\_reports\.eml](<../data/corpus/email_financial_reports.eml>); document ID: DOC-8b6cfb3cf368b794d82567933f9c85062740814819b1e28b4837f6021cbcbee6; normalized lines 128–129.

>    - Fines waived per time period and per branch
>    - Payments made per time period and per payment method \(staff desk,

### REQ-132 — Shelf Space Report Comparing Circulation, Collection, and Shelf Space Percentages

- Internal key: REQ-45a97b4d662a97503be8b357d9c5233c25e2b5e8576f1cd8442e020f1e9c0ef5
- Type: functional
- Priority: P2
- Priority basis: inferred
- Priority rationale: The report supports collection-management resource allocation, but the source does not assign a formal priority level\.
- Originating candidates: CAND-014cd73d14dd417db704dbc7e60d78d59534bd8bc38f2e1eda9e9aac965124b9

The system shall provide a shelf space report that, for each genre and format, compares the percentage of total circulations, the percentage of the collection, and the percentage of total shelf space\.

Sources and evidence:

Source: [interview\_cataloging\_2009-05-08\.txt](<../data/corpus/interview_cataloging_2009-05-08.txt>); document ID: DOC-a79fab45108210e6bce7d92153dfcf055f2ef6b2cdab49a3f6f5717a3e35f29f; normalized lines 100–105.

> 1\. The shelf space report is important for collection management\. For each
>    genre and format, I need to compare:
>    - Percentage of total circulations
>    - Percentage of the collection
>    - Percentage of total shelf space
>    This helps me decide where to allocate resources\.

### REQ-133 — Detailed Shelf Space Comparison Report by Genre and Format

- Internal key: REQ-45a97b4d662a97503be8b357d9c5233c25e2b5e8576f1cd8442e020f1e9c0ef5-new
- Type: functional
- Priority: P2
- Priority basis: inferred
- Priority rationale: The report supports important collection and space analysis; the source does not establish a more specific priority\.
- Originating candidates: CAND-9232a3279103eae4acab816cf83f390ee00d3e93d8ee9f6d9f86842f468a9db6

For each genre and format, the system shall provide a shelf space report that compares percentage of total circulations, percentage of the collection, and percentage of total shelf space, and the report shall be runnable per library and per system\.

Sources and evidence:

Source: [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>); document ID: DOC-091180de9b2d4ea83267d989411ac89f415d4def3bbf7cd51651fb7fda8d8bf9; normalized lines 336–343.

> 10\.3 Shelf Space Report
> For each genre and format of material, ability to compare:
>   - The percentage of total circulations
>   - The percentage of the collection
>   - The percentage of total shelf space
> 
> The report should be able to run per library and per system\.
> 

### REQ-134 — Separate Development/Training Environment Distinct from Production

- Internal key: REQ-467092eba9ef2159fc541702b382c93613fe45f99e6bd71651d544d415fc549b
- Type: nonfunctional
- Priority: P2
- Priority basis: inferred
- Priority rationale: Environment separation supports safe report development and testing, but no explicit priority is supplied\.
- Originating candidates: CAND-4676a15703b2d8a116563ec9a3c675df8bd97451900302089ed9a04afc7655d8

The system shall provide a development or training environment distinct from the production environment for reports\.

Sources and evidence:

Source: [evergreen\_reference\_2009\.txt](<../data/corpus/evergreen_reference_2009.txt>); document ID: DOC-e6aa9f8c6308ab748459f87b578a0df9df9c865b7911bac3686e865963b7af6f; normalized lines 186–186.

> - No development/training environment separation

### REQ-135 — Canned Report Templates for On-Demand and Recurring Execution

- Internal key: REQ-4672df0613679a6e6ae21e10378f8f08f66c2939bc25297d916c438a95a601f2
- Type: functional
- Priority: P2
- Priority basis: inferred
- Priority rationale: Predefined recurring reports are important to routine reporting, but the source does not establish them as critical\.
- Originating candidates: CAND-c115b03dfb31ef8d832cd9bfd9a14ce7be41f2832fcb9af2bbbca26443c35bc1

The system shall supply a set of pre-written canned report templates delivered with the product and shall allow users to run them ASAP or on a recurring basis\.

Sources and evidence:

Source: [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>); document ID: DOC-091180de9b2d4ea83267d989411ac89f415d4def3bbf7cd51651fb7fda8d8bf9; normalized lines 605–607.

> Canned reports are generic reports set to run by the individual either ASAP or
> recurring\. There should be a certain set of templates that are pre-written and
> delivered with the product\. Will have the ability for it to run by yesterday's

### REQ-136 — Branch Capacity and Collection Distribution Analysis

- Internal key: REQ-46af57c3953900c8cfab95b4427e28dfac06e75e994179cc886823776e20ccec
- Type: functional
- Priority: P2
- Priority basis: inferred
- Priority rationale: Branch capacity and collection distribution are identified as management analysis capabilities, although the evidence does not define the capacity measure\.
- Originating candidates: CAND-4597dfcaba5a030e50a217574d5d5f569d561513a2a2d841057068b8f660705a

The system shall provide reporting and analysis capabilities to analyze branch capacity and determine optimal distribution of the collection\.

Sources and evidence:

Source: [meeting\_minutes/meeting\_2009-03-15\_minutes\.txt](<../data/corpus/meeting_minutes/meeting_2009-03-15_minutes.txt>); document ID: DOC-defef992db2ae0e10167fd94902eac93f82c59c4c070df030ca2f77811082818; normalized lines 59–61.

>   - Analyzing the Library collection and its use by patrons
>   - Analyzing branch capacity and optimal distribution of the collection
>   - Analyzing demographics and interests of patrons

### REQ-137 — Survey Name Filtering Without Survey ID Entry

- Internal key: REQ-4712dfa1344a1e1fa9a93331144bbf799cdd2de086893902540cf4d2aab1925e
- Type: functional
- Priority: P3
- Priority basis: inferred
- Priority rationale: Selecting a survey name improves reporting convenience and usability, but the source does not indicate that it is essential to basic operation\.
- Originating candidates: CAND-a8c4505902f52cdc9f24b45cc550f77ac08c2e0bd4849733de19ba5df3b79dcd

The system shall allow users to select a survey name when filtering reports without requiring entry of the survey ID\.

Sources and evidence:

Source: [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>); document ID: DOC-091180de9b2d4ea83267d989411ac89f415d4def3bbf7cd51651fb7fda8d8bf9; normalized lines 661–662.

> - Ability to select the survey name and not have to enter the survey id for
>   filtering

### REQ-138 — Fine-Grained Permissions for Creating and Running Reports

- Internal key: REQ-4749a037a3a6cf57659fe8fdbda89ccac8129bd823ddb037542dafbf79d73867
- Type: functional
- Priority: P1
- Priority basis: inferred
- Priority rationale: Inferred as critical because the evidence identifies fine-grained control over report creation and execution as a required permission capability\.
- Originating candidates: CAND-7cb4d4b570f0c55a2909409c584dac5f16ed16b19d1c09fbee8ba04ee368876c, CAND-84b7320cea15e0202dbd7921f79d0e207b0a6d0dabdc1df822988a784610517a

The system shall provide fine-grained permissions that control who may create and run reports and which reports each user may create or run\.

Sources and evidence:

Source: [evergreen\_reference\_2009\.txt](<../data/corpus/evergreen_reference_2009.txt>); document ID: DOC-e6aa9f8c6308ab748459f87b578a0df9df9c865b7911bac3686e865963b7af6f; normalized lines 185–185.

> - No fine-grained permissions for reports

Source: [survey\_results\_2009\.txt](<../data/corpus/survey_results_2009.txt>); document ID: DOC-aac7bceef7a883652805583e98ec513b6ae2e7951e2ecfa18722127b1f12a5c4; normalized lines 61–61.

>   - Fine-grained permissions \(who can create/run what\): 76%

### REQ-139 — Management Processes Use a Fully Relational Database Backend

- Internal key: REQ-4782640a579b647a510ccf0f1afeaa9afc451704838df6cfda1a04d04addd510
- Type: nonfunctional
- Priority: P2
- Priority basis: inferred
- Priority rationale: The source states this as an explicit technical constraint supporting the reporting layer, but does not establish it as critical or mandatory compliance\.
- Originating candidates: CAND-c44959e9d1d15c61674532cb0eff5d5a9621844f7e7f38426a672c65c60d463f

Management Processes shall use a fully relational database back-end\.

Sources and evidence:

Source: [meeting\_minutes/meeting\_2009-07-20\_minutes\.txt](<../data/corpus/meeting_minutes/meeting_2009-07-20_minutes.txt>); document ID: DOC-5ab1dd8bc97af3b1ab2e378495f0e0d75fd501fcc19f923c0d8fda831074281b; normalized lines 106–108.

> CO-1: Management Processes shall use a fully relational database back-end\.
>       \[Discussion: Evergreen already uses PostgreSQL\. We need to ensure our
>       reporting layer works properly with the relational structure\.\]

### REQ-140 — Canned Report Definitions Support

- Internal key: REQ-47ac0149ece1a6c6de30f063c8b6b59a9db8bb87af3d9341b1658b731649d4c6
- Type: functional
- Priority: P2
- Priority basis: inferred
- Priority rationale: The requirement covers predefined reports specified in an attached report definition set; the source does not establish a more specific priority\.
- Originating candidates: CAND-8f89b91dbe18063602db77c1b389247140ac3021c1d4464e7c7ed695fae76ecf

The system shall support the canned reporting definitions described in Appendix A\.

Sources and evidence:

Source: [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>); document ID: DOC-091180de9b2d4ea83267d989411ac89f415d4def3bbf7cd51651fb7fda8d8bf9; normalized lines 297–300.

> 8\.10 Canned Report Examples
> The system must be able to support the reporting definitions as described in
> the attached report examples \(see Appendix A\)\.
> 

### REQ-141 — Historical Material Volume Filters

- Internal key: REQ-47efd0163702e0d88a82d2b1029efa9a04bbd49afd57a9b5d1249baa8da524c0
- Type: functional
- Priority: P2
- Priority basis: inferred
- Priority rationale: Inferred as important reporting functionality; no explicit source priority is supplied\.
- Originating candidates: CAND-650fc6e0aa0a4fcd0b185e822132eec9c32f12a0d60614eac4a044bc6ddcee68

The system shall provide date filters that allow reports to show material volume at any point in time and support historical comparisons\.

Sources and evidence:

Source: [conversations/conv\_pines014\_material\_volume\.eml](<../data/corpus/conversations/conv_pines014_material_volume.eml>); document ID: DOC-f10d646016479a881ae8ff4ab4043844ee55a671d71f1943623db3fbb5589d8a; normalized lines 78–79.

> We can also add date filters - volume at any point in time, not just
> current\. This would be useful for historical comparisons\.

Source: [conversations/conv\_pines014\_material\_volume\.eml](<../data/corpus/conversations/conv_pines014_material_volume.eml>); document ID: DOC-f10d646016479a881ae8ff4ab4043844ee55a671d71f1943623db3fbb5589d8a; normalized lines 91–92.

> The system should provide the ability to report on the volume of material
> in a given library at any point in time, based on:

### REQ-142 — Batch Item Transfer Between Branches

- Internal key: REQ-487c3d1860dba77b192c6005f68f8be44fd4b47b9039e06c7f2d2fae6c0dcec9
- Type: functional
- Priority: P2
- Priority basis: inferred
- Priority rationale: Supports significant operational workflows across library locations\.
- Originating candidates: CAND-cecc24ea5db477cc5885d210bf68b60376538c540d2fc56994077685f5c0e86a

The system shall provide a utility for transferring batches of items between branches, including uses such as moving items to a mobile library, an outreach collection, or a just-in-time warehouse\.

Sources and evidence:

Source: [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>); document ID: DOC-091180de9b2d4ea83267d989411ac89f415d4def3bbf7cd51651fb7fda8d8bf9; normalized lines 354–357.

> 10\.5 Item Transfer Utility
> System should provide a utility for transferring batches of items between
> branches\. Uses include: moving books into a mobile library, an outreach program
> collection, or a "just-in-time" warehouse\.

### REQ-143 — Query Tool Data Access Control

- Internal key: REQ-4a201812ab33b8e7bf1154550db6de5777a453599df09cb6c7c4859cecda9310
- Type: functional
- Priority: P1
- Priority basis: inferred
- Priority rationale: Access control protects data and query capabilities and is important to system security, although no explicit priority is supplied\.
- Originating candidates: CAND-5fe27c79a2cd4b0ee6ee91782de7c1880dc7a63426751a6bc42016661d38f6e5

Administrators shall control staff access to the tables and fields used by the query tool\.

Sources and evidence:

Source: [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>); document ID: DOC-091180de9b2d4ea83267d989411ac89f415d4def3bbf7cd51651fb7fda8d8bf9; normalized lines 258–259.

> Administrators should control staff access to tables and fields\.
> 

### REQ-144 — Background Processing for Complex Reports

- Internal key: REQ-4a32a3b56eead0606939e075d5ad8d6d97c1ac5872512068c555dc81bd8d4e47
- Type: functional
- Priority: P1
- Priority basis: inferred
- Priority rationale: Protects core circulation and other system operations from reporting disruption\.
- Originating candidates: CAND-ca37c9c8877e4d9bd5ffac768ed2bb4aedc5611a24174efec8dfaf867d4389cd

The system shall allow complex reports to be queued and processed in the background so that running reports does not tie up the database or slow down other clients, including the circulation client\.

Sources and evidence:

Source: [interview\_sysadmin\_2009-05-10\.txt](<../data/corpus/interview_sysadmin_2009-05-10.txt>); document ID: DOC-b1738fd7a6de9498f19ede6747ba156ecb29ead86ad1c9a2768b53e862ece1a9; normalized lines 39–44.

> ROBERT: That's actually a major concern\. Right now, when someone runs a complex
> report, it can tie up the database and slow down the circulation client\. We
> need to make sure reports can be queued and processed in the background\. Or we
> need read-only reporting replicas\. The key requirement is that searches and
> reports can be processed during open hours without disrupting other system
> functions\.

### REQ-145 — Location-Filtered Item Counts for Volume Totals

- Internal key: REQ-4ae4b0f852a72bb24649b10215b3c932066084b34a91af5d5260738fdcd92c04
- Type: functional
- Priority: P2
- Priority basis: inferred
- Priority rationale: Location-specific totals are important for branch-level reporting and operational analysis\.
- Originating candidates: CAND-16470d484872ca45a239e593eba521e3c52ff83981e3ed3f107e7becef78ed92

The reporting query shall count all items with a location filter so that it can produce library-specific volume totals\.

Sources and evidence:

Source: [conversations/conv\_pines014\_material\_volume\.eml](<../data/corpus/conversations/conv_pines014_material_volume.eml>); document ID: DOC-f10d646016479a881ae8ff4ab4043844ee55a671d71f1943623db3fbb5589d8a; normalized lines 73–76.

> For the volume report, I'm thinking we need a query that:
> 1\. Counts all items with a location = your library
> 2\. Groups by categories \(fiction/non-fiction, format, etc\.\)
> 3\. Shows breakdowns with holds count per category

### REQ-146 — Aggregate Report Results at Multiple Levels

- Internal key: REQ-4d1615e1c31c931c9b0acc9439f3400654b06b41649b4d34dcd36c139f1555e2
- Type: functional
- Priority: P2
- Priority basis: inferred
- Priority rationale: Multiple aggregation levels support management analysis, but no explicit priority is supplied\.
- Originating candidates: CAND-4729a2de940a964bcf1dad9811be4a392ca7a93a7035dd081a51c4b0e06f343e

The system shall allow report results to be grouped or aggregated at different levels, including per-library and per-system breakdowns\.

Sources and evidence:

Source: [conversations/conv\_pines016\_shelf\_space\.eml](<../data/corpus/conversations/conv_pines016_shelf_space.eml>); document ID: DOC-b507e8abe1ba7c996c1d86d688e90bcf2404694ec00528c8361f26dfc8bd82f1; normalized lines 74–75.

> We can also add the per-library and per-system breakdown\. That's just
> adding GROUP BY clauses to the right levels\.

### REQ-147 — Exclude Patron-Facing Functions from Management Reporting

- Internal key: REQ-4d442a204e10ac10ff40e537dac866b57793698dc709a714969227923af74261
- Type: nonfunctional
- Priority: P2
- Priority basis: inferred
- Priority rationale: The source explicitly defines this system boundary, but no formal priority is supplied\.
- Originating candidates: CAND-4b6f691f03cd44214373992be9b5a649fc877ca3c211996efbc0fb9e1559b3a3

The reporting system shall exclude day-to-day patron-facing functions; those functions shall remain part of the OPAC and circulation client\.

Sources and evidence:

Source: [meeting\_minutes/meeting\_2009-03-15\_minutes\.txt](<../data/corpus/meeting_minutes/meeting_2009-03-15_minutes.txt>); document ID: DOC-defef992db2ae0e10167fd94902eac93f82c59c4c070df030ca2f77811082818; normalized lines 51–55.

> that the group would focus on Management Processes - that is, reports and
> analysis tools used by library managers, administrators, and staff for
> planning, evaluation, and oversight purposes\. She clarified that this does NOT
> include day-to-day patron-facing functions \(those are part of the OPAC and
> circulation client\)\.

### REQ-148 — Identify How Uncataloged Material Is Being Used

- Internal key: REQ-4d5162677abd8705447c4346c74a78a1755a8b15432b40710864dcd71f8d4c2f
- Type: functional
- Priority: P2
- Priority basis: inferred
- Priority rationale: The source identifies usage tracking as a stated operational requirement, but does not establish it as critical\.
- Originating candidates: CAND-c444007ee0eb5c3772b93b78b76a23920a2f6f3442315248a231257b70b1742b

The system shall provide the ability to identify how uncataloged material is being used\.

Sources and evidence:

Source: [interview\_cataloging\_2009-05-08\.txt](<../data/corpus/interview_cataloging_2009-05-08.txt>); document ID: DOC-a79fab45108210e6bce7d92153dfcf055f2ef6b2cdab49a3f6f5717a3e35f29f; normalized lines 34–36.

> The requirements are: quick distribution \(we need to process these fast\),
> minimal branch labor \(we can't spend a lot of time per item\), and ability to
> identify how the material is being used\. We also need to count transactions

### REQ-149 — Administrative Query for Candidate Materials

- Internal key: REQ-4d66266bac966e927bd99ee1b9c2da38b27a50bf7a59d6c2140484bf2b555000
- Type: functional
- Priority: P3
- Priority basis: inferred
- Priority rationale: The source reports this administrative feature as desired by respondents, but does not identify it as essential to core operation\.
- Originating candidates: CAND-df037f635a0dc9f1d9d540a6282238148a93bda09a04d53c0780e6e3a4a3a60a

The system shall provide an administrative query for candidate materials\.

Sources and evidence:

Source: [survey\_results\_2009\.txt](<../data/corpus/survey_results_2009.txt>); document ID: DOC-aac7bceef7a883652805583e98ec513b6ae2e7951e2ecfa18722127b1f12a5c4; normalized lines 85–86.

> QUESTION 8: "What administrative features do you need?"
>   - Query for candidate materials: 44%

### REQ-150 — Most Recent Patron Activity Determination

- Internal key: REQ-4dfd9d4432362235ee82b22831ea18f3f62b5462a85968600faf8c9a5cc2a58c
- Type: functional
- Priority: P2
- Priority basis: inferred
- Priority rationale: A consolidated most-recent-activity measure supports important patron activity reporting\.
- Originating candidates: CAND-1d880959b4ded45670c438208f21d25a894a3dea2d487d6e548224e70dbb2ebc

The system shall determine each patron's most recent activity by combining relevant events stored across different data sources or tables, including transaction activity, OPAC logins, online hold placements, online renewals, and digital resource access when logged\.

Sources and evidence:

Source: [conversations/conv\_pines024\_inactive\_patrons\.eml](<../data/corpus/conversations/conv_pines024_inactive_patrons.eml>); document ID: DOC-705ab8a51bf22b7b619dae61bf8d2be1cf2487e749f13e7ac55fdde430357793; normalized lines 84–95.

> Technically, this is straightforward\. We query the transaction table for
> the most recent activity per patron, and filter for those whose last
> activity is more than X days ago\.
> 
> For "electronic activity," we track:
> - OPAC login events
> - Online hold placements
> - Online renewals
> - Digital resource access \(if logged\)
> 
> These are stored in different tables, so we'd need a combined query\.
> 

### REQ-151 — Batch Item Transfers Between Branches

- Internal key: REQ-4ea945a733673579c14dd2101929cf1c09dac67aa67c424a051b9d9c64836ba4
- Type: functional
- Priority: P2
- Priority basis: inferred
- Priority rationale: Batch transfers support important branch and collection operations\.
- Originating candidates: CAND-15e2a1c9042548124ec97802868fdbbc4561f092805ed8495e0ca15f71da1da0

The system shall provide a utility for transferring batches of items between branches\.

Sources and evidence:

Source: [conversations/conv\_pines018\_item\_transfer\.eml](<../data/corpus/conversations/conv_pines018_item_transfer.eml>); document ID: DOC-a47eb1f11286ff9099687b72a901e4a6ed2455b431087c0742aa78583c5bd80a; normalized lines 1–3.

> I need a utility for transferring batches of items between branches\. We
> often need to move books to a mobile library, to an outreach program, or
> to a "just-in-time" warehouse\.

### REQ-152 — Patron Count by County Report

- Internal key: REQ-5005d3553e353a093d96fbd291dac28e4b3f2a1703167335862dbf279ca05911
- Type: functional
- Priority: P2
- Priority basis: inferred
- Priority rationale: This is a stated management reporting need, but no explicit source priority is provided\.
- Originating candidates: CAND-ed0d5044a14f8ebf45544607c5c5db86f113de212f72f4135483bc669135e7a2

The system shall provide a Patron Count by County report\.

Sources and evidence:

Source: [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>); document ID: DOC-091180de9b2d4ea83267d989411ac89f415d4def3bbf7cd51651fb7fda8d8bf9; normalized lines 547–547.

> - Patron Count by County

### REQ-153 — Voter Survey Responses County by Week Report

- Internal key: REQ-50a19f69485d02c73221e3f754991f962044f0aa3213e2261542547bcf79f406
- Type: functional
- Priority: P3
- Priority basis: inferred
- Priority rationale: This specific management report is useful but is not shown to be essential to basic operation; no explicit source priority is provided\.
- Originating candidates: CAND-f09593ec4afc503d109b89a44ef7bb3bd3ffa28032ebfe5e94d87ec6c8bd4397

The system shall provide a Voter Survey Responses County by Week report\.

Sources and evidence:

Source: [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>); document ID: DOC-091180de9b2d4ea83267d989411ac89f415d4def3bbf7cd51651fb7fda8d8bf9; normalized lines 553–553.

> - Voter Survey Responses County by Week

### REQ-154 — Executive Reports Interface

- Internal key: REQ-51ee1fa512e19ee9aa32ae5d74990db91ec16540cf05fe7789ef8eda83c1a13a
- Type: functional
- Priority: P2
- Priority basis: inferred
- Priority rationale: Executive reporting is an important management capability, but the source does not assign a P-level priority\.
- Originating candidates: CAND-2b12907af86263458da5cbceba1e5127770b7838992433af7b3bc956c8a3961d

The project shall compile a list of reports needed for an Executive Reports Interface, and the system shall provide an Executive Reports Interface to surface those reports\.

Sources and evidence:

Source: [meeting\_minutes/meeting\_2009-03-15\_minutes\.txt](<../data/corpus/meeting_minutes/meeting_2009-03-15_minutes.txt>); document ID: DOC-defef992db2ae0e10167fd94902eac93f82c59c4c070df030ca2f77811082818; normalized lines 40–46.

>   "Reports Working Group Mission:
>    - Document optimal Reports functionality within a future Evergreen release
>      and develop a list of requirements\.
>    - Become the Reports testing group, through which all new Reports development
>      would be filtered\.
>    - Compile a list of reports needed for an Executive Reports Interface\.
>    - Determine and create templates needed for all PINES libraries\."

### REQ-155 — Reporting Development and Training Environment with Production Migration

- Internal key: REQ-5274ec341a1fdb292ddf486244336728d149dd475eba593b83292ec7e8c22e59
- Type: nonfunctional
- Priority: P3
- Priority basis: inferred
- Priority rationale: This supports development and training workflows but is not stated as necessary for basic production operation\.
- Originating candidates: CAND-42dcb2d75232af264ab8bddc6ccad907def82aac7834b46850b081e3f596b7f4

The system shall provide a development or training environment for reporting, with migration capability to production\.

Sources and evidence:

Source: [evergreen\_reference\_2009\.txt](<../data/corpus/evergreen_reference_2009.txt>); document ID: DOC-e6aa9f8c6308ab748459f87b578a0df9df9c865b7911bac3686e865963b7af6f; normalized lines 220–220.

> 7\. Provide a development/training environment with migration capability

### REQ-156 — Configuration Migration Export and Import

- Internal key: REQ-5360d814680e583f014a2a33513053acba6117d665018cd970055dad81907929
- Type: functional
- Priority: P3
- Priority basis: inferred
- Priority rationale: Configuration migration supports deployment workflows but is not identified as essential to core operation\.
- Originating candidates: CAND-5582fe9c6ce9fd087858406d395f764c51f7cc91d2aa0e0db3419dc635b6bb68

The system shall provide export and import functionality to migrate configurations developed in training or development to production, including report templates, permission settings, and other configuration\.

Sources and evidence:

Source: [interview\_sysadmin\_2009-05-10\.txt](<../data/corpus/interview_sysadmin_2009-05-10.txt>); document ID: DOC-b1738fd7a6de9498f19ede6747ba156ecb29ead86ad1c9a2768b53e862ece1a9; normalized lines 95–97.

> The key is that configurations developed in training/dev need to be migratable
> to production\. We need export/import functionality for report templates,
> permission settings, and other configuration\.

### REQ-157 — Development and Training Environments With Migration

- Internal key: REQ-5360d814680e583f014a2a33513053acba6117d665018cd970055dad81907929-new
- Type: nonfunctional
- Priority: P3
- Priority basis: inferred
- Priority rationale: Providing separate development and training environments supports operational implementation, but no explicit priority is supplied for this candidate\.
- Originating candidates: CAND-5761e6541b0fee1705673a252c4526af721fbba5503ba12feec1e69d0f905607

The system shall provide development and training environments with the ability to migrate configurations to a production environment\.

Sources and evidence:

Source: [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>); document ID: DOC-091180de9b2d4ea83267d989411ac89f415d4def3bbf7cd51651fb7fda8d8bf9; normalized lines 159–160.

> CO-3: The system must provide a development and training environment with the
>       ability to migrate configurations to a production environment\.

### REQ-158 — Cancel Running Reports

- Internal key: REQ-53edbd5b459ca92389a3b9d794048866d005987a0f34750ae8df494f41026176
- Type: functional
- Priority: P2
- Priority basis: inferred
- Priority rationale: Provides operational control over long-running reporting work\.
- Originating candidates: CAND-d2e01e95a4df9cee9e20c98278922ec90e8fb93c7a1fe4183a4709b80389e417

The system shall allow users to cancel a running report\.

Sources and evidence:

Source: [evergreen\_reference\_2009\.txt](<../data/corpus/evergreen_reference_2009.txt>); document ID: DOC-e6aa9f8c6308ab748459f87b578a0df9df9c865b7911bac3686e865963b7af6f; normalized lines 168–168.

> - No ability to cancel a running report

### REQ-159 — Staff Account List Including Password Change and Expiration Dates

- Internal key: REQ-5435212810ea77283733034c7e6330d76bdb493cddd6bccfe8b815806aaab96e
- Type: functional
- Priority: P2
- Priority basis: inferred
- Priority rationale: The report supports account and security administration and is important, but the source does not establish it as critical\.
- Originating candidates: CAND-bc6cb2227ee9499878ac5afd81ff8503bb90feba527454f6b03d7d4c7a4cd3e1

The system shall provide a list of staff accounts that includes the date of last password change and account expiration\.

Sources and evidence:

Source: [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>); document ID: DOC-091180de9b2d4ea83267d989411ac89f415d4def3bbf7cd51651fb7fda8d8bf9; normalized lines 558–558.

> - List of Staff Accounts with date of last password change and account expiration

### REQ-160 — Configurable In-Transit Age Threshold

- Internal key: REQ-543cc4a79be0d916e2dc6465f1093e49e4d766be10bd73fffbbc291b6b71de5c
- Type: functional
- Priority: P2
- Priority basis: inferred
- Priority rationale: Configurable transit-age reporting supports transfer operations, but no explicit priority is supplied\.
- Originating candidates: CAND-58949b6fa23f8b4aff26acb554063793d18f55f519bd9c371c7221921fc41617

The system shall allow the threshold for identifying an item as in transit for more than X days to be configured; 7 days shall not be treated as mandatory because the source presents it only as a suggested default\.

Sources and evidence:

Source: [conversations/conv\_pines019\_020\_missing\_intransit\.eml](<../data/corpus/conversations/conv_pines019_020_missing_intransit.eml>); document ID: DOC-b233b12122cae48b5821d685f6dc058d2d2e3cc8d7f77622fa4e7e55bddc5399; normalized lines 31–32.

> in the delivery trucks\. I need to see what's been in-transit for more than
> X days \(X should be configurable, probably 7 days default\)\.

### REQ-161 — OPAC Independence

- Internal key: REQ-5478728780de0be7580bad7342657c17f6ca590b026cada458a95097ba8b0344
- Type: nonfunctional
- Priority: P2
- Priority basis: inferred
- Priority rationale: Avoiding unintended constraints on the OPAC is an important architectural boundary, but no explicit priority is supplied\.
- Originating candidates: CAND-2c397cfa61fb4cb35f7f73277ca660df6ab76658283022e032e32261e2c4471c

These requirements shall not constrain the functionality or features of the Online Public Access Catalog module\.

Sources and evidence:

Source: [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>); document ID: DOC-091180de9b2d4ea83267d989411ac89f415d4def3bbf7cd51651fb7fda8d8bf9; normalized lines 168–169.

> CO-5: These requirements must not constrain functionality or features of the
>       Online Public Access Catalog \(OPAC\) module\.

### REQ-162 — Centralized Multi-Location Management Processes

- Internal key: REQ-54dc5165886bad36793b9ce63cc2c0de9e7a6429988feffbe9a4db3aa9497e1c
- Type: nonfunctional
- Priority: P2
- Priority basis: inferred
- Priority rationale: Centralized multi-location services support consistent operation across the organization\.
- Originating candidates: CAND-13a693039b11df8ad619da643f0625430a9375b6c70529cb4fa7f6d21aae9798

Management Processes shall be consolidated at a central location and shall accept input and provide services to multiple locations\.

Sources and evidence:

Source: [meeting\_minutes/meeting\_2009-07-20\_minutes\.txt](<../data/corpus/meeting_minutes/meeting_2009-07-20_minutes.txt>); document ID: DOC-5ab1dd8bc97af3b1ab2e378495f0e0d75fd501fcc19f923c0d8fda831074281b; normalized lines 172–175.

> AS-2: Management Processes are consolidated at a central location, and accept
>       input and provide services to multiple locations\.
>       \[Discussion: Centralization enables consistent reporting but requires
>       good network connectivity\.\]

### REQ-163 — Optional Capture of Deletion Reason or Status

- Internal key: REQ-54e07fdc15db837cfe321435c5f67da2f756b02cbe3c2760bed2587876f6fe52
- Type: functional
- Priority: P3
- Priority basis: inferred
- Priority rationale: The source presents deletion context as possibly useful rather than mandatory, so it is treated as a nonessential enhancement\.
- Originating candidates: CAND-d9d951bff6c0e48140b438229837669bcc49faa60157b69760dfbc272e608b81

The system shall optionally capture the reason for deleting a record or the record's status immediately before deletion\.

Sources and evidence:

Source: [conversations/conv\_pines022\_deletions\.eml](<../data/corpus/conversations/conv_pines022_deletions.eml>); document ID: DOC-7b8da7c05931fc99bc80d4a4bb0c8563e690e0c415b57f5ca1ae394462dc26c8; normalized lines 18–23.

> We need:
> - What type of record was deleted \(item/patron/bib\)
> - When it was deleted
> - Who deleted it
> - Where they were located \(which branch\)
> - Possibly why \(status before deletion?\)

### REQ-164 — Saved and shareable queries

- Internal key: REQ-569cf887e9de0b9ee88dd40739ab7ff4d4928123f85df8a63b3b7c14b10e78ef
- Type: functional
- Priority: P2
- Priority basis: inferred
- Priority rationale: Reusable and shared queries improve reporting efficiency and collaboration; the source does not establish a more specific priority\.
- Originating candidates: CAND-8d7b692a9d051a2f77d1e15f7fae75aa5453ced07013ccf2512fcdbb741ec17b

The system shall allow users to save and share queries, including query templates similar to report templates\.

Sources and evidence:

Source: [conversations/conv\_pines018\_item\_transfer\.eml](<../data/corpus/conversations/conv_pines018_item_transfer.eml>); document ID: DOC-a47eb1f11286ff9099687b72a901e4a6ed2455b431087c0742aa78583c5bd80a; normalized lines 52–52.

> 2\. Save/share queries - similar to report templates\.

### REQ-165 — Weeding Report Includes Last Circulation Date

- Internal key: REQ-5761a15d2357c158faad812c8ea64f1b66230647e0b8b67415e97554e92c2199
- Type: functional
- Priority: P2
- Priority basis: inferred
- Priority rationale: Inferred as high priority because the evidence identifies this report enhancement as needed\.
- Originating candidates: CAND-800696766ba618c2c9136a4fb09023b2b63d145ac05900376918042ff99751ac

The system shall provide a weeding report that includes the date of last circulation\.

Sources and evidence:

Source: [evergreen\_reference\_2009\.txt](<../data/corpus/evergreen_reference_2009.txt>); document ID: DOC-e6aa9f8c6308ab748459f87b578a0df9df9c865b7911bac3686e865963b7af6f; normalized lines 148–148.

> - Weeding report with date of last circulation \(partially available\)

### REQ-166 — Supported Web Browsers for Web-Based Management Processes

- Internal key: REQ-57d4471cbfbb6a1e9bb81db9db1d22628d2eef73c0571b9a984287b69aa4a311
- Type: nonfunctional
- Priority: P3
- Priority basis: explicitly specified
- Priority rationale: The supplied review identifies browser compatibility as Medium Priority, which maps to P3; the priority is explicit in the review evidence\.
- Originating candidates: CAND-87f6537aa97ea78cb30dfedef331ba005416a81ba2c263775aea047f08fdee01

If the Management Processes are web-browser based, they shall be accessible through Microsoft Internet Explorer version 6\.0 and later and Mozilla Firefox version 2\.0 and later\.

Sources and evidence:

Source: [meeting\_minutes/meeting\_2009-07-20\_minutes\.txt](<../data/corpus/meeting_minutes/meeting_2009-07-20_minutes.txt>); document ID: DOC-5ab1dd8bc97af3b1ab2e378495f0e0d75fd501fcc19f923c0d8fda831074281b; normalized lines 88–93.

> OE-4: If web-browser based, Management Processes shall be accessible through
>       Microsoft Internet Explorer \(v\.6\.0 and later\) and Mozilla Firefox
>       \(v\.2\.0 and later\)\.
>       \[Discussion: We need to support both IE and Firefox because different
>       libraries standardize on different browsers\. IE 6 is still common in
>       our library environments, even though it's old\.\]

### REQ-167 — Library Manager Reporting Role with Limited Template Modification

- Internal key: REQ-57d547fd6ff212c9aec7fd87134baa5066d84fc33e8040212bf6d41b12ded96f
- Type: functional
- Priority: P2
- Priority basis: inferred
- Priority rationale: The role supports governed reporting and template administration; the source does not assign a priority\.
- Originating candidates: CAND-e5115ecaf6920136b1dfe042bfd2f53f8cae050f03c89f45f59a98c8924a2fc1

The system shall support a Library Manager role that can run approved reports and perform limited template modification\.

Sources and evidence:

Source: [meeting\_tech\_subcommittee\_2009-06-30\.txt](<../data/corpus/meeting_tech_subcommittee_2009-06-30.txt>); document ID: DOC-e081aa7bd57bf5e59c75a8a86f592124757b74dff1ee0df4badc10c025092d96; normalized lines 70–71.

> - Library Manager: Run approved reports, limited template modification
> - Staff: Run reports within assigned permissions

### REQ-168 — Aged Debt Report

- Internal key: REQ-57fb8a54977b6db12b57e20498ac9064868dc8aee8dcd74d0926e9ced8ba31cb
- Type: functional
- Priority: P2
- Priority basis: inferred
- Priority rationale: Debt reporting supports financial and account management, but no explicit priority is supplied\.
- Originating candidates: CAND-369c6c290940ad6a6db39f2a442d83c2509ddad3633f54eec6232091900923f9

The system shall provide an Aged Debt report\.

Sources and evidence:

Source: [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>); document ID: DOC-091180de9b2d4ea83267d989411ac89f415d4def3bbf7cd51651fb7fda8d8bf9; normalized lines 586–586.

> - Aged Debt

### REQ-169 — Schedulable Purging and Cleanup Utility

- Internal key: REQ-589c3576aebfacb7b5807625c034e0a61c7f3f01de66ed30aeb47cd59177c767
- Type: functional
- Priority: P2
- Priority basis: inferred
- Priority rationale: Automated cleanup affects ongoing system administration and data maintenance, but the source does not identify it as critical or mandatory compliance\.
- Originating candidates: CAND-bbb60c3bd1e345099f66d8da87f953cd8cd5582b8aaf9a348e83c816b0219409

The purging or cleanup utility shall be schedulable to run automatically\.

Sources and evidence:

Source: [conversations/conv\_pines021\_item\_purging\.eml](<../data/corpus/conversations/conv_pines021_item_purging.eml>); document ID: DOC-74ccbb6ac77183c0d1b34b1e79ed8fcbbfb4e7525cb33798c3af832fed733ad8; normalized lines 111–112.

> Also wondering - can the purging utility be scheduled? Like, run automatically
> at the end of each year?

### REQ-170 — Item Status Conversion Report

- Internal key: REQ-591bc8ca11ea6dc208fde918b44c2e8ad2095be7c77dca7f8454b9fd5e63cd04
- Type: functional
- Priority: P2
- Priority basis: inferred
- Priority rationale: This supports an operational item-management process with substantial workflow impact\.
- Originating candidates: CAND-9edfcf7595c2da9e90872e6648b71b664e9c63f27fb0ca1c71576927cdf47ecc

The system shall provide a report to assist in converting items from one status to another\.

Sources and evidence:

Source: [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>); document ID: DOC-091180de9b2d4ea83267d989411ac89f415d4def3bbf7cd51651fb7fda8d8bf9; normalized lines 382–383.

> The system should have a report to assist in the conversion of items from one
> status to another\. The system should provide a last copy report that singles

### REQ-171 — Inventory and Capacity Reports for Daily Operations

- Internal key: REQ-599ef7ad7e23b8152747ea9b240ba344c70cf6771ee0ef8a59ab08bb411a8964
- Type: functional
- Priority: P2
- Priority basis: inferred
- Priority rationale: The source states that branch managers use these reports daily, indicating substantial operational impact; the source does not define an explicit priority or resolve the capacity measure\.
- Originating candidates: CAND-aa81220e81bfbcc08b052a4c6d30a8014be4c1806c478255a4bb64550c0aaab5

The system shall provide inventory and capacity reports for staff use in daily operations\.

Sources and evidence:

Source: [meeting\_minutes/meeting\_2009-07-20\_minutes\.txt](<../data/corpus/meeting_minutes/meeting_2009-07-20_minutes.txt>); document ID: DOC-5ab1dd8bc97af3b1ab2e378495f0e0d75fd501fcc19f923c0d8fda831074281b; normalized lines 34–36.

> LaToya Davidson \(Twin Lakes\): Spoke with 3 branch managers\. Key themes:
>   - Inventory and capacity reports are used daily
>   - Financial report needs are understood at the director level

### REQ-172 — Role- and Group-Based Permission Administration

- Internal key: REQ-5a284fdd2acf85ac2a5fa309add5563ac5ee71025a228f5a93d5f91f421666de
- Type: functional
- Priority: P1
- Priority basis: inferred
- Priority rationale: Inferred as critical because the evidence requires role- and group-based access control that is easy to administer\.
- Originating candidates: CAND-86364bc65fe5795bab9b2afd62dc3b563b55ce8de564914f84eaaf3d3552b8be

Permission management shall be controlled through security groups and/or roles, allowing access control for individuals, workgroups, and arbitrary staff groups; changing a user's permissions shall be achievable by changing the user's role assignment\.

Sources and evidence:

Source: [interview\_sysadmin\_2009-05-10\.txt](<../data/corpus/interview_sysadmin_2009-05-10.txt>); document ID: DOC-b1738fd7a6de9498f19ede6747ba156ecb29ead86ad1c9a2768b53e862ece1a9; normalized lines 82–86.

> The permission system needs to be controlled through security groups and/or
> "roles\." This allows access control for individuals, workgroups, and arbitrary
> staff groups\. The system needs to make it easy to administer these roles\.
> Changing someone's permissions should be a simple matter of changing their
> role assignment\.

### REQ-173 — Staff Productivity and Workflow Analysis Tools

- Internal key: REQ-5a93004d416ccf73bd950141c08247c1c6dd0b9d8bdf01558a37b7535151fd1a
- Type: functional
- Priority: P2
- Priority basis: inferred
- Priority rationale: The source identifies staff productivity and workflow analysis as a management-process capability\.
- Originating candidates: CAND-3d7d1adf6265c0cb70ba8626dc95e7c75b73d00c51300a117c73b6c6797c39de

The Management Processes shall provide tools to analyze staff productivity and workflow\.

Sources and evidence:

Source: [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>); document ID: DOC-091180de9b2d4ea83267d989411ac89f415d4def3bbf7cd51651fb7fda8d8bf9; normalized lines 89–89.

>   - Analyzing staff productivity and workflow\.

### REQ-174 — Overdue items contact report

- Internal key: REQ-5afd585d9b2f57d52413965c311f679cd5c7c541f4e9323fe937e5f9ec888cd6
- Type: functional
- Priority: P2
- Priority basis: inferred
- Priority rationale: The report supports important overdue-item and patron-service operations; the source does not establish a more specific priority\.
- Originating candidates: CAND-8a6f0b6380454602a1b0b0e0996bd5d1dd0c612bc792d19725dc88d5dc279636

The system shall provide a report of items more than XX days overdue that includes patron contact information\.

Sources and evidence:

Source: [evergreen\_reference\_2009\.txt](<../data/corpus/evergreen_reference_2009.txt>); document ID: DOC-e6aa9f8c6308ab748459f87b578a0df9df9c865b7911bac3686e865963b7af6f; normalized lines 143–143.

> - Items more than XX days overdue with patron contact info \(not available\)

### REQ-175 — Patron Count by Survey Answer

- Internal key: REQ-5b48a59183426f580c57b6ce999aa91e6114d0ef935332cbe18886261347266b
- Type: functional
- Priority: P3
- Priority basis: inferred
- Priority rationale: This is a specific reporting capability and appears useful, but no source indicates that it is essential to core operation\.
- Originating candidates: CAND-28ec7e2e9f62873d7c2eaa7a5ce673f1c0b31b87d45039e66ab156f2af41bd4a

The system shall provide a Patron Count by Survey Answer report\.

Sources and evidence:

Source: [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>); document ID: DOC-091180de9b2d4ea83267d989411ac89f415d4def3bbf7cd51651fb7fda8d8bf9; normalized lines 551–551.

> - Patron Count by survey answer

### REQ-176 — Patron Financial Records, Updates, and Balance Queries

- Internal key: REQ-5b7f75eb32b7d2d3111fda99ebbaaaeb015a65c79aeaf381f972db998f97d783
- Type: functional
- Priority: P2
- Priority basis: inferred
- Priority rationale: Financial record tracking and account queries support library administration; the source does not assign a priority\.
- Originating candidates: CAND-e2d8a90f1125d0274258568a115d6b073ce5208aa5d4e655569a8c7b6fa7af05

The system shall attach fines, charges, waivers, and ecommerce transactions to patron and item records; track fines waived and payments made per library; support updates to financial information; and allow staff to query patron accounts with balances greater than a specified dollar amount\.

Sources and evidence:

Source: [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>); document ID: DOC-091180de9b2d4ea83267d989411ac89f415d4def3bbf7cd51651fb7fda8d8bf9; normalized lines 467–471.

> 13\.3 Financial Data \(Patrons\)
> Fines, charges, waivers, and ecommerce transactions are attached to patron
> and item records\. System tracks fines waived and payments made per library\.
> Financial information can be updated easily\. As an example, a staff user can
> easily query patron accounts with balances greater than X dollars\.

### REQ-177 — Circulation Breakdown by Transaction Type

- Internal key: REQ-5b89e4b3283430f8a9ee73a302b4203724a9941d38441c9049a46d9f90b513cd
- Type: functional
- Priority: P2
- Priority basis: inferred
- Priority rationale: Circulation analysis is important reporting functionality, but no explicit priority is supplied\.
- Originating candidates: CAND-5b1ba79e438750abc733e3c32807040cae32803724b67c1bb9181197eb98eb74

The system shall retrieve total circulation, including checkouts, renewals, and noncataloged transactions, with a breakdown displaying those circulation types\.

Sources and evidence:

Source: [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>); document ID: DOC-091180de9b2d4ea83267d989411ac89f415d4def3bbf7cd51651fb7fda8d8bf9; normalized lines 644–645.

> - Ability to retrieve total circ including checkouts, renewals, and noncats
>   with a breakdown displaying those circ types

### REQ-178 — Batch Convert Item Status Including 100 Missing to Discard/Weed

- Internal key: REQ-5bd98881a310ed27591aae26e24bbb8768c56675bd8037422ee1590ab9baaa97
- Type: functional
- Priority: P2
- Priority basis: inferred
- Priority rationale: Batch status conversion supports important collection operations and explicitly includes the supplied example, but the source does not assign an explicit priority\.
- Originating candidates: CAND-b868676e9882ab79898743955e3ddf5a37a71a52fefe5be5d8b541420cbe0b1e

The system shall provide the ability to convert item statuses in batch, including changing 100 items from "missing" to "discard/weed\."

Sources and evidence:

Source: [interview\_cataloging\_2009-05-08\.txt](<../data/corpus/interview_cataloging_2009-05-08.txt>); document ID: DOC-a79fab45108210e6bce7d92153dfcf055f2ef6b2cdab49a3f6f5717a3e35f29f; normalized lines 77–79.

> We also need a report to assist in converting items from one status to another\.
> Sometimes I need to change 100 items from "missing" to "discard/weed" in batch\.
> 

### REQ-179 — Scalable Batch Updates Processed in Smaller Batches to Avoid Locking

- Internal key: REQ-5bf8de1177bd44fdf466b4b93bd0a78b33e82d5d075efbf515767989daa898db
- Type: nonfunctional
- Priority: P2
- Priority basis: inferred
- Priority rationale: The source identifies scalability and database-lock avoidance as operational concerns for a collection of 9\.6 million items, but does not assign a formal priority level\.
- Originating candidates: CAND-0894ac3888f6c691fab1653bd623b85a5aefe94711183328344e9834c14dee82

The system shall process large-collection batch updates efficiently and in smaller batches to avoid locking the database\.

Sources and evidence:

Source: [conversations/conv\_pines018\_item\_transfer\.eml](<../data/corpus/conversations/conv_pines018_item_transfer.eml>); document ID: DOC-a47eb1f11286ff9099687b72a901e4a6ed2455b431087c0742aa78583c5bd80a; normalized lines 64–66.

> One concern: with 9\.6 million items, batch updates need to be efficient\.
> We should process in smaller batches to avoid locking the database\.
> 

### REQ-180 — Reports for Missing Specified MARC Fields

- Internal key: REQ-5c605d382a1dcee3081b02e18075da93386a3e9c410539a8d71481a41b218f97
- Type: functional
- Priority: P2
- Priority basis: inferred
- Priority rationale: This supports data quality management and has substantial cataloging impact\.
- Originating candidates: CAND-a5eca48fbf62dfb6cb539b330c1c9679bc5108bae97c0a7d35bbfa1d5076f69f

The system shall provide reports listing bibliographic records missing specified MARC fields\.

Sources and evidence:

Source: [evergreen\_reference\_2009\.txt](<../data/corpus/evergreen_reference_2009.txt>); document ID: DOC-e6aa9f8c6308ab748459f87b578a0df9df9c865b7911bac3686e865963b7af6f; normalized lines 153–153.

> - Bib Records missing specific MARC fields \(not available\)

### REQ-181 — Item Value Reports

- Internal key: REQ-5cfb0dc5742fa3cb607c8f6c2d7c664361e0f4fca4dc083389d678255e4d20e0
- Type: functional
- Priority: P2
- Priority basis: inferred
- Priority rationale: Collection valuation supports significant management and collection decisions; the source does not establish a more specific priority\.
- Originating candidates: CAND-8f4ab5a0f27bcce171b64e4a7989b6f7b263efd87d7050b53102302c3b1ab5a9

The system shall generate reports of item value based on item-record data for the entire collection or a specified portion, including portions such as items with Longoverdue status, DVDs in the children's collection, or the entire collection\.

Sources and evidence:

Source: [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>); document ID: DOC-091180de9b2d4ea83267d989411ac89f415d4def3bbf7cd51651fb7fda8d8bf9; normalized lines 457–461.

> 13\.1 Value of Items Report
> The system can generate a report of the value of items \(based on data in item
> record\) in the entire collection or a portion\. Example: staff can obtain value
> of all items with status of longoverdue, or value of all DVDs in children's
> collection, or value of entire collection\.

### REQ-182 — CSV Report Export for Outreach Systems

- Internal key: REQ-5d12a8386e04e1bccd898a6b601866da3df48a462fdf976ea9d6d3b07bdb4443
- Type: functional
- Priority: P2
- Priority basis: inferred
- Priority rationale: External-system export supports operational workflows and interoperability, but no explicit priority is supplied\.
- Originating candidates: CAND-5a3fdea2897edeeabf8d04af154117b990ec6f7b83fca597595119b419656fe2

The system shall make reports exportable for use in external outreach systems and shall support CSV format\.

Sources and evidence:

Source: [conversations/conv\_pines024\_inactive\_patrons\.eml](<../data/corpus/conversations/conv_pines024_inactive_patrons.eml>); document ID: DOC-705ab8a51bf22b7b619dae61bf8d2be1cf2487e749f13e7ac55fdde430357793; normalized lines 117–118.

> Also, the report should be exportable\. We upload it to our outreach system\.
> 

Source: [conversations/conv\_pines024\_inactive\_patrons\.eml](<../data/corpus/conversations/conv_pines024_inactive_patrons.eml>); document ID: DOC-705ab8a51bf22b7b619dae61bf8d2be1cf2487e749f13e7ac55fdde430357793; normalized lines 142–142.

> - Exportable format \(CSV\)

### REQ-183 — New Patron Count Report

- Internal key: REQ-5d200b5f411347a1ae724837856c65f114262a04b6ffb7e6acb4c4bb35703dba
- Type: functional
- Priority: P3
- Priority basis: inferred
- Priority rationale: This is a specific reporting capability and is not identified as essential to basic operation\.
- Originating candidates: CAND-30db376939b250eefe320bddad610e9b173cae36564c9184f20354e1b5b1c2c9

The system shall provide a New Patron Count report showing patrons added during the previous month by demographic category\.

Sources and evidence:

Source: [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>); document ID: DOC-091180de9b2d4ea83267d989411ac89f415d4def3bbf7cd51651fb7fda8d8bf9; normalized lines 545–545.

> - New Patron Count \(patrons added the previous month by Demographic Category\)

### REQ-184 — Items in Transit to Destination Library Report

- Internal key: REQ-5dae62739cb9193fac81f21e9bb5fc95e6b8caac397300a4d5794d8b89aa54ce
- Type: functional
- Priority: P2
- Priority basis: inferred
- Priority rationale: The report supports operational delivery visibility, but the source does not assign a formal priority level\.
- Originating candidates: CAND-017827c3eed0eb15eaa895056eae71c2ab1f8c8dd16c835a5c0e1f9dd93e24e5

The system shall provide a report of items in transit to a destination library\.

Sources and evidence:

Source: [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>); document ID: DOC-091180de9b2d4ea83267d989411ac89f415d4def3bbf7cd51651fb7fda8d8bf9; normalized lines 578–578.

> - Items In Transit to Destination Library

### REQ-185 — Preview and Confirm Changes Before Applying Location Updates

- Internal key: REQ-5dd637df0254d190379e13a7e74eefa49af71d9370ff0809362ab7b723e5595a
- Type: functional
- Priority: P1
- Priority basis: inferred
- Priority rationale: Preview and confirmation reduce the risk of unintended bulk operational changes and therefore protect data and inventory integrity\.
- Originating candidates: CAND-b5cdcb15e82fc847019ec7a3597a3162084372734de669d37189d989e7a5b4ee

The system shall show a preview and confirmation before making changes, including the number of items affected and their source and destination locations when applicable\.

Sources and evidence:

Source: [conversations/conv\_pines018\_item\_transfer\.eml](<../data/corpus/conversations/conv_pines018_item_transfer.eml>); document ID: DOC-a47eb1f11286ff9099687b72a901e4a6ed2455b431087c0742aa78583c5bd80a; normalized lines 99–101.

> Also, the utility should show a preview before making changes\. "If you
> run this now, 25 items will be moved from Dalton-Whitman to Mobile
> Library Unit 3\. Confirm?"

### REQ-186 — Reports Interface Usability Redesign

- Internal key: REQ-5e771e50870e3506a919dd6d073f0b9d48ad3c56cb48f7f09dc9f6ad53ece2e7
- Type: functional
- Priority: P2
- Priority basis: inferred
- Priority rationale: The source identifies staff difficulties with the current interface, indicating substantial usability impact, but provides no explicit priority\.
- Originating candidates: CAND-5d4c3e49c526478bc803fed1e0a75b2117ee9b3fdcb32ef3c5fddfd2177cde81

The reporting system redesign shall address the difficulties library staff experience with the current Evergreen reports interface\.

Sources and evidence:

Source: [meeting\_minutes/meeting\_2009-03-15\_minutes\.txt](<../data/corpus/meeting_minutes/meeting_2009-03-15_minutes.txt>); document ID: DOC-defef992db2ae0e10167fd94902eac93f82c59c4c070df030ca2f77811082818; normalized lines 25–27.

> group was formed in late February 2009 following discussions at the PINES
> Annual Conference about difficulties library staff were experiencing with the
> current reports interface in Evergreen\.

### REQ-187 — Transfer Audit Logging

- Internal key: REQ-5f2c8ff886717769aeec82cd97b19e3f52e62c21b4eb706da27aa226082dae96
- Type: nonfunctional
- Priority: P2
- Priority basis: inferred
- Priority rationale: Audit logging is an important accountability control, but the source does not assign a formal priority level\.
- Originating candidates: CAND-0a9f1160133ccb14eb9bcd025b8f46d252373ed0a30cc5acd6e5906250064d64

The system shall track and log all item transfers for audit purposes\.

Sources and evidence:

Source: [conversations/conv\_pines018\_item\_transfer\.eml](<../data/corpus/conversations/conv_pines018_item_transfer.eml>); document ID: DOC-a47eb1f11286ff9099687b72a901e4a6ed2455b431087c0742aa78583c5bd80a; normalized lines 62–62.

> 6\. Logging - track all transfers for audit purposes\.

### REQ-188 — Include Null and Blank Fields in Report Results

- Internal key: REQ-5fd6fea533086daf9cb437b66554dd8907feda280ecdeef6a63b923718f61001
- Type: nonfunctional
- Priority: P2
- Priority basis: inferred
- Priority rationale: Preserving null and blank data affects reporting completeness and interpretation; no explicit source priority is provided\.
- Originating candidates: CAND-f52704325b6492235058eae00ee3cfba0e22b93397bca5e607a55bab9ae53a52

The system shall include all null and blank fields in report results regardless of the filters or displayed fields selected\.

Sources and evidence:

Source: [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>); document ID: DOC-091180de9b2d4ea83267d989411ac89f415d4def3bbf7cd51651fb7fda8d8bf9; normalized lines 653–654.

> - All nulls and blank fields must be included in the results no matter what is
>   being filtered or displayed

### REQ-189 — Supported Server Environment

- Internal key: REQ-602064e99e776378e6114c0a1a455ed14b5949d8f1ffae03f8458ffaf1672422
- Type: nonfunctional
- Priority: P2
- Priority basis: explicitly specified
- Priority rationale: The source explicitly marks this requirement high priority, which maps to P2\.
- Originating candidates: CAND-59c960798b3709e469a8dafc5a451bf9e5193ec69eea2ca93be96efc30ede3e7

The system shall operate on a Linux or Solaris server environment\.

Sources and evidence:

Source: [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>); document ID: DOC-091180de9b2d4ea83267d989411ac89f415d4def3bbf7cd51651fb7fda8d8bf9; normalized lines 132–133.

> OE-2: The system must operate on a Linux or Solaris server environment\.
>       \[\* High Priority\]

### REQ-190 — Items Edited Count Report

- Internal key: REQ-60428b53a0ec5a3f58130ad395cc7444396eebf5af4fdc967546abea6d5b8d59
- Type: functional
- Priority: P3
- Priority basis: inferred
- Priority rationale: The report is useful for operational analysis but is not identified as essential to basic operation\.
- Originating candidates: CAND-616e5417ae8350a7d2a5c3067d853a74b04b6ff914caac37a25163d9764a6ea7

The system shall provide an Items Edited Count report\.

Sources and evidence:

Source: [evergreen\_reference\_2009\.txt](<../data/corpus/evergreen_reference_2009.txt>); document ID: DOC-e6aa9f8c6308ab748459f87b578a0df9df9c865b7911bac3686e865963b7af6f; normalized lines 141–141.

> - Items Edited Count \(not available\)

### REQ-191 — Patron Geographic Count Reports by Geography

- Internal key: REQ-612f860863b073151afb50afc992153a1eac4c946e867a507a1d3da79697f1c0
- Type: functional
- Priority: P2
- Priority basis: inferred
- Priority rationale: Geographic patron reporting is important management functionality, but no explicit source priority is provided\.
- Originating candidates: CAND-fb5c37891da74cb7d7bed2c72a7e15e7278b5c71ad4ad30ba252a58a575de963

The system shall provide patron count reports by county, city, and ZIP code\.

Sources and evidence:

Source: [evergreen\_reference\_2009\.txt](<../data/corpus/evergreen_reference_2009.txt>); document ID: DOC-e6aa9f8c6308ab748459f87b578a0df9df9c865b7911bac3686e865963b7af6f; normalized lines 156–156.

> - Patron Count by County, City, &amp; Zip Code \(not available\)

### REQ-192 — In-Transit Item Identification by Null Arrival and Age

- Internal key: REQ-6179da66c87f0417bd0cadc989f3fcefd1be1eea044bd602b99b69765d2df261
- Type: functional
- Priority: P2
- Priority basis: inferred
- Priority rationale: Inferred as important status-reporting functionality; no explicit source priority is supplied\.
- Originating candidates: CAND-6696fecd6573f7f647894da5f27c46ff2f2b484d1b8b0f761af83c0c5ab51a43

For reporting purposes, the system shall identify an item as in transit when its arrival date is null and its departure date is more than X days ago\.

Sources and evidence:

Source: [conversations/conv\_pines019\_020\_missing\_intransit\.eml](<../data/corpus/conversations/conv_pines019_020_missing_intransit.eml>); document ID: DOC-b233b12122cae48b5821d685f6dc058d2d2e3cc8d7f77622fa4e7e55bddc5399; normalized lines 66–67.

> For in-transit items, we need to check the transit table for items where
> the arrival date is null and the departure date is more than X days ago\.

### REQ-193 — Patron Count by Profile Group

- Internal key: REQ-621c7b4b493f852210632e3630560b41111338716b7188a5414e5ac363130401
- Type: functional
- Priority: P3
- Priority basis: inferred
- Priority rationale: This is a useful demographic report but is not identified as essential for basic operation\.
- Originating candidates: CAND-0d9b4b8af2d1d040cf7f2526e403c8d1e67217a3a248ade4106438fc2cd0ab03

The system shall provide a report presenting patron count grouped by profile group\.

Sources and evidence:

Source: [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>); document ID: DOC-091180de9b2d4ea83267d989411ac89f415d4def3bbf7cd51651fb7fda8d8bf9; normalized lines 550–550.

> - Patron Count by Profile Group

### REQ-194 — Enterprise Library Automation Management Processes

- Internal key: REQ-6293a5e0dd8f1acbfbff85ef30ca8878cf8d661121ddd3167f6a7217aecba717
- Type: nonfunctional
- Priority: P2
- Priority basis: inferred
- Priority rationale: Enterprise-level integration is an explicit architectural assumption; the source does not assign a priority\.
- Originating candidates: CAND-da968ff4766f186ea30fc73e2596c1298415198e067063b8dd1a066f5a812ace

The system shall provide Management Processes as part of an enterprise-level Library Automation System\.

Sources and evidence:

Source: [meeting\_minutes/meeting\_2009-07-20\_minutes\.txt](<../data/corpus/meeting_minutes/meeting_2009-07-20_minutes.txt>); document ID: DOC-5ab1dd8bc97af3b1ab2e378495f0e0d75fd501fcc19f923c0d8fda831074281b; normalized lines 167–170.

> AS-1: Management Processes are part of an enterprise-level Library Automation
>       System\.
>       \[Discussion: This means we can rely on the infrastructure being
>       enterprise-grade\. Evergreen is that system for PINES\.\]

### REQ-195 — Activity Cross-Tabulation Reports

- Internal key: REQ-62beac27fe28410d78c0303986a176d451292baed407e42c4f0420ff1f3ec915
- Type: functional
- Priority: P2
- Priority basis: inferred
- Priority rationale: Supports substantial operational and management analysis\.
- Originating candidates: CAND-d47876d538df701a226c072d724c60792ae217900399576a28e03064dc718087

The system shall provide activity reports showing check-outs, check-ins, holds placed, and holds filled, and shall allow cross-tabulation by terminal, branch, library system, hour, patron age range, patron type, and patron location\.

Sources and evidence:

Source: [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>); document ID: DOC-091180de9b2d4ea83267d989411ac89f415d4def3bbf7cd51651fb7fda8d8bf9; normalized lines 265–269.

> Activity reports should indicate traffic and volume of use, displaying
> statistics on check-outs, check-ins, holds placed, and holds filled\. It
> should be possible to cross-tabulate per terminal, per branch, per library
> system, per hour, per patron age range, per patron type, and per patron
> location\.

### REQ-196 — Management-Focused Reporting and Analysis Tools

- Internal key: REQ-639b75f2232b422699bae6fbfbcc0b33927c9d407c66d670db9a927932483f89
- Type: functional
- Priority: P2
- Priority basis: inferred
- Priority rationale: This defines the central user-facing purpose of the reporting system; no explicit source priority is supplied\.
- Originating candidates: CAND-fd80fac8d5e6102026d39da2dfa5206bff790fb9d9ca940117e4f201e4a1c3c3

The reporting system shall provide reports and analysis tools focused on Management Processes used by library managers, administrators, and staff for planning, evaluation, and oversight, excluding day-to-day patron-facing functions\.

Sources and evidence:

Source: [meeting\_minutes/meeting\_2009-03-15\_minutes\.txt](<../data/corpus/meeting_minutes/meeting_2009-03-15_minutes.txt>); document ID: DOC-defef992db2ae0e10167fd94902eac93f82c59c4c070df030ca2f77811082818; normalized lines 50–55.

> Jennifer Durham asked about the scope of the group's work\. Katherine explained
> that the group would focus on Management Processes - that is, reports and
> analysis tools used by library managers, administrators, and staff for
> planning, evaluation, and oversight purposes\. She clarified that this does NOT
> include day-to-day patron-facing functions \(those are part of the OPAC and
> circulation client\)\.

### REQ-197 — Collection Use Reporting and Analysis

- Internal key: REQ-64adc45b62a0adeee8872a8ce2ec779342e6c0bd68bd45bc15314bc308c86458
- Type: functional
- Priority: P2
- Priority basis: inferred
- Priority rationale: Collection-use analysis supports collection management decisions; the source does not assign a priority\.
- Originating candidates: CAND-e462dabc37f958dcbf7672c9138236edf7582ebba84ff06c420a75165f77ad0e

The system shall provide reporting and analysis capabilities for the library collection and its use by patrons\.

Sources and evidence:

Source: [meeting\_minutes/meeting\_2009-03-15\_minutes\.txt](<../data/corpus/meeting_minutes/meeting_2009-03-15_minutes.txt>); document ID: DOC-defef992db2ae0e10167fd94902eac93f82c59c4c070df030ca2f77811082818; normalized lines 59–60.

>   - Analyzing the Library collection and its use by patrons
>   - Analyzing branch capacity and optimal distribution of the collection

### REQ-198 — List Patrons by Expiration Date

- Internal key: REQ-65badf429e7052b0df4fa26d58eed3317e69ff5948598c6e323300b5d343dd62
- Type: functional
- Priority: P2
- Priority basis: inferred
- Priority rationale: The list supports patron-account administration, but the source does not assign an explicit priority\.
- Originating candidates: CAND-b7b00d863ed78b634f3e33820989792b2e3b8e53b323b074e41bb47a942dd548

The system shall provide a list of patrons by expiration date\.

Sources and evidence:

Source: [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>); document ID: DOC-091180de9b2d4ea83267d989411ac89f415d4def3bbf7cd51651fb7fda8d8bf9; normalized lines 554–554.

> - List of Patrons by Expiration Date

### REQ-199 — Report deleted WorldCat last-copy items

- Internal key: REQ-66259eeb658e0ea5b8f23220f67db490ea0fc5fc54446cc5ebb6134458b6823b
- Type: functional
- Priority: P1
- Priority basis: explicitly specified
- Priority rationale: The source identifies the last-copy report as critical for preventing and addressing WorldCat cataloging problems\.
- Originating candidates: CAND-8f1c19d45b9073470c0da42f89684e4ab23018ef9076d075f88ae6a349770dab

The system shall provide a report listing items deleted that were the last copy owned by the library system, to support updating WorldCat\.

Sources and evidence:

Source: [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>); document ID: DOC-091180de9b2d4ea83267d989411ac89f415d4def3bbf7cd51651fb7fda8d8bf9; normalized lines 638–639.

> - Ability to get a list of items deleted that was the last copy owned by the
>   library system in order to update WorldCat

### REQ-200 — Staff Report Authoring and Templates

- Internal key: REQ-66e6a5d7fd0934baf00c674101170b84d28bf0dad8a44657a32166eca1238745
- Type: functional
- Priority: P2
- Priority basis: inferred
- Priority rationale: Supports adaptation of reports to local management needs\.
- Originating candidates: CAND-d506611962290660a9487a07c28c927e422444f70018992b80c7aec89aba5a98

The system shall allow staff to create report content and report templates\.

Sources and evidence:

Source: [meeting\_minutes/meeting\_2009-03-15\_minutes\.txt](<../data/corpus/meeting_minutes/meeting_2009-03-15_minutes.txt>); document ID: DOC-defef992db2ae0e10167fd94902eac93f82c59c4c070df030ca2f77811082818; normalized lines 87–91.

>   Staff: Paid employees of PINES member libraries involved in designing and
>          providing services\. This includes front-line circulation staff,
>          supervisors, etc\.
>          \[Jenny: Staff are our primary content creators for reports\]
> 

### REQ-201 — Periodic Management Reporting Workflow Support

- Internal key: REQ-6727386b1b5f3b1aad9757665f43a8e1c49fc0d5e484cc5dc4468425f88f7eca
- Type: nonfunctional
- Priority: P2
- Priority basis: inferred
- Priority rationale: The source identifies monthly board reporting and quarterly assessment as management needs with substantial impact, but does not establish a critical or compliance priority\.
- Originating candidates: CAND-c36378b0868747bcdc9f5ecc8e701daf4854d626694dc9ae1f7a9b5e562cd73e

The reporting capability shall support periodic management reporting workflows, including use for monthly board reports and quarterly assessments; the supplied evidence does not specify the required format, scheduling, or delivery mechanism\.

Sources and evidence:

Source: [conversations/conv\_pines014\_material\_volume\.eml](<../data/corpus/conversations/conv_pines014_material_volume.eml>); document ID: DOC-f10d646016479a881ae8ff4ab4043844ee55a671d71f1943623db3fbb5589d8a; normalized lines 8–9.

> We need this for our monthly board report and I'm currently pulling it
> manually from three different screens\. :\(

Source: [conversations/conv\_pines014\_material\_volume\.eml](<../data/corpus/conversations/conv_pines014_material_volume.eml>); document ID: DOC-f10d646016479a881ae8ff4ab4043844ee55a671d71f1943623db3fbb5589d8a; normalized lines 53–54.

> I second this request\. At Twin Lakes we need this for our quarterly
> assessment\. Can we make the categories customizable? Different libraries

### REQ-202 — Selected MARC Fields on Single Row Reports

- Internal key: REQ-68c19a7a8f1c5f6d44675a054553560d4772f4867db99fd4799dee01b53a323e
- Type: functional
- Priority: P2
- Priority basis: inferred
- Priority rationale: Inferred as important bibliographic reporting functionality; no explicit source priority is supplied\.
- Originating candidates: CAND-677a4b1257a222cc56e8f4c8c3f24ea4728da6b12ba02d1a16f2a0ee89e8cc18

The system shall allow selected MARC fields to appear on a single row of report data\.

Sources and evidence:

Source: [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>); document ID: DOC-091180de9b2d4ea83267d989411ac89f415d4def3bbf7cd51651fb7fda8d8bf9; normalized lines 664–665.

> - Ability to pull MARC record fields so that they appear on a single row of data
> - Ability to run a report on transactions that occurred on x date and time on x

### REQ-203 — Items Sent for Holds Report

- Internal key: REQ-68d84947254ab8d744707e5dc721c2db41e8ae7424e4465632eb5a7b903165a6
- Type: functional
- Priority: P3
- Priority basis: inferred
- Priority rationale: Inferred as useful operational reporting functionality; no explicit source priority is supplied\.
- Originating candidates: CAND-64fcf15e64cf998b31773d0a516776771d9ad69c3b8075caad278de0eb85ea0e

The system shall provide an Items Sent for Holds report\.

Sources and evidence:

Source: [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>); document ID: DOC-091180de9b2d4ea83267d989411ac89f415d4def3bbf7cd51651fb7fda8d8bf9; normalized lines 563–563.

> - Items Sent for Holds

### REQ-204 — Patron and Material Use Statistics

- Internal key: REQ-69f74f64cabdcadefe6388276b5592e03cb9fbb35c6eba3a39cb0a254c14bc39
- Type: functional
- Priority: P2
- Priority basis: inferred
- Priority rationale: Behavior and material-use statistics support important planning and analytical decisions\.
- Originating candidates: CAND-1c027e89807cec1ef5670ce2cbde759ac8e2d080781acf61afd38ca66ea85c45

The system shall produce statistics usable to understand and predict patron behavior and material use, including average return time for a book, likelihood that a book will be renewed, and the percentage of check-outs at a branch that are renewals\.

Sources and evidence:

Source: [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>); document ID: DOC-091180de9b2d4ea83267d989411ac89f415d4def3bbf7cd51651fb7fda8d8bf9; normalized lines 309–315.

> 9\.1 Patron Behavior and Use Analysis
> The system should produce statistics that can be used to understand and predict
> patron behavior and use of materials\. For example:
>   - How quickly is a particular book returned, on average?
>   - How likely is a particular book to be renewed?
>   - What percent of check-outs at a particular branch are renewals?
> 

### REQ-205 — Optional Streamlined Staff Login Without Requiring Card-Based Login

- Internal key: REQ-6a1dbfd822fabd0295f7513c5723a9769f530a76696a84f1f1a639cb0a1979fc
- Type: functional
- Priority: P2
- Priority basis: inferred
- Priority rationale: Inferred as high priority because the evidence requests streamlined staff login while explicitly requiring username/password as an available alternative\.
- Originating candidates: CAND-775b519373198af56fa52273a4ebaafe582d46785615ae3fc014867e0bb1dcdb

The system shall support streamlined staff login methods such as employee badge card swipe and shall also allow individual username/password login; card-based login shall not be required\.

Sources and evidence:

Source: [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>); document ID: DOC-091180de9b2d4ea83267d989411ac89f415d4def3bbf7cd51651fb7fda8d8bf9; normalized lines 224–229.

> 8\.1 Staff Login
> The system should support streamlined methods of logging into terminals\. For
> example, a staff member could swipe a card \(like an RFID employee badge\) to
> log in, or alternatively use individual login credentials \(username and
> password\)\. The system should not REQUIRE card-based login - traditional
> username/password should also be available as a fallback\.

### REQ-206 — Recent Acquisition Volume Reports by Acquisition Date

- Internal key: REQ-6b402aa5f7e63c1bf5ab9d3d5421196826aabd03c888d564b85824bfd3f760ab
- Type: functional
- Priority: P3
- Priority basis: inferred
- Priority rationale: The source confirms that acquisition dates are tracked and requests this analytical capability, without establishing a higher priority\.
- Originating candidates: CAND-bfd13fba1a8e144a998546ce2999f68855df2c92e5c242b493475cd4a412b3d2

The reporting capability shall provide reports on volume added during recent intervals, such as the last 30, 60, or 90 days, using the acquisition date tracked in the database\.

Sources and evidence:

Source: [conversations/conv\_pines014\_material\_volume\.eml](<../data/corpus/conversations/conv_pines014_material_volume.eml>); document ID: DOC-f10d646016479a881ae8ff4ab4043844ee55a671d71f1943623db3fbb5589d8a; normalized lines 57–59.

> Also, Robert - any idea if the database tracks acquisition date? It would
> be helpful to see how much volume has been added in the last 30/60/90 days\.
> 

Source: [conversations/conv\_pines014\_material\_volume\.eml](<../data/corpus/conversations/conv_pines014_material_volume.eml>); document ID: DOC-f10d646016479a881ae8ff4ab4043844ee55a671d71f1943623db3fbb5589d8a; normalized lines 70–71.

> Yes, the database tracks acquisition date for items\. We can definitely
> build reports that show volume changes over time\.

### REQ-207 — Holds Purchase Alert Report

- Internal key: REQ-6b4ac7c91043bef6198e290d39c4af05732d1ef2a6550572638314ad791e9a76
- Type: functional
- Priority: P3
- Priority basis: inferred
- Priority rationale: The source requests this report but does not establish it as essential to basic operation\.
- Originating candidates: CAND-c6c02c59a7e9eb7b5bafe756835a8478b5dce48ad7d6e3884e6f4634e22d83b8

The system shall provide a Holds Purchase Alert report\.

Sources and evidence:

Source: [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>); document ID: DOC-091180de9b2d4ea83267d989411ac89f415d4def3bbf7cd51651fb7fda8d8bf9; normalized lines 562–562.

> - Holds Purchase Alert

### REQ-208 — Select Database Fields for Reporting Output

- Internal key: REQ-6b51df2613c7d1c37d5481b1f579482239dd0d76e1125d39c737e0af2b8bccae
- Type: functional
- Priority: P2
- Priority basis: inferred
- Priority rationale: Broad field selection supports flexible reporting, but no explicit priority is supplied\.
- Originating candidates: CAND-4f6985c368ec8194fbadb8ea2a141725bc150b4f0e8127c9a1adb3988d0b2219

The system shall allow relevant database fields to be selected for reporting rather than limiting reports to only a subset of available fields\.

Sources and evidence:

Source: [evergreen\_reference\_2009\.txt](<../data/corpus/evergreen_reference_2009.txt>); document ID: DOC-e6aa9f8c6308ab748459f87b578a0df9df9c865b7911bac3686e865963b7af6f; normalized lines 40–40.

> - Limited field selection \(not all database fields are available\)

### REQ-209 — Web Browser Compatibility for IE6 and Firefox 2

- Internal key: REQ-6c060665182d4ef51a6fb5a33e09fedd5d78f55944731f5f54d48168b4395ca9
- Type: nonfunctional
- Priority: P3
- Priority basis: explicitly specified
- Priority rationale: The source explicitly identifies this as a medium-priority requirement, mapped to P3\.
- Originating candidates: CAND-1dda307ca69a73196365fb0a88fffde3900af53bf77324997fb3db47b0305879

If the system is web-browser based, it shall be accessible through Microsoft Internet Explorer version 6\.0 and later and Mozilla Firefox version 2\.0 and later\.

Sources and evidence:

Source: [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>); document ID: DOC-091180de9b2d4ea83267d989411ac89f415d4def3bbf7cd51651fb7fda8d8bf9; normalized lines 139–141.

> OE-4: If web-browser based, the system must be accessible through Microsoft
>       Internet Explorer \(version 6\.0 and later\) and Mozilla Firefox \(version
>       2\.0 and later\)\.

### REQ-210 — Role-Based Access Control with Defined Role Levels and Scopes

- Internal key: REQ-6c95f6fdb3caa54ba215292496ef4b0f9c1559a345faf708fc3fa212ae6981f2
- Type: functional
- Priority: P1
- Priority basis: inferred
- Priority rationale: Access control protects system functions and data; P1 is inferred from its security-critical nature\.
- Originating candidates: CAND-3cdeaada135c9a0bcc8b849407b54ee0742e9283779463dd5c31a8318defba7f

The system shall implement role-based access control with the following role levels and access scopes: Patron for public OPAC access, Staff for basic circulation functions, Local Admin for branch-manager reporting and local configuration, and Global Admin for full system access\.

Sources and evidence:

Source: [interview\_sysadmin\_2009-05-10\.txt](<../data/corpus/interview_sysadmin_2009-05-10.txt>); document ID: DOC-b1738fd7a6de9498f19ede6747ba156ecb29ead86ad1c9a2768b53e862ece1a9; normalized lines 76–81.

> ROBERT: PINES uses a role-based system\. We have different levels of access:
>   - Patron \(public access through OPAC\)
>   - Staff \(basic circulation functions\)
>   - Local Admin \(branch manager - can run reports, configure local settings\)
>   - Global Admin \(IT staff - full system access\)
> 

### REQ-211 — Estimated Shelf-Space Percent Metrics by Genre and Format

- Internal key: REQ-6cbfb8b74be736536146daba8b31706978ba34d43ba390fc90eff2cfa95fb461
- Type: functional
- Priority: P3
- Priority basis: inferred
- Priority rationale: Supports collection analysis but is not identified as essential to basic operation\.
- Originating candidates: CAND-d8be353b42119d356e43ef9018d1642704f8702353d40e30b25ecf5fa2e720a6

The system shall estimate shelf space per genre and format to produce a percentage-of-total-shelf-space metric; the system shall not be constrained to a specific estimation method because shelf space is not directly tracked in the database\.

Sources and evidence:

Source: [conversations/conv\_pines016\_shelf\_space\.eml](<../data/corpus/conversations/conv_pines016_shelf_space.eml>); document ID: DOC-b507e8abe1ba7c996c1d86d688e90bcf2404694ec00528c8361f26dfc8bd82f1; normalized lines 69–73.

> 3\. Estimate shelf space per genre/format \(this is the "percentage of shelf space"\)
> 
> The tricky part is \#3\. Shelf space isn't directly tracked in the database\.
> We'd need to estimate based on item dimensions or use item count as a proxy\.
> 

### REQ-212 — Appendix A Report Types by Category

- Internal key: REQ-6cde243ede2410058103383d28345877d78037653b2f5674e57ab9e349d993be
- Type: functional
- Priority: P2
- Priority basis: inferred
- Priority rationale: The source identifies these report categories and examples as necessary, but does not assign a priority\.
- Originating candidates: CAND-e3f98bc05372108041f9475ee997e2346230d8b95fb43ad1992b0c45a1f5289f

The system shall support the report categories and example report types identified in Appendix A, including the enumerated circulation, item, and bibliographic-record report types\.

Sources and evidence:

Source: [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>); document ID: DOC-091180de9b2d4ea83267d989411ac89f415d4def3bbf7cd51651fb7fda8d8bf9; normalized lines 488–541.

> 14\. APPENDIX A - REPORT TYPES
> ================================================================================
> 
> This appendix lists the various report categories and example report types
> that have been identified as necessary\.
> 
> CIRCULATION REPORTS:
> - Check in Count
> - Checkout Count \(includes checkouts only\)
> - Items overdue by X days \(daily, shelf reading, patron contact info\)
> - Circulation Count by Circ Modifier, Cat1, and Cat2 \(Adult, YA, Juv\.\.\.\)
> - Renewals Count
> - Non-Cat Count
> - Circulation Count - total circ including checkouts, renewals, and noncats
> - Total Circulation Count \(Merging both Cat and Non-Cat circulation data\)
> - Circulation Count by Dewey
> - Circulation Count by Circ Modifier
> - Circulation Count by Shelving Location
> - Circulation Count by MARC
> - Circulation Count by Circ Location broken down by Patron County
> - Circulation Count by Circ Location broken down by Patron Home Library
> - Circulation Count by Age Demographic
> 
> ITEMS REPORTS:
> - Items Added Count
> - Items Deleted Count
> - List of Items Added
> - Items Edited Count
> - Items Count
> - List of Items by Fines Stopped Reason
> - Items Currently Checked Out
> - Items more than XX days overdue \(Overdue Materials Report\)
> - Items marked longoverdue by system
> - List of Items with a &gt; Total Use Count
> - List of Items with a &lt; Total Use Count \[Weeding Report\]
> - Last Copy Report \(last copy owned by a library system that was deleted\)
> - List of Items by Creation Date Range
> - List of Items with a status of Missing
> - List of Items in Transit by both sending library and destination library
> - Claims returned
> - List of Long Overdue
> - Weeding report \(date of last circulation and number of circs\)
> - List of items with XXX in bib record
> - Age of collection by call number or shelving location
> - Price value of collection by call number or shelving location
> - Items to be Converted \(batch converting items from one status to another\)
> 
> BIB RECORDS REPORTS:
> - Bib Records Count
> - Bib Records Edited Count
> - Bib Records Added by user by library Count
> - Bib Records with No Volumes attached
> - Bib Records missing specific MARC fields
> 

### REQ-213 — Group Report Results by Categories

- Internal key: REQ-6d646c6cee6e4425ad99cd1b86247521c86f3f318d6a3dc2d3cd31fe5d9f5e95
- Type: functional
- Priority: P2
- Priority basis: inferred
- Priority rationale: Inferred as high priority because the evidence requires category grouping and breakdowns in report results\.
- Originating candidates: CAND-863a43fb822dbf32bec12103ca27b01b6b574eb9894bb3e9ea37efc203c03ca5

The system shall group report results by categories, such as fiction/non-fiction and format\.

Sources and evidence:

Source: [conversations/conv\_pines014\_material\_volume\.eml](<../data/corpus/conversations/conv_pines014_material_volume.eml>); document ID: DOC-f10d646016479a881ae8ff4ab4043844ee55a671d71f1943623db3fbb5589d8a; normalized lines 74–76.

> 1\. Counts all items with a location = your library
> 2\. Groups by categories \(fiction/non-fiction, format, etc\.\)
> 3\. Shows breakdowns with holds count per category

### REQ-214 — Bibliographic Records Added by User and Library Report

- Internal key: REQ-6edec70821e73c8037c2cce8852e7af21a4b4d886c296a36b0c98f93dfe77cf9
- Type: functional
- Priority: P2
- Priority basis: inferred
- Priority rationale: The report is identified in the supplied reporting scope, but the source does not assign a formal priority level\.
- Originating candidates: CAND-034fecf821b645588e68748637bffd60073f797d5ef00e8ea0a60737710ee722

The system shall provide a report counting bibliographic records added by user and library\.

Sources and evidence:

Source: [evergreen\_reference\_2009\.txt](<../data/corpus/evergreen_reference_2009.txt>); document ID: DOC-e6aa9f8c6308ab748459f87b578a0df9df9c865b7911bac3686e865963b7af6f; normalized lines 152–152.

> - Bib Records Added by user by library Count \(not available\)

### REQ-215 — Accessible Standards-Compliant HTML Output

- Internal key: REQ-6f4f8f81f9f39ea5a6f385afb79b3904d261f9867fd88d2568bdea51d1a8b276
- Type: nonfunctional
- Priority: P2
- Priority basis: explicitly specified
- Priority rationale: The source explicitly identifies standards-compliant HTML as high priority, which maps to P2\.
- Originating candidates: CAND-55ea828708012ebe9e6b43418f4ff583cbb65dc59e307904f51c5ec985bf00ff

The system shall produce standards-compliant, properly structured HTML output that includes alternative text, ARIA labels, and semantic HTML\.

Sources and evidence:

Source: [interview\_sysadmin\_2009-05-10\.txt](<../data/corpus/interview_sysadmin_2009-05-10.txt>); document ID: DOC-b1738fd7a6de9498f19ede6747ba156ecb29ead86ad1c9a2768b53e862ece1a9; normalized lines 61–64.

> 
> We can't have blind staff members unable to run reports\. The HTML output
> needs to be properly structured with alt tags, ARIA labels, and proper
> semantic HTML\. And the system needs to produce standards-compliant HTML\.

### REQ-216 — Supported Reporting Platforms

- Internal key: REQ-70059418f0b496a80ec44d5d62fed2f4e62916e07835d6a738b8911d18f03d82
- Type: nonfunctional
- Priority: P1
- Priority basis: inferred
- Priority rationale: Compatibility with the stated production and disaster-recovery platforms is essential to operational continuity\.
- Originating candidates: CAND-9bc83e68a2ac35e88a62b2ea11afa35cb58e25e8664475c70717f96dc03363d1

The reporting system shall run on Red Hat Enterprise Linux 5 and Solaris 10 on SPARC, including the secondary site used for disaster recovery and reporting\.

Sources and evidence:

Source: [interview\_sysadmin\_2009-05-10\.txt](<../data/corpus/interview_sysadmin_2009-05-10.txt>); document ID: DOC-b1738fd7a6de9498f19ede6747ba156ecb29ead86ad1c9a2768b53e862ece1a9; normalized lines 31–35.

> ROBERT: Our main server is a Red Hat Enterprise Linux 5 box with dual quad-core
> processors and 32GB of RAM\. It runs PostgreSQL 8\.3 for the database\. We also
> have a secondary site that runs Solaris 10 on SPARC hardware for disaster
> recovery and reporting\. So any reporting system needs to work on both Linux
> and Solaris\.

### REQ-217 — Holds Count by Category in Volume Report

- Internal key: REQ-7030a0338f7d50d821b63e99163ff738eefe84b95bfa84ecd72b3b6ae13962eb
- Type: functional
- Priority: P2
- Priority basis: inferred
- Priority rationale: The source specifies holds counts as a required breakdown of the volume report; the source does not assign a priority\.
- Originating candidates: CAND-e4ac68a71049583f93a1b53405330a03486fa061dc63427db0c39f302316ef9a

The system shall include a holds count for each category in the volume report\.

Sources and evidence:

Source: [conversations/conv\_pines014\_material\_volume\.eml](<../data/corpus/conversations/conv_pines014_material_volume.eml>); document ID: DOC-f10d646016479a881ae8ff4ab4043844ee55a671d71f1943623db3fbb5589d8a; normalized lines 73–77.

> For the volume report, I'm thinking we need a query that:
> 1\. Counts all items with a location = your library
> 2\. Groups by categories \(fiction/non-fiction, format, etc\.\)
> 3\. Shows breakdowns with holds count per category
> 

### REQ-218 — Open Template Reporting Capability

- Internal key: REQ-7053459f4b8c9eec6a72d786f8898e8a44a63dca4a4707dbd90b059b5c00c08b
- Type: functional
- Priority: P2
- Priority basis: inferred
- Priority rationale: The review identifies open template reporting as a normatively required capability, although the supplied evidence describes it as a current-state gap rather than assigning a P-level priority\.
- Originating candidates: CAND-3d4dd0a7b7ba5877aba682afa820bdc7fb1e32db02e66281ab2256bd353fe16a

The system shall provide open template reporting capability\.

Sources and evidence:

Source: [evergreen\_reference\_2009\.txt](<../data/corpus/evergreen_reference_2009.txt>); document ID: DOC-e6aa9f8c6308ab748459f87b578a0df9df9c865b7911bac3686e865963b7af6f; normalized lines 196–196.

> - Open Template Reporting - does not exist

### REQ-219 — Pivot Table Report Output

- Internal key: REQ-7077e56b2fa35fae9851b043b8e89e48b5f3693ffc9fdde55e90733427fd3e9a
- Type: functional
- Priority: P3
- Priority basis: inferred
- Priority rationale: Pivot output enhances analysis but is not essential to basic report generation\.
- Originating candidates: CAND-1579494ea61bfcbdf1e30b269955d9aa236c97995e6467824e0ee37b61876e88

The system shall provide pivot table output capability for reports\.

Sources and evidence:

Source: [evergreen\_reference\_2009\.txt](<../data/corpus/evergreen_reference_2009.txt>); document ID: DOC-e6aa9f8c6308ab748459f87b578a0df9df9c865b7911bac3686e865963b7af6f; normalized lines 169–169.

> - No pivot table output

### REQ-220 — Query Design Interface for Reporting

- Internal key: REQ-71767e4a8974877aadfa45f23c8c696e073eb556e9109a031ec756199df6bb2b
- Type: functional
- Priority: P2
- Priority basis: inferred
- Priority rationale: This affects the breadth and usability of staff reporting and query work\.
- Originating candidates: CAND-a0e8b761f088e244420adc211f725a53a6d1fa056e421e0171e97f5728491795, CAND-a2dbdbdeff31fe58e57ad98855fad7ebd6fd9ff396eb7610eff87f18092eb208

The system shall provide a query design interface that lets staff design queries against all record types, select fields to query, select values from picklists, select regular expressions from a dropdown menu, and use Boolean operators\.

Sources and evidence:

Source: [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>); document ID: DOC-091180de9b2d4ea83267d989411ac89f415d4def3bbf7cd51651fb7fda8d8bf9; normalized lines 252–256.

> Staff should be able to:
>   - Select fields to query
>   - Select values from a picklist of possible values
>   - Select regular expressions from a drop-down menu
>   - Use a full range of Boolean operators

Source: [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>); document ID: DOC-091180de9b2d4ea83267d989411ac89f415d4def3bbf7cd51651fb7fda8d8bf9; normalized lines 256–256.

>   - Use a full range of Boolean operators

Source: [email\_report\_features\.eml](<../data/corpus/email_report_features.eml>); document ID: DOC-d9e168e0c03903021bf9e636e1d8e5f56dfcb79cc110d3839e38175a7c54344e; normalized lines 6–9.

> 1\. QUERY TOOL: We need a user-friendly interface for designing queries against
>    all record types\. Staff should be able to select fields to query, select
>    values from picklists, use regular expressions from a dropdown, and use
>    Boolean operators\.

### REQ-221 — Standards-Compliant HTML

- Internal key: REQ-71c09d3debbebd25f9b68d843e3e1898a822f74fe5a8b07376e19d8206e10bb2
- Type: nonfunctional
- Priority: P2
- Priority basis: inferred
- Priority rationale: Standards compliance supports browser and assistive-technology compatibility, but the source does not assign a P-level priority\.
- Originating candidates: CAND-26296051cb9a5061293ad3ff67a1c69578ce0b638a90671b91a4f8309d8cab05

The system shall produce standards-compliant HTML for its web-based interface, help system, and report output, and the HTML shall validate against W3C standards\.

Sources and evidence:

Source: [meeting\_tech\_subcommittee\_2009-06-30\.txt](<../data/corpus/meeting_tech_subcommittee_2009-06-30.txt>); document ID: DOC-e081aa7bd57bf5e59c75a8a86f592124757b74dff1ee0df4badc10c025092d96; normalized lines 41–47.

> 2\.2 HTML COMPLIANCE
> The system must produce standards-compliant HTML\. This was discussed in the
> context of the web-based interface, the help system, and report output\.
> 
> "We need to make sure all HTML output validates against W3C standards,"
> Robert noted\. "This isn't just about looks - it's about compatibility with
> different browsers and assistive technologies\."

### REQ-222 — Fines and Charges Reports by Time Period and Charge Type

- Internal key: REQ-71f581aa1a0bea45a7ce0aa0a3405615a81bf5fe15926091a7d3ee30d8705ca1
- Type: functional
- Priority: P2
- Priority basis: inferred
- Priority rationale: Financial reporting is important for operational oversight, but the sources do not assign a formal priority level\.
- Originating candidates: CAND-05b609dfc646cb62f50469db7ec52be926c9da3765d5a861603d491344651570

The system shall provide reports of fines and charges accrued by time period, including the last 12 months, year to date, and last month, broken down by charge type such as overdue fines, damaged-item charges, and lost-item charges\.

Sources and evidence:

Source: [email\_financial\_reports\.eml](<../data/corpus/email_financial_reports.eml>); document ID: DOC-8b6cfb3cf368b794d82567933f9c85062740814819b1e28b4837f6021cbcbee6; normalized lines 17–17.

>    - Fines and charges accrued per time period \(last 12 months, YTD, last month\)

Source: [email\_financial\_reports\.eml](<../data/corpus/email_financial_reports.eml>); document ID: DOC-8b6cfb3cf368b794d82567933f9c85062740814819b1e28b4837f6021cbcbee6; normalized lines 125–127.

>    - Fines and charges accrued per time period \(last 12 months, YTD, last month\)
>      and per type of charge \(overdue fines, damaged item charges, lost item
>      charges, etc\.\)

### REQ-223 — Last-Copy Deletion Report

- Internal key: REQ-72517b21017ecc724f617421ec665319e4099c979b03605d11db84e254798f17
- Type: functional
- Priority: P2
- Priority basis: inferred
- Priority rationale: Supports monitoring of consequential deletions\.
- Originating candidates: CAND-ca15eabcb970b4bf25099cfbc88624bb85b93034616b37921506e81974dc1984

The system shall allow users to run a report on deleted items that were the last copy in the facility\.

Sources and evidence:

Source: [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>); document ID: DOC-091180de9b2d4ea83267d989411ac89f415d4def3bbf7cd51651fb7fda8d8bf9; normalized lines 663–663.

> - Ability to run a report on deleted items that were the last copy in the facility

### REQ-224 — Report Output Formats and Scheduling Options

- Internal key: REQ-7269ca0721d9a1bdff9833b93628b75d3383dff8b9b3e9de6208d7c40cdd9670
- Type: functional
- Priority: P2
- Priority basis: inferred
- Priority rationale: The source identifies these as management-level reporting capabilities, but does not assign a formal priority level\.
- Originating candidates: CAND-0e2e731ddaee00e55c766fabc7d2a367dfb5b49b02df439c5b7d2b4ea7319787

The system shall provide multiple report output formats and expanded report scheduling options\.

Sources and evidence:

Source: [evergreen\_reference\_2009\.txt](<../data/corpus/evergreen_reference_2009.txt>); document ID: DOC-e6aa9f8c6308ab748459f87b578a0df9df9c865b7911bac3686e865963b7af6f; normalized lines 217–217.

> 4\. Provide multiple output formats and scheduling options

### REQ-225 — Batch Item Transfer Utility Across Branches

- Internal key: REQ-72ae8d0b837aabd6f61f69bd648de8eb13f588365a12e8b20675e5d8f3becc55
- Type: functional
- Priority: P2
- Priority basis: inferred
- Priority rationale: Batch transfers support recurring branch and outreach operations and have substantial operational impact; no explicit source priority is provided\.
- Originating candidates: CAND-f60304d962427437cad08cede1fa274f32e442a854a1f026eb4c445808124222

The system shall provide an item transfer utility that moves batches of items between branches, including transfers to mobile library units or outreach program collections\.

Sources and evidence:

Source: [interview\_cataloging\_2009-05-08\.txt](<../data/corpus/interview_cataloging_2009-05-08.txt>); document ID: DOC-a79fab45108210e6bce7d92153dfcf055f2ef6b2cdab49a3f6f5717a3e35f29f; normalized lines 42–45.

> THOMAS: Yes, the item transfer utility is crucial for us\. We often need to
> move batches of items between branches - for example, sending books to a mobile
> library unit or to an outreach program collection\. The utility needs several
> capabilities:

### REQ-226 — Administrative Report Templates

- Internal key: REQ-731e6eec00d9c797e092d41b469d337b790174437f9cdcc4641c345307ab2c5d
- Type: functional
- Priority: P2
- Priority basis: inferred
- Priority rationale: Template creation and modification is important reporting functionality for administrators; no explicit source priority is provided\.
- Originating candidates: CAND-e8143608858e361e828b71c80680fb73f6ad26848ed192453f560c94dd0e8345

The system shall allow administrators to create report templates and run them as-is or modify them before running\.

Sources and evidence:

Source: [survey\_results\_2009\.txt](<../data/corpus/survey_results_2009.txt>); document ID: DOC-aac7bceef7a883652805583e98ec513b6ae2e7951e2ecfa18722127b1f12a5c4; normalized lines 133–134.

> 9\. Report templates can be created by administrators and run as-is or modified\.
> 

### REQ-227 — Fine-Grained Permissions for Creating and Cloning Reports

- Internal key: REQ-7320b94faf743c76e2039394f63fddfa2571379becc82d7a437f0ac71a6471c6
- Type: functional
- Priority: P2
- Priority basis: inferred
- Priority rationale: Report permissions control access to report creation and cloning and are important to secure administration, but the source does not identify them as critical or compliance-mandated\.
- Originating candidates: CAND-a8263f024ea52f917468a7739817e59e5f17e73a892c7990c14ddf9e724adbd3

The system shall provide distinct, fine-grained permission levels that limit who can create and clone reports, and shall make those permissions easy to administer\.

Sources and evidence:

Source: [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>); document ID: DOC-091180de9b2d4ea83267d989411ac89f415d4def3bbf7cd51651fb7fda8d8bf9; normalized lines 242–244.

> 8\.3 Report Permissions
> The system should provide distinct, fine-grained permission levels that limit
> who can create and clone reports\. All permissions should be easy to administer\.

### REQ-228 — Compute Patron Age at Query Time from Birth Date

- Internal key: REQ-739373cca6671fc6a6a4dc36883788f53f65cc1432941b852f3ebc76231bb05d
- Type: functional
- Priority: P2
- Priority basis: inferred
- Priority rationale: This enables requested demographic analysis using the specified source field and query-time calculation\.
- Originating candidates: CAND-3dedd3ef9065b0f3c2f4bbf294c62626bdc19a926a29a3c07d8a397446451e74

The system shall calculate patron age at query time from the birth\_date field and shall support creating age brackets for queries\.

Sources and evidence:

Source: [conversations/conv\_pines023\_patron\_characteristics\.eml](<../data/corpus/conversations/conv_pines023_patron_characteristics.eml>); document ID: DOC-d2b26a6e7678ca4e82bfa7bb06566f329dea692ea22e8987b516fa8bc98c544b; normalized lines 89–91.

> The "age range" is calculated from the birth\_date field, which means we
> need to compute it at query time\. We can create age brackets in the query\.
> 

### REQ-229 — Reports to Identify Purge Candidates Without Deletion

- Internal key: REQ-73bf767d54af7baceafac0b609b0ed37fe205bd7d086b35f70af7fd246150264
- Type: nonfunctional
- Priority: P1
- Priority basis: inferred
- Priority rationale: Inferred as critical because read-only candidate reporting is identified as a safety measure before deletions\.
- Originating candidates: CAND-773f1da3bb2b506e15ae827523e1e3ae5df320e297fa60cf7786ebb5aa9e26ef

The system shall provide reports that identify candidates for purging without directly performing deletions\.

Sources and evidence:

Source: [conversations/conv\_pines021\_item\_purging\.eml](<../data/corpus/conversations/conv_pines021_item_purging.eml>); document ID: DOC-74ccbb6ac77183c0d1b34b1e79ed8fcbbfb4e7525cb33798c3af832fed733ad8; normalized lines 69–71.

> I'm thinking:
> 1\. Reports show candidates for purging \(read-only\)
> 2\. A separate confirmation step for actual deletions

Source: [conversations/conv\_pines021\_item\_purging\.eml](<../data/corpus/conversations/conv_pines021_item_purging.eml>); document ID: DOC-74ccbb6ac77183c0d1b34b1e79ed8fcbbfb4e7525cb33798c3af832fed733ad8; normalized lines 136–139.

> Safety measures:
> - Read-only reports for identifying candidates
> - Separate confirmation step for actual deletions
> - Audit trail for all purges

### REQ-230 — Items Received for Holds Report

- Internal key: REQ-73d2b19304fc933ff7c98c219e28c25aa0810bda1c3df3f24321e0c783982316
- Type: functional
- Priority: P3
- Priority basis: inferred
- Priority rationale: This is a useful operational report and is not identified as essential to core operation\.
- Originating candidates: CAND-a1f1b024fd672328a748a87a845eff93e3c3c4b496b0a3a31273fcf3087a391b

The system shall provide an Items Received for Holds report\.

Sources and evidence:

Source: [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>); document ID: DOC-091180de9b2d4ea83267d989411ac89f415d4def3bbf7cd51651fb7fda8d8bf9; normalized lines 564–564.

> - Items Received for Holds

### REQ-231 — Report Templates with Controlled Modification by Administrators

- Internal key: REQ-73eff4f7560788fe0eb7b2d6b0d16af9462694379777ef825955425c67909099
- Type: functional
- Priority: P2
- Priority basis: inferred
- Priority rationale: Reusable and controlled templates support important staff reporting workflows, but no explicit priority is supplied\.
- Originating candidates: CAND-49254efda41b2f8287bd83538ba6e849a3d7b19deb0fa64728a439ceb1d3d723

The system shall allow administrators to create report templates available to staff; staff shall be able to run templates as-is or modify them, and administrators shall be able to limit which filters and display fields may be altered\.

Sources and evidence:

Source: [email\_report\_features\.eml](<../data/corpus/email_report_features.eml>); document ID: DOC-d9e168e0c03903021bf9e636e1d8e5f56dfcb79cc110d3839e38175a7c54344e; normalized lines 11–14.

> 2\. REPORT TEMPLATES: Admins need to create report templates that are available
>    to staff\. Templates should be runnable as-is or modified\. Changes shouldn't
>    compromise results\. Admins should be able to limit which filters and display
>    fields can be altered\.

Source: [email\_report\_features\.eml](<../data/corpus/email_report_features.eml>); document ID: DOC-d9e168e0c03903021bf9e636e1d8e5f56dfcb79cc110d3839e38175a7c54344e; normalized lines 16–18.

>    Example: Front-line staff can set a call number range for a weeding report
>    or add/remove display fields from a pick list, but can't alter the template
>    to display deleted items\.

### REQ-232 — Financial Reports with Balances, Fines, and Payments Breakdowns

- Internal key: REQ-741a4838019c01825fab688164a6cc554e84f4c18e4cba3253934eef40d6a5b5
- Type: functional
- Priority: P2
- Priority basis: inferred
- Priority rationale: Financial reporting has substantial operational and management impact, but the source does not establish it as critical or mandatory compliance\.
- Originating candidates: CAND-c0f0e7b1393c1e80fb5c05e38d8471d30dbdf2556cbbcc7a4b274f0b9a15e608

The system shall provide financial reports including patron account balances by patron, home branch, and system; fines and charges accrued by time period and type of charge; fines waived by time period and branch; and payments made by time period and payment method, including methods such as staff desk, self-check station, and OPAC\.

Sources and evidence:

Source: [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>); document ID: DOC-091180de9b2d4ea83267d989411ac89f415d4def3bbf7cd51651fb7fda8d8bf9; normalized lines 473–481.

> 13\.4 Financial Reports
> The system provides financial reports including:
>   - patron account balances by patron, home library, and system
>   - fines and charges accrued per time period \(e\.g\., last twelve months, YTD,
>     last month\) and per type of charge \(overdue fines, damaged item charges,
>     lost item charges, etc\.\)
>   - fines waived per time period and per branch
>   - payments made per time period and per payment method \(e\.g\., staff desk,
>     self-check station, OPAC\)

### REQ-233 — Editable Canned Report Display Options

- Internal key: REQ-743a70079470d57806063469d0a5fa5a023ea9261b34f5d28e19290a7c884b55
- Type: functional
- Priority: P3
- Priority basis: inferred
- Priority rationale: This improves flexibility of predefined reports but is not essential to basic reporting\.
- Originating candidates: CAND-9cc145c97ab22903f3a2f4b2f57a95679b764ffd05f5c53e07d490cdd7432559

The system shall allow staff to edit the display options of canned reports\.

Sources and evidence:

Source: [evergreen\_reference\_2009\.txt](<../data/corpus/evergreen_reference_2009.txt>); document ID: DOC-e6aa9f8c6308ab748459f87b578a0df9df9c865b7911bac3686e865963b7af6f; normalized lines 177–177.

> - No ability to edit canned report display options

### REQ-234 — Batch Item Status Conversion Utility and Report

- Internal key: REQ-750ef8573b46428e52db5fb6cbe7d0fc213003cd99795fbedfafdc66c239d7a3
- Type: functional
- Priority: P2
- Priority basis: inferred
- Priority rationale: Batch status conversion supports a stated operational workflow and affects many records at once\.
- Originating candidates: CAND-40f9a764146577eb5765bc1f9379141e3d624206d5c92a06583c00efdf6254c5

The system shall provide a report and utility to convert items from one status to another in batch, such as changing many items from missing to discard or weed\.

Sources and evidence:

Source: [conversations/conv\_pines021\_item\_purging\.eml](<../data/corpus/conversations/conv_pines021_item_purging.eml>); document ID: DOC-74ccbb6ac77183c0d1b34b1e79ed8fcbbfb4e7525cb33798c3af832fed733ad8; normalized lines 10–11.

> 2\. I need a report to help convert items from one status to another in batch\.
>    Like changing 100 items from "missing" to "discard/weed" at once\.

Source: [conversations/conv\_pines021\_item\_purging\.eml](<../data/corpus/conversations/conv_pines021_item_purging.eml>); document ID: DOC-74ccbb6ac77183c0d1b34b1e79ed8fcbbfb4e7525cb33798c3af832fed733ad8; normalized lines 128–130.

> The system should:
> - Provide a report to assist in the conversion of items from one status to
>   another

### REQ-235 — Streamlined Login Audit and Authentication with Staff Identification

- Internal key: REQ-75384725abe9bc284f0fa8b864d7ed17139f30169f70b2abb0c7ea380b9a8941
- Type: functional
- Priority: P2
- Priority basis: inferred
- Priority rationale: Individual authentication and auditability are important control requirements, but the source does not assign a formal priority level\.
- Originating candidates: CAND-085d50782057940ca78d26cc2c6c0e69687947fc2415e3e859bd7654d34df246

When a streamlined login method such as a card swipe is used, the system shall identify and track the individual staff member who is logged in, and the streamlined method shall not bypass individual authentication entirely\.

Sources and evidence:

Source: [email\_staff\_login\.eml](<../data/corpus/email_staff_login.eml>); document ID: DOC-64b10e94c42508c5aea1af877ec9d2fe34485b099b29994b8b1a76cadc55e8b3; normalized lines 38–41.

> to consider: even with card swipe, we need individual authentication\. The
> system must track WHICH staff member is logged in for audit purposes\. The card
> is just a convenient way to identify the person, but it shouldn't bypass
> individual authentication entirely\.

### REQ-236 — Role-Based Access Control for Staff Groups

- Internal key: REQ-75f761336ce9f46285d9f31c43db12cd04397af3260d6f2d9ff7eb10412eea41
- Type: functional
- Priority: P1
- Priority basis: explicitly specified
- Priority rationale: The source explicitly confirms flexible role-based access control as essential\.
- Originating candidates: CAND-909bbd607262588d8cc515f8b82288b63b6572aa737fe3472ab0859556f7b9b7, CAND-92351b7749fec0a153571a8cdc3144d5c24cf8e5cdca67ab31b836f2fbf314dc

The system shall control user rights and privileges through security groups and/or roles that support access control for individuals, workgroups, and arbitrary staff groups, and shall allow a user's permissions to be changed by changing the user's role assignment\.

Sources and evidence:

Source: [meeting\_minutes/meeting\_2009-07-20\_minutes\.txt](<../data/corpus/meeting_minutes/meeting_2009-07-20_minutes.txt>); document ID: DOC-5ab1dd8bc97af3b1ab2e378495f0e0d75fd501fcc19f923c0d8fda831074281b; normalized lines 120–124.

> CO-4: User rights and privileges will be controlled through security groups
>       and/or "roles" that allow access control for individuals, workgroups,
>       and arbitrary staff groups\.
>       \[Discussion: George confirmed this is essential\. We need flexible
>       role-based access control\.\]

Source: [meeting\_tech\_subcommittee\_2009-06-30\.txt](<../data/corpus/meeting_tech_subcommittee_2009-06-30.txt>); document ID: DOC-e081aa7bd57bf5e59c75a8a86f592124757b74dff1ee0df4badc10c025092d96; normalized lines 60–66.

> 2\.4 USER RIGHTS AND ROLES
> The role-based access control system was detailed:
> 
> Robert: "We need security groups and/or 'roles' that allow access control for
> individuals, workgroups, and arbitrary staff groups\. The system should make it
> easy to change someone's permissions by simply changing their role assignment\."
> 

### REQ-237 — Monthly Noncataloged In-House Use Report

- Internal key: REQ-760403193d0d6284117bafb23d34c4cf9a09e3523e703967f7b020940637289d
- Type: functional
- Priority: P3
- Priority basis: inferred
- Priority rationale: Useful circulation reporting, but not essential to basic operation\.
- Originating candidates: CAND-d21c470e20ce9f1b73208ae42bc86a04aa6023ce390ee7ce40c1cb4a6d299b2e

The system shall provide a monthly report of in-house use counts for noncataloged material\.

Sources and evidence:

Source: [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>); document ID: DOC-091180de9b2d4ea83267d989411ac89f415d4def3bbf7cd51651fb7fda8d8bf9; normalized lines 574–574.

> - NonCat In House Use Count by Month

### REQ-238 — Shelf Space Comparison Report

- Internal key: REQ-764024ba7436bda4e187c159793ac0cf657eda897ab873c97ea1ef4d58bfd219
- Type: functional
- Priority: P2
- Priority basis: inferred
- Priority rationale: Comparing circulation, collection, and shelf-space percentages supports important collection analysis\.
- Originating candidates: CAND-202972b16179a87374aa98fe9b4ef5390df65be8f54196a9a71c2e8543426407

The system shall provide, for each genre and format, the ability to compare the percentage of total circulations, the percentage of the collection, and the percentage of total shelf space\.

Sources and evidence:

Source: [conversations/conv\_pines016\_shelf\_space\.eml](<../data/corpus/conversations/conv_pines016_shelf_space.eml>); document ID: DOC-b507e8abe1ba7c996c1d86d688e90bcf2404694ec00528c8361f26dfc8bd82f1; normalized lines 98–106.

> Great discussion everyone\. Summarizing the Shelf Space Report requirement:
> 
> The system should provide, for each genre and format of material, the ability
> to compare:
> - The percentage of total circulations
> - The percentage of the collection
> - The percentage of total shelf space
> 
> The report should be available per library and per system\.

### REQ-239 — Global System Administrator Role

- Internal key: REQ-76944e40208876dcc27b57b460d000c3922dd90f49ae198e9e7725fecd2b9368
- Type: functional
- Priority: P2
- Priority basis: inferred
- Priority rationale: Consortium-wide administration and reporting are important system capabilities, but the sources do not assign a P-level priority\.
- Originating candidates: CAND-24a24c4117e586597171b350401c9b7be9ae6780852f85be2851daa83a377b5c, CAND-2bac5a70d2574e5b4fc5e0b9a1edf031e25874c56c5a8981ed3e9007f4c62e9c

The system shall provide a Global System Administrator role with full system access that can implement software changes and configurations and generate statistical reports for PINES as a whole\.

Sources and evidence:

Source: [meeting\_minutes/meeting\_2009-03-15\_minutes\.txt](<../data/corpus/meeting_minutes/meeting_2009-03-15_minutes.txt>); document ID: DOC-defef992db2ae0e10167fd94902eac93f82c59c4c070df030ca2f77811082818; normalized lines 105–109.

>   Global System Administrator: Manages PINES at the consortium level,
>                                implementing software changes and configurations,
>                                and generating statistical reports for PINES as
>                                a whole\.
>                                \[Katherine: This is the PINES central IT team\]

Source: [meeting\_tech\_subcommittee\_2009-06-30\.txt](<../data/corpus/meeting_tech_subcommittee_2009-06-30.txt>); document ID: DOC-e081aa7bd57bf5e59c75a8a86f592124757b74dff1ee0df4badc10c025092d96; normalized lines 67–69.

> Key points:
> - Global Admin: Full system access
> - Local Admin: Branch-level reporting and configuration

### REQ-240 — Accessible Report Interface and Compliance

- Internal key: REQ-77cdbbcd3678512ff8c2d374f74207fc584d021748c3379ecb41db69c9ca42b4
- Type: nonfunctional
- Priority: P1
- Priority basis: inferred
- Priority rationale: Accessibility of the report interface is essential for equitable access to core reporting functions\.
- Originating candidates: CAND-a3ff94c9dd49a977120652f5f0c189848736bb1712930ebddda528a7a9d60945

The report interface shall provide accessibility support and implement accessibility compliance\.

Sources and evidence:

Source: [evergreen\_reference\_2009\.txt](<../data/corpus/evergreen_reference_2009.txt>); document ID: DOC-e6aa9f8c6308ab748459f87b578a0df9df9c865b7911bac3686e865963b7af6f; normalized lines 188–188.

> - No accessibility support for report interface

### REQ-241 — Survey Name Filtering

- Internal key: REQ-781c58730544f482396b4b16059b63f9ae6bd2d0aaff7c0f49ed753eaec8268b
- Type: functional
- Priority: P3
- Priority basis: inferred
- Priority rationale: This is a useful reporting convenience and usability improvement, not a core operational necessity; no explicit source priority is provided\.
- Originating candidates: CAND-f2f2e1111f9493da96f82e3d591b5b6584aff73e8e23d1055883e8e390391fca

The system shall allow users to filter surveys by survey name rather than only by survey ID by resolving survey names to IDs internally\.

Sources and evidence:

Source: [meeting\_tech\_subcommittee\_2009-06-30\.txt](<../data/corpus/meeting_tech_subcommittee_2009-06-30.txt>); document ID: DOC-e081aa7bd57bf5e59c75a8a86f592124757b74dff1ee0df4badc10c025092d96; normalized lines 182–185.

> 5\.5 SURVEY FILTERING
> The ability to filter by survey name rather than survey ID requires the system
> to resolve names to IDs internally\.
> 

### REQ-242 — Circulation Count by Location and Patron Home Library

- Internal key: REQ-7873382b18e91570bd8197281a6f001e9df3c93b3140c02c99059080d039bf9b
- Type: functional
- Priority: P2
- Priority basis: inferred
- Priority rationale: The report provides specified circulation analysis across locations and patron home libraries, but no explicit priority is supplied\.
- Originating candidates: CAND-b7305b8c16e82236b048dfc26e8b6a08e3e7875fe6b36a3bc3013a4e489bd2b8

The system shall provide a circulation count report by circulation location broken down by patron home library\.

Sources and evidence:

Source: [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>); document ID: DOC-091180de9b2d4ea83267d989411ac89f415d4def3bbf7cd51651fb7fda8d8bf9; normalized lines 508–508.

> - Circulation Count by Circ Location broken down by Patron Home Library

### REQ-243 — Patron Notes Wording Report

- Internal key: REQ-7a0c8973cb8ed518f9abf82bb7bbff333e848201b464a8d1576ab72a81411d5a
- Type: functional
- Priority: P3
- Priority basis: inferred
- Priority rationale: This is a useful targeted patron-reporting capability but is not shown to be essential to basic operation\.
- Originating candidates: CAND-4d491824820ae6a1f29329bbfe0925a24ac55d907b7bba81ca9e0dc18831e9b1

The system shall provide a list of patrons whose notes contain specified wording\.

Sources and evidence:

Source: [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>); document ID: DOC-091180de9b2d4ea83267d989411ac89f415d4def3bbf7cd51651fb7fda8d8bf9; normalized lines 559–559.

> - List of Patrons with specific wording in notes

### REQ-244 — Last Edit Date Reporting Excluding Circulation Events

- Internal key: REQ-7af1cc46a49ccf5f4c4b2bd851449c1696f3fee3522d06d42a3ff9338a0f7b0c
- Type: functional
- Priority: P2
- Priority basis: inferred
- Priority rationale: Separating editing activity from circulation activity supports accurate reporting and analysis\.
- Originating candidates: CAND-178571d7af05d72fa2f60629463807ef029ded441ef482cb71b5986fa7d6d660

The system shall provide last edit date reporting that excludes last circulation events\.

Sources and evidence:

Source: [evergreen\_reference\_2009\.txt](<../data/corpus/evergreen_reference_2009.txt>); document ID: DOC-e6aa9f8c6308ab748459f87b578a0df9df9c865b7911bac3686e865963b7af6f; normalized lines 200–201.

> - Last edit date not including last circulation - does not exist
> - Ability to indicate last circulation date - not available as separate field

### REQ-245 — Administrative Error Feedback with Query-Specific Front-End Details

- Internal key: REQ-7b6c7fa4f29a5a82f0b392224a571cacdf11a6c369e557bbcb9abaa45e292c24
- Type: nonfunctional
- Priority: P2
- Priority basis: inferred
- Priority rationale: Actionable error feedback is important for administration and diagnosis of reporting problems\.
- Originating candidates: CAND-d8ce075db4025d4b21ff176b9a8f7441c43582d38b3e3e2ee5ff05173bb3ca8b

The system shall provide high-level error reporting and feedback and shall provide low-level query-specific feedback through the front-end interface to Local and Global System Administrators\.

Sources and evidence:

Source: [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>); document ID: DOC-091180de9b2d4ea83267d989411ac89f415d4def3bbf7cd51651fb7fda8d8bf9; normalized lines 192–194.

> UD-4: The system must provide thorough high-level error reporting and feedback,
>       and shall allow low-level query-specific feedback for Local and Global
>       System Administrators from the front-end interface\.

### REQ-246 — Route New Report Development Through Reports Testing Group

- Internal key: REQ-7bfaf83f69efe7ebbcf159a165debedbb8b9fc85ca3c45349ea3362e73aa008e
- Type: nonfunctional
- Priority: P2
- Priority basis: inferred
- Priority rationale: The requirement establishes a quality-control process for new reports development, but the source does not assign an explicit priority\.
- Originating candidates: CAND-af05cdfd98fe37bdde26517512297869a3cb74dedf25280eb893150842c08c70

All new reports development shall be filtered through the Reports testing group\.

Sources and evidence:

Source: [meeting\_minutes/meeting\_2009-03-15\_minutes\.txt](<../data/corpus/meeting_minutes/meeting_2009-03-15_minutes.txt>); document ID: DOC-defef992db2ae0e10167fd94902eac93f82c59c4c070df030ca2f77811082818; normalized lines 40–44.

>   "Reports Working Group Mission:
>    - Document optimal Reports functionality within a future Evergreen release
>      and develop a list of requirements\.
>    - Become the Reports testing group, through which all new Reports development
>      would be filtered\.

### REQ-247 — Query Design for Multiple Record Types

- Internal key: REQ-7c16046ba6cf4f3099300c95c29b171590021cf3f9a0981e5e289f4bf02b6713
- Type: functional
- Priority: P2
- Priority basis: inferred
- Priority rationale: Cross-record query design is important reporting functionality, but no explicit priority is supplied\.
- Originating candidates: CAND-62dd49230766d1ec3c627dc1a8d44d25179910b28708a2a4005c61edb66ec248

The system shall provide a user-friendly interface for designing queries against bibliographic, item, patron, transaction, and financial record types\.

Sources and evidence:

Source: [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>); document ID: DOC-091180de9b2d4ea83267d989411ac89f415d4def3bbf7cd51651fb7fda8d8bf9; normalized lines 249–251.

> 8\.4 Query Tool
> The system should provide a user-friendly interface for designing queries
> against all record types \(bibliographic, item, patron, transaction, financial\)\.

### REQ-248 — Recurring Report Scheduling

- Internal key: REQ-7cbe18a43bc004e93ecf8282a23407c7a5358217e0432522a3741056777c0437
- Type: functional
- Priority: P2
- Priority basis: inferred
- Priority rationale: Recurring reports support regular operational reporting and were identified as a needed capability\.
- Originating candidates: CAND-1bc7def882a047e862f987f1504b9dd7c9b7bf604ae540469ef1466fd697b540

The system shall allow users to schedule recurring reports\.

Sources and evidence:

Source: [survey\_results\_2009\.txt](<../data/corpus/survey_results_2009.txt>); document ID: DOC-aac7bceef7a883652805583e98ec513b6ae2e7951e2ecfa18722127b1f12a5c4; normalized lines 66–66.

>   - Ability to schedule recurring reports: 52%

### REQ-249 — WorldCat last-copy editing support

- Internal key: REQ-7dab36d987513bce4cb4615bba05f66aace93596a21b6af917732c1341df4ad2
- Type: functional
- Priority: P1
- Priority basis: explicitly specified
- Priority rationale: The source explicitly describes WorldCat integration as critical\.
- Originating candidates: CAND-8a9fcb99b42bc663f32a410c3e22694d275a797a4b95a0992bce133cf02c4037

The system shall provide or integrate WorldCat-related functionality to assist catalogers in editing WorldCat entries when the library system has a last copy\.

Sources and evidence:

Source: [interview\_cataloging\_2009-05-08\.txt](<../data/corpus/interview_cataloging_2009-05-08.txt>); document ID: DOC-a79fab45108210e6bce7d92153dfcf055f2ef6b2cdab49a3f6f5717a3e35f29f; normalized lines 80–83.

> And the last copy report is CRITICAL\. This singles out a library system's last
> copies, to assist catalogers who need to edit WorldCat entries\. Last month, we
> almost deleted our last copy of a rare book before someone remembered to check
> WorldCat\. If we had a report like this, it would save us from that situation\.

Source: [interview\_cataloging\_2009-05-08\.txt](<../data/corpus/interview_cataloging_2009-05-08.txt>); document ID: DOC-a79fab45108210e6bce7d92153dfcf055f2ef6b2cdab49a3f6f5717a3e35f29f; normalized lines 125–125.

> - The last copy report and WorldCat integration are critical

### REQ-250 — Cancel Scheduled or Running Reports

- Internal key: REQ-7e074f3c3d835ca452ae3c48e422ec1fb3e3eaf364a70205c06313f97cbcd39a
- Type: functional
- Priority: P3
- Priority basis: inferred
- Priority rationale: This provides useful operational control but is not required for basic report generation\.
- Originating candidates: CAND-9ad3b8929a72aa2ef6c42c3c53ab60d52ff8ee72746b73253f3dd57b2f913a62

The system shall allow staff to cancel a scheduled or running report\.

Sources and evidence:

Source: [survey\_results\_2009\.txt](<../data/corpus/survey_results_2009.txt>); document ID: DOC-aac7bceef7a883652805583e98ec513b6ae2e7951e2ecfa18722127b1f12a5c4; normalized lines 99–99.

>   - "Ability to cancel a scheduled or running report"

### REQ-251 — Patron Demographics and Interests Analysis

- Internal key: REQ-7ecfec537f372907a56dd312a0a6962119a8217ac76bf50cd1a766fb9d1f2c3a
- Type: functional
- Priority: P2
- Priority basis: inferred
- Priority rationale: The capability supports management analysis, but the source does not assign a P-level priority\.
- Originating candidates: CAND-36a38745a975aa7cc77dabcfe50d08aa0f564c9e5432afd16d2250a0764ed45b

The Management Processes shall provide tools to analyze patron demographics and interests\.

Sources and evidence:

Source: [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>); document ID: DOC-091180de9b2d4ea83267d989411ac89f415d4def3bbf7cd51651fb7fda8d8bf9; normalized lines 88–88.

>   - Analyzing the demographics and interests of patrons\.

### REQ-252 — Weeding Reports

- Internal key: REQ-7efb5012d383718b9284f50d1a00abbc19577086935bfb4354e5df78c359bb13
- Type: functional
- Priority: P2
- Priority basis: inferred
- Priority rationale: The source states that weeding reports are frequently used, indicating important operational value without assigning an explicit priority\.
- Originating candidates: CAND-27817c8c3b15ff4dd8628fce4194ec4b5354ca1cd8c9e7e36557d742af715430

The system shall provide weeding reports\.

Sources and evidence:

Source: [meeting\_minutes/meeting\_2009-07-20\_minutes\.txt](<../data/corpus/meeting_minutes/meeting_2009-07-20_minutes.txt>); document ID: DOC-5ab1dd8bc97af3b1ab2e378495f0e0d75fd501fcc19f923c0d8fda831074281b; normalized lines 51–51.

>   - Weeding reports are frequently used

### REQ-253 — Administrator-Managed Security Groups and Roles

- Internal key: REQ-7f0e00541153d76c0eb37e842dda667430954bb3ae468044ec341c41933c7b43
- Type: functional
- Priority: P2
- Priority basis: inferred
- Priority rationale: Inferred as important access-control administration functionality; no explicit source priority is supplied\.
- Originating candidates: CAND-75be9cb43f93d8b89c6ee0ef6d30a3ecf96678b8052c8f466c4e8e214275d47e

Administrators shall be able to create and manage security groups or roles\.

Sources and evidence:

Source: [email\_staff\_login\.eml](<../data/corpus/email_staff_login.eml>); document ID: DOC-64b10e94c42508c5aea1af877ec9d2fe34485b099b29994b8b1a76cadc55e8b3; normalized lines 50–51.

> permissions should be determined by their assigned security group/role\.
> Administrators should be able to create and manage these groups\.

### REQ-254 — Item location reversion after set period

- Internal key: REQ-7f1a8945403765968d103e08e01a58d54f2b22d479076453a054b57043001735
- Type: functional
- Priority: P2
- Priority basis: inferred
- Priority rationale: Location restoration affects operational accuracy for mobile and distributed services; the source does not establish a more specific priority\.
- Originating candidates: CAND-8d346afecd1e6fca9e58195a62e10416ccbfa3d340df66ad694714e318975370

The system shall provide mechanisms to revert items to their original location after a set period of time, such as when a mobile library returns to base\.

Sources and evidence:

Source: [interview\_cataloging\_2009-05-08\.txt](<../data/corpus/interview_cataloging_2009-05-08.txt>); document ID: DOC-a79fab45108210e6bce7d92153dfcf055f2ef6b2cdab49a3f6f5717a3e35f29f; normalized lines 53–55.

> location\. And there should be mechanisms for reverting items back to their
> original location after a set period of time - like when a mobile library
> returns to base\.

### REQ-255 — Include Null and Blank Fields in Report Results

- Internal key: REQ-7fe20f2f414d0b6bb2a5fbb727f85c0e025ab09a5e7a3ab230564b2c404d8920
- Type: functional
- Priority: P2
- Priority basis: inferred
- Priority rationale: Preserving null and blank values is important for complete and accurate reporting\.
- Originating candidates: CAND-1a3811c0a213ac2be35bea074bea127e75d003925d98fe25bb57878953be4911, CAND-1a96ef3f6e53faff772618b35a3b663759518c0ae10b0de428882cc6783b2208

The system shall include all null and blank fields in report result sets\.

Sources and evidence:

Source: [meeting\_tech\_subcommittee\_2009-06-30\.txt](<../data/corpus/meeting_tech_subcommittee_2009-06-30.txt>); document ID: DOC-e081aa7bd57bf5e59c75a8a86f592124757b74dff1ee0df4badc10c025092d96; normalized lines 177–181.

> 5\.4 NULL HANDLING
> "All nulls and blank fields must be included in the results," Robert noted\.
> "This is actually the default behavior in SQL, but we need to make sure it's
> explicitly required\."
> 

Source: [survey\_results\_2009\.txt](<../data/corpus/survey_results_2009.txt>); document ID: DOC-aac7bceef7a883652805583e98ec513b6ae2e7951e2ecfa18722127b1f12a5c4; normalized lines 100–100.

>   - "All nulls and blank fields must be included in results"

### REQ-256 — Require Confirmation Before Purging Deletions

- Internal key: REQ-8039ff9491ba06c264a939614123435e1c5c9753c536dac27a6919356224d7a5
- Type: nonfunctional
- Priority: P1
- Priority basis: inferred
- Priority rationale: The source identifies separate confirmation as a deletion safety measure; P1 is inferred because it protects records from unintended destructive action\.
- Originating candidates: CAND-3b905d1f2f12567b87b0769be444523daf3037cf4c0fa345e22c334644ae9eb3

The system shall require a separate confirmation step before actual deletions purge records\.

Sources and evidence:

Source: [conversations/conv\_pines021\_item\_purging\.eml](<../data/corpus/conversations/conv_pines021_item_purging.eml>); document ID: DOC-74ccbb6ac77183c0d1b34b1e79ed8fcbbfb4e7525cb33798c3af832fed733ad8; normalized lines 71–72.

> 2\. A separate confirmation step for actual deletions
> 3\. Audit trail for all purges

Source: [conversations/conv\_pines021\_item\_purging\.eml](<../data/corpus/conversations/conv_pines021_item_purging.eml>); document ID: DOC-74ccbb6ac77183c0d1b34b1e79ed8fcbbfb4e7525cb33798c3af832fed733ad8; normalized lines 136–139.

> Safety measures:
> - Read-only reports for identifying candidates
> - Separate confirmation step for actual deletions
> - Audit trail for all purges

### REQ-257 — Vendor Data Interfaces via APIs and File Transfers

- Internal key: REQ-815ab976eb1fb48c310acaae0250bd25aa1f280735d89a870ee1860c5446b0eb
- Type: functional
- Priority: P2
- Priority basis: inferred
- Priority rationale: External-vendor integration is important to the stated Management Processes scope; no explicit source priority is provided\.
- Originating candidates: CAND-efd8161d2574a6d047d206d43becedf3cf02c9dcbd7391c80358f2d47521d20f

Management Processes shall interface with vendor websites through published APIs and/or automated transfer of standard-format data files, including formats such as USMARC21 and EDIFACT\.

Sources and evidence:

Source: [meeting\_minutes/meeting\_2009-07-20\_minutes\.txt](<../data/corpus/meeting_minutes/meeting_2009-07-20_minutes.txt>); document ID: DOC-5ab1dd8bc97af3b1ab2e378495f0e0d75fd501fcc19f923c0d8fda831074281b; normalized lines 183–186.

> DE-2: Management Processes interface with a variety of vendor websites, via
>       published APIs and/or automated transfer of standard-format data files
>       \(e\.g\., USMARC21, EDIFACT\)\.
>       \[Discussion: Some libraries use external vendors for certain functions\.

### REQ-258 — Document Report Architectural Constraints via Technical Subcommittee

- Internal key: REQ-81f81b8cbd8488bb7bdc3fabe462101ffb91eebdbd111d794ade10c632b1d34c
- Type: nonfunctional
- Priority: P2
- Priority basis: inferred
- Priority rationale: The source explicitly schedules technical-subcommittee review of architectural constraints, making this a project documentation obligation\.
- Originating candidates: CAND-4348024e4fc3569842e0421dd59682230968237168a06dc27d93983925ea3fd9

The project shall identify and document architectural constraints relevant to reports through the designated technical-subcommittee process\.

Sources and evidence:

Source: [meeting\_minutes/meeting\_2009-03-15\_minutes\.txt](<../data/corpus/meeting_minutes/meeting_2009-03-15_minutes.txt>); document ID: DOC-defef992db2ae0e10167fd94902eac93f82c59c4c070df030ca2f77811082818; normalized lines 129–134.

>   - Each member will conduct at least one interview with staff at their library
>     system to gather report needs \(due by April 15, 2009\)
>   - Katherine will circulate the King County / Galecia Group draft for reference
>   - A follow-up meeting is scheduled for July 20, 2009 to review findings
>   - A technical subcommittee meeting will be held in late June to discuss
>     architectural constraints

### REQ-259 — Board and Activity Reports for Annual and Usage Statistics

- Internal key: REQ-8239e0a8a6025c47becf4d159f74ea17fd7f9338cd1e27ddee866970d1c85438
- Type: functional
- Priority: P2
- Priority basis: inferred
- Priority rationale: This supports required organizational reporting and management evaluation\.
- Originating candidates: CAND-a6688ed9bf7aeeb6a83cdda3157b6e8e4ba3c7aafca383edaa6c77cbdd7f22e5

The system shall provide predefined board reports containing basic statistics required for the Georgia Annual Report and activity reports showing traffic and volume of use, including checkouts, check-ins, holds placed, and holds filled\.

Sources and evidence:

Source: [email\_report\_features\.eml](<../data/corpus/email_report_features.eml>); document ID: DOC-d9e168e0c03903021bf9e636e1d8e5f56dfcb79cc110d3839e38175a7c54344e; normalized lines 25–29.

> 4\. BOARD REPORTS: Pre-defined reports for library boards with basic statistics
>    \(Georgia Annual Report requirements\)\. Activity reports showing traffic and
>    volume of use - checkouts, check-ins, holds placed, holds filled\. Cross-
>    tabulated per terminal, per branch, per system, per hour, per age range,
>    per patron type, per patron location\.

Source: [email\_report\_features\.eml](<../data/corpus/email_report_features.eml>); document ID: DOC-d9e168e0c03903021bf9e636e1d8e5f56dfcb79cc110d3839e38175a7c54344e; normalized lines 110–111.

> 4\. BOARD REPORTS: Pre-defined reports for boards\. Cross-tabulated per
>    terminal/branch/system/hour/age/patron type/location\.

### REQ-260 — Definable Staff Roles and Assignments

- Internal key: REQ-82a9433355bfd9211ad7c71140e59ac886e17446f6338635a08f20eb76f2f334
- Type: functional
- Priority: P2
- Priority basis: inferred
- Priority rationale: Role definition and assignment supports controlled administration and operational access; the source does not assign a priority\.
- Originating candidates: CAND-e04a626fb77338ba833377637031307dd80ff7d12f65c7cd20aaac5e8c4382d0

The system shall support defining roles for different staff types and assigning those roles to staff members\.

Sources and evidence:

Source: [email\_staff\_login\.eml](<../data/corpus/email_staff_login.eml>); document ID: DOC-64b10e94c42508c5aea1af877ec9d2fe34485b099b29994b8b1a76cadc55e8b3; normalized lines 64–71.

> At Piedmont, we have several different types of staff:
> - Front desk staff \(can run basic reports, limited filters\)
> - Department heads \(can create and modify templates\)
> - System administrators \(full access to all reports and permissions\)
> 
> Each of these should be a role that can be assigned to staff members\. The system
> should make it easy to administer these roles - changing someone's permissions
> should be a simple matter of changing their role assignment, not modifying

### REQ-261 — Transfer Auto-Revert

- Internal key: REQ-831ab059e0df7aa832e04fbdefd18e1394023cbd41c003b50e79910ba5628237
- Type: functional
- Priority: P2
- Priority basis: inferred
- Priority rationale: Automatic recovery of transferred items is operationally important, but no explicit priority is supplied\.
- Originating candidates: CAND-24efd64b595fc9935b6fd3c48aaaf8e87c43ef009d57cbf3503a27abe88b31f8

The system shall provide an auto-revert mechanism implemented as a scheduled task that checks transferred items and reverts them according to elapsed-time or status criteria\.

Sources and evidence:

Source: [conversations/conv\_pines018\_item\_transfer\.eml](<../data/corpus/conversations/conv_pines018_item_transfer.eml>); document ID: DOC-a47eb1f11286ff9099687b72a901e4a6ed2455b431087c0742aa78583c5bd80a; normalized lines 59–60.

> 5\. Auto-revert mechanism - a scheduled task that checks transferred items
>    and reverts them based on time or status criteria\.

### REQ-262 — Support Multiple Reporting Interfaces

- Internal key: REQ-83305b684e7e93c6ed6b812a002241c272ca271d92b69b56a2b6a444d498db08
- Type: functional
- Priority: P2
- Priority basis: inferred
- Priority rationale: Multiple reporting interfaces materially affect reporting capability; the source does not assign a priority\.
- Originating candidates: CAND-e6357108ed68dbac76984d51c4c380ca77361e00bb400a736fbd7b0a43b24b1c

The system shall support canned, on-demand, and open-template reporting interfaces\.

Sources and evidence:

Source: [evergreen\_reference\_2009\.txt](<../data/corpus/evergreen_reference_2009.txt>); document ID: DOC-e6aa9f8c6308ab748459f87b578a0df9df9c865b7911bac3686e865963b7af6f; normalized lines 195–196.

> - Three interfaces \(canned, on-demand, open template\) - only basic canned exists
> - Open Template Reporting - does not exist

### REQ-263 — Collection Use and Shelf Space Percentage Report by Genre and Format

- Internal key: REQ-8415aa47b68eeaa3d7c651ef75a378079208c853df5ac7d4005814a7fd898085
- Type: functional
- Priority: P2
- Priority basis: inferred
- Priority rationale: The report supports collection and shelf-space management, but the source does not assign an explicit priority\.
- Originating candidates: CAND-bb5b03e98522452b8d99e3b3e5f1e0ba2b10dc527aea5c9363ff1e5f95e94552

For each genre and format of material, the system shall provide a report showing the percentage of total circulations, the percentage of the collection, and the percentage of total shelf space\.

Sources and evidence:

Source: [conversations/conv\_pines016\_shelf\_space\.eml](<../data/corpus/conversations/conv_pines016_shelf_space.eml>); document ID: DOC-b507e8abe1ba7c996c1d86d688e90bcf2404694ec00528c8361f26dfc8bd82f1; normalized lines 1–6.

> Question for the group: How do I figure out if I'm using my shelf space
> efficiently? I need something that shows me, for each genre and format:
> - What percentage of total circulations it has
> - What percentage of the collection it is
> - What percentage of total shelf space it occupies
> 

### REQ-264 — Indirect Access to Reporting Through OPAC Displays

- Internal key: REQ-846c11ac1bf6e94d7a1e70ede1591ee52cb12cf92cb1b5a982e86218f507c7fa
- Type: functional
- Priority: P2
- Priority basis: inferred
- Priority rationale: Separating patron access from the reporting system supports controlled access, but no explicit priority is supplied\.
- Originating candidates: CAND-5206d91138d9a8251b5e9bd1d7bf79e6b2f0bc73a40d422d8a42e2fee106c544

Patrons shall access reporting results indirectly through OPAC displays and shall not have direct access to the reporting system\.

Sources and evidence:

Source: [meeting\_tech\_subcommittee\_2009-06-30\.txt](<../data/corpus/meeting_tech_subcommittee_2009-06-30.txt>); document ID: DOC-e081aa7bd57bf5e59c75a8a86f592124757b74dff1ee0df4badc10c025092d96; normalized lines 71–72.

> - Staff: Run reports within assigned permissions
> - Patron: Indirect access through OPAC displays

### REQ-265 — Standards-Compliant HTML for Web Output

- Internal key: REQ-868b0352fbd6dfa0f86d941f7b6b971bb3ec2630959efaf8d42a43bd87e0fe21
- Type: nonfunctional
- Priority: P2
- Priority basis: inferred
- Priority rationale: This applies broadly to web output and supports interoperability and consistent operation of web-based interfaces\.
- Originating candidates: CAND-99e6efc589c27a60d93e8f01243ed44004c4377af40e2dc911fa7279d620d5cd

Management Processes shall produce standards-compliant HTML for all web output\.

Sources and evidence:

Source: [meeting\_minutes/meeting\_2009-07-20\_minutes\.txt](<../data/corpus/meeting_minutes/meeting_2009-07-20_minutes.txt>); document ID: DOC-5ab1dd8bc97af3b1ab2e378495f0e0d75fd501fcc19f923c0d8fda831074281b; normalized lines 110–112.

> CO-2: Management Processes shall produce standards-compliant HTML\.
>       \[Discussion: All web output needs to be valid HTML\. This affects report
>       display, help system, and any web-based UI components\.\]

### REQ-266 — Combined AND/OR Query Filters

- Internal key: REQ-86982ec1ffb99ec98051b741fa992d7e213ffc9e75d21d19bdf3d0de91b35205
- Type: functional
- Priority: P2
- Priority basis: inferred
- Priority rationale: Combined filtering is important for flexible report and query selection\.
- Originating candidates: CAND-1769be726f97ae8abb3e561ead88bcf5c0ae22a30cd9b7b7b929a5c81669f536

The system shall allow users to combine multiple filters with AND and OR logic\.

Sources and evidence:

Source: [conversations/conv\_pines023\_patron\_characteristics\.eml](<../data/corpus/conversations/conv_pines023_patron_characteristics.eml>); document ID: DOC-d2b26a6e7678ca4e82bfa7bb06566f329dea692ea22e8987b516fa8bc98c544b; normalized lines 92–93.

> Combining filters is also doable - just add WHERE clauses\. We can support
> both AND and OR logic\.

Source: [conversations/conv\_pines023\_patron\_characteristics\.eml](<../data/corpus/conversations/conv_pines023_patron_characteristics.eml>); document ID: DOC-d2b26a6e7678ca4e82bfa7bb06566f329dea692ea22e8987b516fa8bc98c544b; normalized lines 120–120.

> - Filters can be combined with AND/OR logic

### REQ-267 — Report Recipient Email Address Entry

- Internal key: REQ-86a49ed1b58b112c2faa97c310e907661195ae388f2eb5eaea33dc4a62485df2
- Type: functional
- Priority: P3
- Priority basis: inferred
- Priority rationale: The source requests recipient address entry as a reporting convenience and does not establish a higher priority\.
- Originating candidates: CAND-bd7d935d839397e3c7f2400a4c9f87d8aae202b1ec90370e29a439fc4258eca1

The system shall allow users to enter email addresses to which reports are sent\.

Sources and evidence:

Source: [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>); document ID: DOC-091180de9b2d4ea83267d989411ac89f415d4def3bbf7cd51651fb7fda8d8bf9; normalized lines 626–626.

> - Ability to enter email addresses for report to be sent to - would be great to

### REQ-268 — Count and Track Record Deletions

- Internal key: REQ-876194ec737cc7f823e0518315eacdfb0314ec0a91eb5cc53a90b54a781d3e8e
- Type: functional
- Priority: P2
- Priority basis: inferred
- Priority rationale: Inferred as high priority because the evidence identifies counting and tracking deletions as an administrative capability\.
- Originating candidates: CAND-7d196bae1fe78f8b24ee1f8a999bbbf1b16574b81d8e0faa66ea79b7d1fbc992

The system shall count and track record deletions\.

Sources and evidence:

Source: [survey\_results\_2009\.txt](<../data/corpus/survey_results_2009.txt>); document ID: DOC-aac7bceef7a883652805583e98ec513b6ae2e7951e2ecfa18722127b1f12a5c4; normalized lines 91–91.

>   - Count and track record deletions: 27%

### REQ-269 — Fine-Grained Report Permissions and Shared Folder Control

- Internal key: REQ-88615aec00d43be9da5d586cb117eb6dab96e6733f67acb441b5ef63d3ed4bff
- Type: functional
- Priority: P1
- Priority basis: inferred
- Priority rationale: Fine-grained permissions protect access to reports and datasets and support system security, but no explicit priority is supplied\.
- Originating candidates: CAND-63815786889337e0b615ef60a7b3255f73a310aaf3b4d29436a809e00c670c8a

The system shall support distinct, fine-grained permission levels that limit who can create and clone reports, and administrators shall be able to create shared folders to allow or disallow staff from running specific reports and/or running ad hoc reports on specific sets of data\.

Sources and evidence:

Source: [email\_report\_features\.eml](<../data/corpus/email_report_features.eml>); document ID: DOC-d9e168e0c03903021bf9e636e1d8e5f56dfcb79cc110d3839e38175a7c54344e; normalized lines 20–23.

> 3\. PERMISSIONS: We need distinct, fine-grained permission levels limiting who
>    can create and clone reports\. Admins can create shared folders to allow or
>    disallow staff from running specific reports, and/or to run ad hoc reports
>    on specific sets of data\.

### REQ-270 — Filter Reports by Patron Characteristics

- Internal key: REQ-89b1e0cc81a36fd7830ac5be11d27779694335c4419e02415109db84c48530e2
- Type: functional
- Priority: P2
- Priority basis: inferred
- Priority rationale: Inferred as high priority because the evidence explicitly requires filtering by multiple patron characteristics\.
- Originating candidates: CAND-78b6df61fa356e5a45fbf1b8c45d260b4b6369ab64c77a0e46c79b2194b209fd

The system shall allow queries and reports to be filtered by patron characteristics including age range, zip code, county of residence, home branch, patron type, and preferred language\.

Sources and evidence:

Source: [conversations/conv\_pines023\_patron\_characteristics\.eml](<../data/corpus/conversations/conv_pines023_patron_characteristics.eml>); document ID: DOC-d2b26a6e7678ca4e82bfa7bb06566f329dea692ea22e8987b516fa8bc98c544b; normalized lines 109–116.

> The system should allow queries and reports to be limited or grouped by
> various patron characteristics, including:
> - Age range
> - Zip code
> - County of residence
> - Home branch
> - Patron type
> - Preferred language

### REQ-271 — Count Check-Ins Individually and Cumulatively by Terminal and User/Self-Service

- Internal key: REQ-89b31722a4d93b63b47802265aca41760b53ada131836b24055723a2c441b94d
- Type: functional
- Priority: P2
- Priority basis: inferred
- Priority rationale: The counts support circulation operations and analysis across the explicitly listed check-in types, but no explicit priority is supplied\.
- Originating candidates: CAND-b3e81d2e296785ea12efd286cf634e4caea369aaf231c49076077009f228b279

The system shall count all types of check-in individually and cumulatively, including book-drop, by terminal, and by user or self-service\.

Sources and evidence:

Source: [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>); document ID: DOC-091180de9b2d4ea83267d989411ac89f415d4def3bbf7cd51651fb7fda8d8bf9; normalized lines 425–429.

> 12\.3 Types of Check-In
> The system counts all types of check-in individually and cumulatively:
>   - book-drop
>   - by terminal
>   - by user or self-service

### REQ-272 — Read-Only Reporting Dependency on Enterprise ILS \(Acquisitions, Cataloging\)

- Internal key: REQ-8ac3195f7cf4e11a3d982c3fcfefa208d25c5108e9f473af03ee9e2feb702a45
- Type: nonfunctional
- Priority: P1
- Priority basis: inferred
- Priority rationale: This defines a foundational system boundary and dependency; P1 is inferred because violating it would change the system's core scope and integration model\.
- Originating candidates: CAND-44c830a5190f065767306d7caa36a95c35236b27f94c80260538f379e4b8f5e7

The Management Processes shall rely on enterprise ILS data structures and functionality, including the Acquisitions and Cataloging modules; the reporting system shall read ILS data and shall not manage acquisitions or cataloging\.

Sources and evidence:

Source: [meeting\_tech\_subcommittee\_2009-06-30\.txt](<../data/corpus/meeting_tech_subcommittee_2009-06-30.txt>); document ID: DOC-e081aa7bd57bf5e59c75a8a86f592124757b74dff1ee0df4badc10c025092d96; normalized lines 135–141.

> 4\.3 LIBRARY AUTOMATION DEPENDENCIES
> DE-1: Management Processes rely on the data structures and functionality of
> an enterprise-level Library Automation System, including Acquisitions and
> Cataloging modules\.
> 
> "All our data comes from the ILS," Robert said\. "The reporting system doesn't
> manage acquisitions or cataloging - it just reads the data\."

### REQ-273 — Shared Folders for Staff Reports

- Internal key: REQ-8b25402a1a0e0da35e86fe4b1d9a88283c13600adcc7dba6a5665cf264bb8ed8
- Type: functional
- Priority: P3
- Priority basis: inferred
- Priority rationale: Shared storage improves collaboration but is an optional enhancement to report access\.
- Originating candidates: CAND-3d456d58d8ae127d235f5e8e1f6ee8a0045b74343969bbb1b82172ebe759e9f5

The system shall provide shared folders for storing and sharing reports among staff\.

Sources and evidence:

Source: [evergreen\_reference\_2009\.txt](<../data/corpus/evergreen_reference_2009.txt>); document ID: DOC-e6aa9f8c6308ab748459f87b578a0df9df9c865b7911bac3686e865963b7af6f; normalized lines 84–85.

> - No fine-grained control over who can create vs\. run reports
> - No shared folders concept

### REQ-274 — Mass Deletion Safeguards

- Internal key: REQ-8b3162c6b2ee1cfa3434cc55bee249edf64ec3695993dba1227540dd34f1903a
- Type: nonfunctional
- Priority: P1
- Priority basis: inferred
- Priority rationale: The source identifies accidental deletion of an entire collection as a safety concern and proposes safeguards around purging\.
- Originating candidates: CAND-2c4fd558dbcd126d5fb2f8e3dbe922654aa8924d8eac9255457fdd774f956923

The system shall include safeguards to prevent accidental mass deletion of collections or entire library holdings\.

Sources and evidence:

Source: [conversations/conv\_pines021\_item\_purging\.eml](<../data/corpus/conversations/conv_pines021_item_purging.eml>); document ID: DOC-74ccbb6ac77183c0d1b34b1e79ed8fcbbfb4e7525cb33798c3af832fed733ad8; normalized lines 65–68.

> From a technical standpoint, we need to be careful here\. "Customizable
> criteria" is great, but we need to make sure the system is safe - we
> don't want someone accidentally deleting their entire collection\.
> 

Source: [conversations/conv\_pines021\_item\_purging\.eml](<../data/corpus/conversations/conv_pines021_item_purging.eml>); document ID: DOC-74ccbb6ac77183c0d1b34b1e79ed8fcbbfb4e7525cb33798c3af832fed733ad8; normalized lines 69–73.

> I'm thinking:
> 1\. Reports show candidates for purging \(read-only\)
> 2\. A separate confirmation step for actual deletions
> 3\. Audit trail for all purges
> 

### REQ-275 — Selectable Report Data Elements

- Internal key: REQ-8b40b51e287eb2319ac729b20fa6b31ae2ebe9ed9c7058db83ec7a5438870b57
- Type: functional
- Priority: P2
- Priority basis: inferred
- Priority rationale: Selecting report data elements directly affects report usability and is important functionality; the source does not assign a priority\.
- Originating candidates: CAND-dbb6c889ee7b708a3288eef0e22e4c3d64ac4fa010fcb363e64202021c258914

The system shall allow users to select any available data element to include in a report\.

Sources and evidence:

Source: [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>); document ID: DOC-091180de9b2d4ea83267d989411ac89f415d4def3bbf7cd51651fb7fda8d8bf9; normalized lines 623–623.

> - Check off any part of data you want

### REQ-276 — Collection Counts by Genre and Format

- Internal key: REQ-8b4585499327ee31292d05065bd2dc33c6c3f94a3c5a5780257da2f04498126d
- Type: functional
- Priority: P2
- Priority basis: inferred
- Priority rationale: The metric supports collection analysis within the stated reporting scope; no explicit source priority is provided\.
- Originating candidates: CAND-f10479aeb481beded51c02d24ee74a0dfd57e939477120b5ed9121e5228ce516

The system shall count items per genre and format to produce the percentage-of-collection metric\.

Sources and evidence:

Source: [conversations/conv\_pines016\_shelf\_space\.eml](<../data/corpus/conversations/conv_pines016_shelf_space.eml>); document ID: DOC-b507e8abe1ba7c996c1d86d688e90bcf2404694ec00528c8361f26dfc8bd82f1; normalized lines 66–69.

> From a data perspective, we need to:
> 1\. Count items per genre/format \(this is the "percentage of collection"\)
> 2\. Sum checkouts per genre/format \(this is the "percentage of circulations"\)
> 3\. Estimate shelf space per genre/format \(this is the "percentage of shelf space"\)

### REQ-277 — Deletion Tracking by Location and System

- Internal key: REQ-8b50cc7a2add902799915c02a6da09069c78e2035161fb874f51b0958cca34a6
- Type: functional
- Priority: P1
- Priority basis: inferred
- Priority rationale: Deletion tracking supports auditability and compliance across locations and systems\.
- Originating candidates: CAND-ccda4d5b7132404c27aa255b6e37fcd48185a9dc20b6c6c933d37458c25ed678

The system shall count and track record deletions, including item and patron records, per branch and per system\.

Sources and evidence:

Source: [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>); document ID: DOC-091180de9b2d4ea83267d989411ac89f415d4def3bbf7cd51651fb7fda8d8bf9; normalized lines 389–391.

> 10\.9 Deletions Tracking
> Ability to count and track record deletions \(e\.g\., item records, patron records\)
> per location and per system\.

### REQ-278 — Configurable Patron Inactivity Analysis

- Internal key: REQ-8b6de1fd47daed1f9f96459ff01c5e08dea509ea26a831aa26f0c2d9b30cba32
- Type: functional
- Priority: P2
- Priority basis: inferred
- Priority rationale: Inferred as important recurring operational analysis; no explicit source priority is supplied\.
- Originating candidates: CAND-6525261a628a0a11521f32a5790398b9ca97cf97e0d15b97620c3ce2cc6a5c35, CAND-6ff3ce681657abb9346ab5aeeffe36fec45748654c96855c7486bed40ecd5fba

The system shall identify patrons with no circulation or electronic activity during a configurable number of days; it shall support periods of 30, 90, 180, and 365 days, allow any number of days to be specified, and treat OPAC or patron-account logins, online hold placement, online renewals, and access to integrated digital collections as electronic activity\.

Sources and evidence:

Source: [conversations/conv\_pines024\_inactive\_patrons\.eml](<../data/corpus/conversations/conv_pines024_inactive_patrons.eml>); document ID: DOC-705ab8a51bf22b7b619dae61bf8d2be1cf2487e749f13e7ac55fdde430357793; normalized lines 2–3.

> activity in the last X days\. X should be configurable - we usually use 365
> days but it would be nice to adjust\.

Source: [conversations/conv\_pines024\_inactive\_patrons\.eml](<../data/corpus/conversations/conv_pines024_inactive_patrons.eml>); document ID: DOC-705ab8a51bf22b7b619dae61bf8d2be1cf2487e749f13e7ac55fdde430357793; normalized lines 59–64.

> "Electronic activity" should include:
> 1\. Logging into OPAC/patron account
> 2\. Placing holds online
> 3\. Renewing items online
> 4\. Accessing digital collections \(if integrated\)
> 

Source: [conversations/conv\_pines024\_inactive\_patrons\.eml](<../data/corpus/conversations/conv_pines024_inactive_patrons.eml>); document ID: DOC-705ab8a51bf22b7b619dae61bf8d2be1cf2487e749f13e7ac55fdde430357793; normalized lines 68–75.

> For the configurable X days - what ranges make sense?
> - 30 days \(monthly check\)
> - 90 days \(quarterly check\)
> - 180 days \(semi-annual\)
> - 365 days \(annual\)
> 
> Can we make it fully customizable? Like any number of days?
> 

Source: [conversations/conv\_pines024\_inactive\_patrons\.eml](<../data/corpus/conversations/conv_pines024_inactive_patrons.eml>); document ID: DOC-705ab8a51bf22b7b619dae61bf8d2be1cf2487e749f13e7ac55fdde430357793; normalized lines 128–131.

> The system should generate a list of patrons with no circulation or
> electronic activity in the last X days \(X configurable\)\. Electronic activity
> includes OPAC login, online hold placement, online renewals\.
> 

### REQ-279 — Preserve Correctness After Report Template Modification

- Internal key: REQ-8c5bc8cb0f5e65072154696039e05ee9fd567987e95cee2516a8c5e2a4b3e582
- Type: nonfunctional
- Priority: P1
- Priority basis: inferred
- Priority rationale: Incorrect report results undermine reporting reliability and could affect operational and compliance decisions, so this quality constraint is treated as critical\.
- Originating candidates: CAND-a92484bc9ad4bb23e44e084f856d52f357dbbb8bf856fb373fbfb5c7519a4320

The system shall preserve the correctness of report results when report templates are modified\.

Sources and evidence:

Source: [email\_report\_features\.eml](<../data/corpus/email_report_features.eml>); document ID: DOC-d9e168e0c03903021bf9e636e1d8e5f56dfcb79cc110d3839e38175a7c54344e; normalized lines 11–13.

> 2\. REPORT TEMPLATES: Admins need to create report templates that are available
>    to staff\. Templates should be runnable as-is or modified\. Changes shouldn't
>    compromise results\. Admins should be able to limit which filters and display

### REQ-280 — Permission-Controlled Addition of Extra Canned Reports

- Internal key: REQ-8c6f37fe34933f404144236016e0ae8d0ea9cf21b7ab931304732fb9f3720761
- Type: functional
- Priority: P2
- Priority basis: inferred
- Priority rationale: Permission-controlled report extensibility is important for organizational reporting needs, but the source does not establish it as critical\.
- Originating candidates: CAND-c15389e241d81f1cd2aa6c6416a77de3683539064f6965942259a674c99e6a43

The system shall allow additional canned reports to be added under permission-level control\.

Sources and evidence:

Source: [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>); document ID: DOC-091180de9b2d4ea83267d989411ac89f415d4def3bbf7cd51651fb7fda8d8bf9; normalized lines 637–637.

> - Ability to add more canned reports via permission level

### REQ-281 — Management Process Access

- Internal key: REQ-8c9cf6d105b79b0da461665b1032fbe49f6b1298888fc62d473bb746c32fee41
- Type: nonfunctional
- Priority: P2
- Priority basis: inferred
- Priority rationale: The source describes this access as critical because libraries prefer different access modes, but it does not explicitly map that statement to the supplied P-level scale\.
- Originating candidates: CAND-2b5558f3fc6e1eb53479f4dec04000a56b2204ca28322c2b925339a8fc2eda8b

Management Processes shall be accessible through a web browser or a Windows-compatible client\.

Sources and evidence:

Source: [meeting\_minutes/meeting\_2009-07-20\_minutes\.txt](<../data/corpus/meeting_minutes/meeting_2009-07-20_minutes.txt>); document ID: DOC-5ab1dd8bc97af3b1ab2e378495f0e0d75fd501fcc19f923c0d8fda831074281b; normalized lines 82–86.

> OE-3: Management Processes shall be accessible through a web-browser or a
>       Windows-compatible client\.
>       \[Discussion: This is critical - some libraries prefer browser-based
>       access \(no client install\), others prefer the dedicated client for
>       better performance\.\]

### REQ-282 — Inactive Patron Activity Report

- Internal key: REQ-8d7bbbf2cf6bad036b7a0558c0f18a69c5aa7cdd2275cb289db4e26f8c8760e0
- Type: functional
- Priority: P2
- Priority basis: inferred
- Priority rationale: The source identifies this as a needed operational report and specifies configurable X, but assigns no P-level priority\.
- Originating candidates: CAND-338906b17783c1e7a062385f6d2f651f722cb88917910451888cbe6c1da192b6

The system shall generate a report or list of patrons with no circulation or electronic activity during the last configurable X days\.

Sources and evidence:

Source: [conversations/conv\_pines024\_inactive\_patrons\.eml](<../data/corpus/conversations/conv_pines024_inactive_patrons.eml>); document ID: DOC-705ab8a51bf22b7b619dae61bf8d2be1cf2487e749f13e7ac55fdde430357793; normalized lines 1–3.

> We need a report that shows patrons with no circulation or electronic
> activity in the last X days\. X should be configurable - we usually use 365
> days but it would be nice to adjust\.

Source: [conversations/conv\_pines024\_inactive\_patrons\.eml](<../data/corpus/conversations/conv_pines024_inactive_patrons.eml>); document ID: DOC-705ab8a51bf22b7b619dae61bf8d2be1cf2487e749f13e7ac55fdde430357793; normalized lines 126–131.

> Requirement consolidated:
> 
> The system should generate a list of patrons with no circulation or
> electronic activity in the last X days \(X configurable\)\. Electronic activity
> includes OPAC login, online hold placement, online renewals\.
> 

### REQ-283 — OPAC Patron Data Access for Management Processes

- Internal key: REQ-8e6224a751d8131f6bb8e55a2b3f3476c8a5a02b106014ef80d80863ee2e8aac
- Type: functional
- Priority: P2
- Priority basis: inferred
- Priority rationale: This enables reporting on patron data created through the OPAC and supports important management processes\.
- Originating candidates: CAND-9db5584ae85dac5b6ed40f6f61553749e5825a2aa0e2845f29c9e2baae13bea2

Management Processes shall interact with the Online Public Access Catalog and shall be able to query patron data such as holds and circulation\.

Sources and evidence:

Source: [meeting\_minutes/meeting\_2009-07-20\_minutes\.txt](<../data/corpus/meeting_minutes/meeting_2009-07-20_minutes.txt>); document ID: DOC-5ab1dd8bc97af3b1ab2e378495f0e0d75fd501fcc19f923c0d8fda831074281b; normalized lines 189–192.

> DE-3: Management Processes interact with a patron interface, also known as an
>       Online Public Access Catalog \(OPAC\)\.
>       \[Discussion: Patron data \(holds, circulation\) is created in the OPAC\.
>       Our reports need to query this data\.\]

### REQ-284 — Checkout Counts by Individual and Cumulative Checkout Type

- Internal key: REQ-8e6d56b291cb5b74a95397bc1ffdb3386f0b867820c998d2300b5702688943f7
- Type: functional
- Priority: P2
- Priority basis: inferred
- Priority rationale: Detailed circulation counts support management reporting, but no explicit priority is supplied\.
- Originating candidates: CAND-4eeb11030f1b22afa583cb6df81b09fc54e4ed1c3724b9f1b8b123703804eb12

The system shall count each checkout type individually and cumulatively, including staff checkout, self checkout, staff renewal, self checkout renewal, online renewal, and OPAC renewal\.

Sources and evidence:

Source: [survey\_results\_2009\.txt](<../data/corpus/survey_results_2009.txt>); document ID: DOC-aac7bceef7a883652805583e98ec513b6ae2e7951e2ecfa18722127b1f12a5c4; normalized lines 117–119.

> 4\. All types of check-out counted individually and cumulatively: staff checkout,
>    self checkout, staff renewal, self checkout renewal, online renewal, OPAC
>    renewal\.

### REQ-285 — Uncataloged Material Transaction Counts in Circulation Statistics

- Internal key: REQ-8ea032b7c4ecfb681eec7b23aaa46bfd1e15b3094e13fedc3832a7e19ccfccff
- Type: functional
- Priority: P2
- Priority basis: inferred
- Priority rationale: Supports complete circulation statistics\.
- Originating candidates: CAND-d7941b4db384ba47bd026dad79bad2e252ef0b18d01c5d34dadca424b1fc4c8e

The system shall count transactions for uncataloged material and include those counts in circulation statistics and reports\.

Sources and evidence:

Source: [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>); document ID: DOC-091180de9b2d4ea83267d989411ac89f415d4def3bbf7cd51651fb7fda8d8bf9; normalized lines 351–352.

> Ability to count transactions and include in circulation statistics and
> reports\.

### REQ-286 — Fine-Grained Permissions for Report Creation and Cloning

- Internal key: REQ-901cf3a8a5cbe9cefb77128edcf0929c6abc5ded0f8393b350b6cacf317b11e6
- Type: functional
- Priority: P2
- Priority basis: inferred
- Priority rationale: Controlling report creation and cloning protects reporting functions and has substantial administrative impact\.
- Originating candidates: CAND-972bd6fb98361cf24737267dddd887376654510d19c82143e32e84d2c82db41c

The system shall use fine-grained permissions to limit which users may create and clone reports\.

Sources and evidence:

Source: [survey\_results\_2009\.txt](<../data/corpus/survey_results_2009.txt>); document ID: DOC-aac7bceef7a883652805583e98ec513b6ae2e7951e2ecfa18722127b1f12a5c4; normalized lines 135–136.

> 10\. Fine-grained permissions limit who can create and clone reports\.
> 

### REQ-287 — Environment configuration migration export/import

- Internal key: REQ-9080886072a096004bc8d03bb4aa40635fa547530d19deeefd7a53594fef15dc
- Type: functional
- Priority: P2
- Priority basis: inferred
- Priority rationale: Migration between operational environments has substantial deployment and administration impact; the source does not establish a more specific priority\.
- Originating candidates: CAND-89f23663d56f1a10d52ea2882c947d1caf288f7f2540dd325cf9f905973ffddf

The system shall provide export and import mechanisms to migrate templates, permission settings, and saved queries between development, training, and production environments\.

Sources and evidence:

Source: [meeting\_tech\_subcommittee\_2009-06-30\.txt](<../data/corpus/meeting_tech_subcommittee_2009-06-30.txt>); document ID: DOC-e081aa7bd57bf5e59c75a8a86f592124757b74dff1ee0df4badc10c025092d96; normalized lines 53–55.

> "We have a dev server, a training server, and production," Robert explained\.
> "What we need is a way to migrate configurations between them\. Export/import
> of templates, permission settings, and saved queries\."

### REQ-288 — Enhanced Last Copy Report to Protect Sole Copies

- Internal key: REQ-9134e1fed77978c60fb2413ae36402b8b14a44f8163f3d7e9e65743731662c19
- Type: functional
- Priority: P1
- Priority basis: explicitly specified
- Priority rationale: The source explicitly labels the last copy report as critical and ties it to preventing accidental deletion of the only consortium copy\.
- Originating candidates: CAND-b9e93d46ca2cb5f59659a364cb1f94bcc9f3c11008a3b7eb8cb41a71d1a392ce, CAND-c70e64fe2b184be0202659711f54d06217522bb993a6643757739291f02055b3

The system shall provide an enhanced last copy report that identifies a library system's last copies to assist catalogers in updating WorldCat entries without accidentally deleting the only copy in the consortium\.

Sources and evidence:

Source: [conversations/conv\_pines021\_item\_purging\.eml](<../data/corpus/conversations/conv_pines021_item_purging.eml>); document ID: DOC-74ccbb6ac77183c0d1b34b1e79ed8fcbbfb4e7525cb33798c3af832fed733ad8; normalized lines 13–15.

> 3\. CRITICAL: We need a "last copy report" that identifies our library
>    system's last copies\. This helps catalogers update WorldCat entries
>    so we don't accidentally delete the only copy in the consortium\.

Source: [conversations/conv\_pines021\_item\_purging\.eml](<../data/corpus/conversations/conv_pines021_item_purging.eml>); document ID: DOC-74ccbb6ac77183c0d1b34b1e79ed8fcbbfb4e7525cb33798c3af832fed733ad8; normalized lines 131–132.

> - Provide a last copy report singling out a library system's last copies,
>   to assist catalogers who need to edit WorldCat entries

Source: [evergreen\_reference\_2009\.txt](<../data/corpus/evergreen_reference_2009.txt>); document ID: DOC-e6aa9f8c6308ab748459f87b578a0df9df9c865b7911bac3686e865963b7af6f; normalized lines 145–145.

> - Last Copy Report \(partially available, needs enhancement\)

### REQ-289 — Anonymized Demographic Statistics

- Internal key: REQ-91f40e4f994a661fbd58a544bc85c0f7d57b247aee518094ca62f72dc34ecc66
- Type: nonfunctional
- Priority: P1
- Priority basis: inferred
- Priority rationale: Protecting patron identifiability is a privacy and compliance concern\.
- Originating candidates: CAND-d0b9a48e96307475db583e46bb29db395074117652a39ef119f20ef0657091b2

The system shall anonymize data used to produce demographic statistics by deleting information that could be used to identify a patron\.

Sources and evidence:

Source: [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>); document ID: DOC-091180de9b2d4ea83267d989411ac89f415d4def3bbf7cd51651fb7fda8d8bf9; normalized lines 318–320.

> by geographical regions, age ranges, etc\. The data used to produce these
> statistics must be anonymized - information that could be used to identify a
> patron is deleted\.

### REQ-290 — Vendor Interfaces via APIs or Standard Data Files

- Internal key: REQ-92690e7229e8e98217908fd4b252b561e24c36d8008f455021f96c3b5461cd3a
- Type: nonfunctional
- Priority: P2
- Priority basis: inferred
- Priority rationale: External interoperability is important to management operations, but no explicit priority is supplied\.
- Originating candidates: CAND-528b742017846017eda4a28de291243864d008e8f6b8105d5553b9c33f7e4985

Management Processes shall interface with vendor websites through published APIs or automated transfer of standard-format data files, including formats such as USMARC21 and EDIFACT\.

Sources and evidence:

Source: [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>); document ID: DOC-091180de9b2d4ea83267d989411ac89f415d4def3bbf7cd51651fb7fda8d8bf9; normalized lines 211–213.

> DE-2: Management Processes interface with a variety of vendor websites, via
>       published APIs and/or automated transfer of standard-format data files
>       \(e\.g\., USMARC21, EDIFACT\)\.

### REQ-291 — Financial Transaction Reporting Capabilities

- Internal key: REQ-92bb4dd94489df26ced5202fc9574a69e5656f3613a6d0f251ac4bbe89352d83
- Type: functional
- Priority: P1
- Priority basis: inferred
- Priority rationale: Inferred as critical because financial tracking and verification support financial control and auditability\.
- Originating candidates: CAND-710d77d9020152a42ed48b85c8cce791461d677e82674719081815f65625ee92

The system shall provide reporting capabilities to track and verify financial transactions\.

Sources and evidence:

Source: [meeting\_minutes/meeting\_2009-03-15\_minutes\.txt](<../data/corpus/meeting_minutes/meeting_2009-03-15_minutes.txt>); document ID: DOC-defef992db2ae0e10167fd94902eac93f82c59c4c070df030ca2f77811082818; normalized lines 63–64.

>   - Tracking and verifying financial transactions
> 

### REQ-292 — Pivot-Table Output for Reports

- Internal key: REQ-9315fc23c9498813e0135ab7ec19eccd2821ddf3c9ceb8f1c1a7a9bcfc38ab07
- Type: functional
- Priority: P3
- Priority basis: inferred
- Priority rationale: Inferred as useful report analysis functionality; no explicit source priority is supplied\.
- Originating candidates: CAND-6bdfdcb8f5ea58189e87b8a6dca662af7f1a00f8d924aabfb037b1dcd10666d2

The system shall provide pivot-table output for reports\.

Sources and evidence:

Source: [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>); document ID: DOC-091180de9b2d4ea83267d989411ac89f415d4def3bbf7cd51651fb7fda8d8bf9; normalized lines 649–649.

> - Pivot table output

### REQ-293 — Last-Copy Report

- Internal key: REQ-93ff13e5f1b1dd8612c680769837792c2a0f9e80d66939fb6e5636dbf851bacd
- Type: functional
- Priority: P1
- Priority basis: explicitly specified
- Priority rationale: The source explicitly describes the last-copy report as critical because it helps prevent accidental deletion and supports catalog maintenance\.
- Originating candidates: CAND-247e727333db03eb1ef134d8765073dd09c3f89803389eb0ca2dca942efeb1e6

The system shall provide a last-copy report that identifies a library system’s last copies to help prevent accidental deletion and assist catalogers editing WorldCat entries\.

Sources and evidence:

Source: [interview\_cataloging\_2009-05-08\.txt](<../data/corpus/interview_cataloging_2009-05-08.txt>); document ID: DOC-a79fab45108210e6bce7d92153dfcf055f2ef6b2cdab49a3f6f5717a3e35f29f; normalized lines 80–83.

> And the last copy report is CRITICAL\. This singles out a library system's last
> copies, to assist catalogers who need to edit WorldCat entries\. Last month, we
> almost deleted our last copy of a rare book before someone remembered to check
> WorldCat\. If we had a report like this, it would save us from that situation\.

### REQ-294 — Aggregate Item Purchase Prices for Reporting

- Internal key: REQ-9489f0f1a9476e68442675d818e19ae6035f739d1489e5beb4b8f9443cbe5768
- Type: functional
- Priority: P2
- Priority basis: inferred
- Priority rationale: This provides a requested financial analysis based on existing item data\.
- Originating candidates: CAND-39cc7f882373c242a21e240c969f085209db9abb60c99b7ab701467786648ef8

The system shall query and aggregate the purchase-price field in item records to compute item values for reporting\.

Sources and evidence:

Source: [email\_financial\_reports\.eml](<../data/corpus/email_financial_reports.eml>); document ID: DOC-8b6cfb3cf368b794d82567933f9c85062740814819b1e28b4837f6021cbcbee6; normalized lines 46–48.

> - Regarding the "value of items report" - the data is already in the item
>   records \(purchase price field\)\. We just need the system to be able to query
>   and aggregate this\. This should be straightforward\.

### REQ-295 — Rapid Uncataloged Material Distribution

- Internal key: REQ-9550e74f4358e59fdb834160cd6c82d5af698ef9eeee8e5ba97342819fb0cab6
- Type: nonfunctional
- Priority: P2
- Priority basis: inferred
- Priority rationale: The source specifies rapid processing and minimal branch labor as required operational outcomes; the source does not assign a priority\.
- Originating candidates: CAND-dd32d3617e73dbf9e57c6aa210f3463a3e38222538fcf3a9c1341e18db193e4a

The system shall support quick distribution processing for uncataloged material and shall minimize branch labor required per item\.

Sources and evidence:

Source: [interview\_cataloging\_2009-05-08\.txt](<../data/corpus/interview_cataloging_2009-05-08.txt>); document ID: DOC-a79fab45108210e6bce7d92153dfcf055f2ef6b2cdab49a3f6f5717a3e35f29f; normalized lines 34–36.

> The requirements are: quick distribution \(we need to process these fast\),
> minimal branch labor \(we can't spend a lot of time per item\), and ability to
> identify how the material is being used\. We also need to count transactions

### REQ-296 — Join Patron and Item Financial Data for Financial Reports

- Internal key: REQ-95ba89b96696c858a6c40748d55622b8824772ceeec1abf0c72d1c924ec94932
- Type: functional
- Priority: P1
- Priority basis: inferred
- Priority rationale: Inferred as critical because the source requires financial reporting across both patron and item records to support financial reconciliation\.
- Originating candidates: CAND-714eff94d1667f6ca43ed80dacbe68f126071db527de4b5cceab3262e6eeb09b

When generating financial reports, the system shall join financial data attached to patron records with financial data attached to item records\.

Sources and evidence:

Source: [email\_financial\_reports\.eml](<../data/corpus/email_financial_reports.eml>); document ID: DOC-8b6cfb3cf368b794d82567933f9c85062740814819b1e28b4837f6021cbcbee6; normalized lines 64–66.

> - The financial data is attached to patron records AND item records\. So when
>   we query for financial reports, we need to be able to join these data sources\.
> 

Source: [email\_financial\_reports\.eml](<../data/corpus/email_financial_reports.eml>); document ID: DOC-8b6cfb3cf368b794d82567933f9c85062740814819b1e28b4837f6021cbcbee6; normalized lines 116–119.

> 3\. FINANCIAL DATA \(PATRONS\):
>    Fines, charges, waivers, and ecommerce transactions are attached to patron
>    and item records\. System tracks fines waived and payments made per library\.
>    Financial information can be updated easily\. A staff user can easily query

### REQ-297 — Separate Reporting from Production

- Internal key: REQ-96002f3d3db7fd77af98c48a3a4bef6e9c43c8548bf96dde6253e733125cec7f
- Type: nonfunctional
- Priority: P2
- Priority basis: inferred
- Priority rationale: Protects production availability and performance\.
- Originating candidates: CAND-d42a11233c968c6812c3ce3d870cbfac439a900be355d454e90c091991c1b2a4

The system shall separate reporting from production operations, including by using a separate reporting database or replica when appropriate, and shall avoid running heavy reports on production operations\.

Sources and evidence:

Source: [evergreen\_reference\_2009\.txt](<../data/corpus/evergreen_reference_2009.txt>); document ID: DOC-e6aa9f8c6308ab748459f87b578a0df9df9c865b7911bac3686e865963b7af6f; normalized lines 219–219.

> 6\. Separate reporting from production operations

### REQ-298 — Busy-Hour Report Performance Constraint

- Internal key: REQ-968ed81502d16790f38794f66aab29f219af762f09c89cf8d77e5a84160e83fe
- Type: nonfunctional
- Priority: P2
- Priority basis: inferred
- Priority rationale: Report responsiveness during busy hours materially affects operational usability, but no measurable service level is provided\.
- Originating candidates: CAND-189c8a495d293566e6b2d2d067404c64c7b639cbd8dec37d339235eea812113b

The system shall ensure that reports do not take too long to run during busy hours\.

Sources and evidence:

Source: [survey\_results\_2009\.txt](<../data/corpus/survey_results_2009.txt>); document ID: DOC-aac7bceef7a883652805583e98ec513b6ae2e7951e2ecfa18722127b1f12a5c4; normalized lines 70–70.

>   - "Reports take too long to run during busy hours"

### REQ-299 — Unfilled Holds Report

- Internal key: REQ-96a0a661a772b9eacf94509db1b9c2107f58d40e42191d3bf63b50343c24e142
- Type: functional
- Priority: P3
- Priority basis: inferred
- Priority rationale: This is a useful hold-management report but is not shown to be essential to basic operation\.
- Originating candidates: CAND-53428a2ff442116121eb96a63cefc9f0b3de86e51ba12432c486e6a7f63dade7

The system shall provide an Unfilled Holds report\.

Sources and evidence:

Source: [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>); document ID: DOC-091180de9b2d4ea83267d989411ac89f415d4def3bbf7cd51651fb7fda8d8bf9; normalized lines 569–569.

> - Unfilled Holds

### REQ-300 — Report Result Identification

- Internal key: REQ-96ad5648aad0d60583508a1dc21bdb329cce2ea34f44177f1d4efda7d27f37f7
- Type: functional
- Priority: P2
- Priority basis: inferred
- Priority rationale: Identifying report scope improves the reliability and usability of reporting output, but no explicit priority is supplied\.
- Originating candidates: CAND-330af25d6aa5626df4d41791bd9a725af9fc4dabcb87980223ba0336d89262d1

The system shall include the selected date criteria and the report name at the top or bottom of report results\.

Sources and evidence:

Source: [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>); document ID: DOC-091180de9b2d4ea83267d989411ac89f415d4def3bbf7cd51651fb7fda8d8bf9; normalized lines 659–660.

> - Report results would include the date selection criteria at the top or bottom
>   to quickly see date range selected along with the name of the report

### REQ-301 — Manual Selection of Titles or Items from Query Results

- Internal key: REQ-97fa935a0d52bfa813c0a18133690ba835253bfb6236d1efd3d7305ffd26d8d1
- Type: functional
- Priority: P2
- Priority basis: inferred
- Priority rationale: Manual subset selection is needed for controlled action on query results and is explicitly requested\.
- Originating candidates: CAND-46458ab91f305f2be1d041a5393d6c08a14ddd03e330576ec232e64dd04d5648

The system shall allow users to manually select titles or items from query results, including selecting a subset using check boxes\.

Sources and evidence:

Source: [conversations/conv\_pines018\_item\_transfer\.eml](<../data/corpus/conversations/conv_pines018_item_transfer.eml>); document ID: DOC-a47eb1f11286ff9099687b72a901e4a6ed2455b431087c0742aa78583c5bd80a; normalized lines 113–116.

> I also want to be able to MANUALLY SELECT from query results\. Maybe I
> run a query and get 100 candidate items, but I only want to move 25 of
> them\. I should be able to check boxes and select which ones to include\.
> 

### REQ-302 — Uncataloged Material Inventory Control

- Internal key: REQ-97fda17c62526fbd57a9cd61ccd4eac31076728d1286dbc3693b61b9e881461b
- Type: functional
- Priority: P2
- Priority basis: inferred
- Priority rationale: This supports material distribution and usage tracking with operational impact, but no explicit priority is supplied\.
- Originating candidates: CAND-57b68f1f07814ebe8636037a9fe8037294884431e0b1285289defb48414a9ee1

The system shall provide the ability to control inventory of uncataloged material, including paperback books and children's board books, while supporting quick distribution, minimal branch labor, and identification of how the material is being used\.

Sources and evidence:

Source: [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>); document ID: DOC-091180de9b2d4ea83267d989411ac89f415d4def3bbf7cd51651fb7fda8d8bf9; normalized lines 344–350.

> 10\.4 Uncataloged Material
> Ability to control inventory of uncataloged material, such as paperback books
> and children's board books\. Support needed for:
>   - Quick distribution
>   - Minimal branch labor
>   - Ability to identify how the material is being used
> 

### REQ-303 — Document Branch Capacity Metrics Before Capacity Interface

- Internal key: REQ-983e2944d476bd25ab51211437e775c1f4d53221c0318bdfc06bd833671f2542
- Type: functional
- Priority: P2
- Priority basis: inferred
- Priority rationale: A defined capacity measure is important to the correctness of any capacity interface, but the supplied evidence does not establish a critical safety, security, compliance, or core-operation priority\.
- Originating candidates: CAND-ffc4099894dab9631579d30b9d3be3f70b16ecf621010888bb568c779a723e51

The system shall define and document which specific metrics constitute branch capacity before building a capacity interface; the supplied alternatives—number of items versus shelf space, number of physical items versus a configured limit, and circulation volume versus processing capacity—remain unresolved and shall not be selected without stakeholder clarification\.

Sources and evidence:

Source: [conversations/conv\_pines015\_capacity\_interface\.eml](<../data/corpus/conversations/conv_pines015_capacity_interface.eml>); document ID: DOC-4acf2fdb375b86d49420e5743267e19b3f0af9ebe8bd764c1a88379aa9f5b662; normalized lines 52–56.

> Also, what specific metrics define "capacity"? Is it:
> - Number of items vs\. shelf space?
> - Number of physical items vs\. a configured limit?
> - Circulation volume vs\. processing capacity?
> 

Source: [conversations/conv\_pines015\_capacity\_interface\.eml](<../data/corpus/conversations/conv_pines015_capacity_interface.eml>); document ID: DOC-4acf2fdb375b86d49420e5743267e19b3f0af9ebe8bd764c1a88379aa9f5b662; normalized lines 57–57.

> Need to nail this down before building the interface\.

### REQ-304 — Edit Recurring Reports Including Selections and Email Addresses

- Internal key: REQ-987cc70e7e6b615dd653632904fce88c54622f895dbba9bf474c07c437d814dd
- Type: functional
- Priority: P3
- Priority basis: inferred
- Priority rationale: Inferred as medium priority because editing recurring reports supports report administration but is not identified as essential\.
- Originating candidates: CAND-7dc1f716197a0c43209cf2c7342cf0cbe5d6e4e5e9d799b2d95990797a7dff44

The system shall allow recurring reports to be edited by adding or removing report selections and editing their email addresses\.

Sources and evidence:

Source: [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>); document ID: DOC-091180de9b2d4ea83267d989411ac89f415d4def3bbf7cd51651fb7fda8d8bf9; normalized lines 628–629.

> - Ability to edit recurring reports by adding or removing report selections
>   as well as editing the email addresses

### REQ-305 — Branch Capacity Drilldown

- Internal key: REQ-994cdfd99eeed77986033145b1b7d8b9a9fd8b5fb4415a4390477b0d424563b3
- Type: functional
- Priority: P2
- Priority basis: inferred
- Priority rationale: Inferred as important operational analysis functionality; no explicit source priority is supplied\.
- Originating candidates: CAND-64dd892986d23319d8fe445b4f292b9d0a93176635bfbed52cb16196762261c1

The system shall allow users to drill down from an overview into individual branches to view detailed capacity information\.

Sources and evidence:

Source: [conversations/conv\_pines015\_capacity\_interface\.eml](<../data/corpus/conversations/conv_pines015_capacity_interface.eml>); document ID: DOC-4acf2fdb375b86d49420e5743267e19b3f0af9ebe8bd764c1a88379aa9f5b662; normalized lines 33–36.

> I think we need:
> 1\. A high-level summary view \(all branches, key metrics\)
> 2\. Ability to drill down into individual branches
> 3\. Maybe color-coding - green for under capacity, yellow for getting full,

Source: [conversations/conv\_pines015\_capacity\_interface\.eml](<../data/corpus/conversations/conv_pines015_capacity_interface.eml>); document ID: DOC-4acf2fdb375b86d49420e5743267e19b3f0af9ebe8bd764c1a88379aa9f5b662; normalized lines 85–86.

> - High-level overview of all branches' capacity at once
> - Ability to drill down into individual branches

### REQ-306 — Text-File Report Filtering

- Internal key: REQ-99ee3fb2cebef41e79d5c214c94a23f682ee6ff752a8a5fc9113220a678c7b83
- Type: functional
- Priority: P2
- Priority basis: inferred
- Priority rationale: This capability improves report selection workflows, but no explicit priority is supplied\.
- Originating candidates: CAND-2ea79939686c908ea6ca417f2bcb5a927839f5aad8b5e3a6aeef8864ef55146c

The system shall allow staff to upload text files containing values such as barcodes or TCNs and use those values as selection criteria for reports\.

Sources and evidence:

Source: [evergreen\_reference\_2009\.txt](<../data/corpus/evergreen_reference_2009.txt>); document ID: DOC-e6aa9f8c6308ab748459f87b578a0df9df9c865b7911bac3686e865963b7af6f; normalized lines 175–175.

> - No ability to upload text files for filtering \(barcodes, TCNs\)

### REQ-307 — Background Processing or Queuing for Long-Running Reports

- Internal key: REQ-9a62d854296eab1382d7396fb8748a06178ae56447fc095afe6b7a81cf1f26c4
- Type: nonfunctional
- Priority: P1
- Priority basis: inferred
- Priority rationale: Preventing reporting from affecting circulation operations protects core operation, but no explicit priority is supplied\.
- Originating candidates: CAND-483f228e8b04032feccfa6743d636fe3767982bc3f0bc4a665bd5f7f796ffe52, CAND-49f2468c9084efdcc077175f4ee0bc1032ac9dda61c4f4feb645d64174bbda76

The system shall provide background processing or queuing for long-running report generation so that report generation does not slow down the circulation client\.

Sources and evidence:

Source: [evergreen\_reference\_2009\.txt](<../data/corpus/evergreen_reference_2009.txt>); document ID: DOC-e6aa9f8c6308ab748459f87b578a0df9df9c865b7911bac3686e865963b7af6f; normalized lines 183–183.

> - No background processing for long-running reports

Source: [meeting\_minutes/meeting\_2009-07-20\_minutes\.txt](<../data/corpus/meeting_minutes/meeting_2009-07-20_minutes.txt>); document ID: DOC-5ab1dd8bc97af3b1ab2e378495f0e0d75fd501fcc19f923c0d8fda831074281b; normalized lines 73–76.

>       \[Discussion: George noted that Evergreen already handles this scale\.
>       The concern is about report processing during peak hours\. We need
>       background processing/queuing to prevent report generation from slowing
>       down the circulation client\.\]

### REQ-308 — Display Report Selection Criteria Alongside Results

- Internal key: REQ-9abc4859ea4f78e036e40092e1b053c532d09862cf20c8bac4f31ff817b9ac48
- Type: functional
- Priority: P2
- Priority basis: inferred
- Priority rationale: Users need this capability to interpret and verify report results\.
- Originating candidates: CAND-3943d017bbe9155bc4d8c9581687c9b6b483b81991e327be1101f977c7cdd366, CAND-3a0b2fd351b8a6606350f8226579eeb12c5cdc5dcb7091f4c78be7761cf21cf4

The system shall display the query selections or selection criteria used to generate report results alongside those results\.

Sources and evidence:

Source: [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>); document ID: DOC-091180de9b2d4ea83267d989411ac89f415d4def3bbf7cd51651fb7fda8d8bf9; normalized lines 289–292.

> 8\.8 Query Selections Display
> The system should provide the query selections along with the results, so users
> can see what criteria were used to generate the report\.
> 

Source: [evergreen\_reference\_2009\.txt](<../data/corpus/evergreen_reference_2009.txt>); document ID: DOC-e6aa9f8c6308ab748459f87b578a0df9df9c865b7911bac3686e865963b7af6f; normalized lines 176–176.

> - No selection criteria display in report results

### REQ-309 — Generate Item Value Report by Collection and Item Status

- Internal key: REQ-9af7d80d0eb3bab6a034404290bc83407b77174a4d06dcb2a1591f58e30f591f
- Type: functional
- Priority: P2
- Priority basis: inferred
- Priority rationale: Collection valuation supports financial and collection-management decisions, but the source does not assign an explicit priority\.
- Originating candidates: CAND-b5b8877697ddd79a308e865825b9671203a11955fe8dfdf7a7abac66e8bbc453

The system shall generate a report of item value based on data in item records for the entire collection or a specified portion, including items selected by status, such as "longoverdue," and by collection, such as DVDs in the children's collection\.

Sources and evidence:

Source: [email\_financial\_reports\.eml](<../data/corpus/email_financial_reports.eml>); document ID: DOC-8b6cfb3cf368b794d82567933f9c85062740814819b1e28b4837f6021cbcbee6; normalized lines 8–13.

> 1\. Value of items report - staff should be able to get the value of items
>    based on data in item records\. This could be the entire collection, or a
>    portion\. For example, they want to be able to get:
>    - Value of all items with status "longoverdue"
>    - Value of all DVDs in children's collection
>    - Value of entire collection

Source: [email\_financial\_reports\.eml](<../data/corpus/email_financial_reports.eml>); document ID: DOC-8b6cfb3cf368b794d82567933f9c85062740814819b1e28b4837f6021cbcbee6; normalized lines 106–110.

> 1\. VALUE OF ITEMS REPORT:
>    System can generate a report of the value of items \(based on data in item
>    record\) in the entire collection or a portion\. Examples: value of all items
>    with status of "longoverdue", value of all DVDs in children's collection,
>    value of entire collection\.

### REQ-310 — Item-Level Holds Report

- Internal key: REQ-9b6a0e7273fde31be149bb6ef5d19ba13ecf50061cbb4b9a7bff50a616c82fa1
- Type: functional
- Priority: P2
- Priority basis: inferred
- Priority rationale: This supports circulation operations; the source does not identify it as critical\.
- Originating candidates: CAND-9aac6402d5da958aeb67c2418c3c056426f513bf6410d31e3332bc6f42df9f47

The system shall provide a report of item-level holds\.

Sources and evidence:

Source: [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>); document ID: DOC-091180de9b2d4ea83267d989411ac89f415d4def3bbf7cd51651fb7fda8d8bf9; normalized lines 277–280.

>   - Bibliographic records with holds
>   - Items that have not been checked out in X days
>   - Item-level holds
>   - Items with invalid item type

### REQ-311 — Configurable Transaction History Retention

- Internal key: REQ-9bed4e5fa63e162aad9174dfab25d412e43f8e4b9584b685a54fe73cebc718bd
- Type: functional
- Priority: P2
- Priority basis: inferred
- Priority rationale: Supports important operational and management reporting\.
- Originating candidates: CAND-c874d30522c1e3c37e24fc1bd1bf92d3a084fbe8f9c1f8ebdd210469d4feca0f

The system shall maintain transaction history for X days, where X is configurable, and shall maintain monthly and annual aggregate information indefinitely\.

Sources and evidence:

Source: [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>); document ID: DOC-091180de9b2d4ea83267d989411ac89f415d4def3bbf7cd51651fb7fda8d8bf9; normalized lines 416–419.

> 12\.1 Transaction History Maintenance
> Transaction history is maintained for X days \(X is configurable\)\. Monthly and
> annual aggregate information is maintained indefinitely\.
> 

### REQ-312 — Data Quality Reports

- Internal key: REQ-9cae740e23764f4586af93809cd3c99de5668733752bfcc9e95d35865c34bccc
- Type: functional
- Priority: P2
- Priority basis: inferred
- Priority rationale: Data quality reporting is important for dependable system data, but no explicit priority is supplied\.
- Originating candidates: CAND-59b2b5a9dbc557ef0af7c9154f071fc2d4cb34c8aa75aae6e231aa5ca7ef63f9

The system shall provide data quality reports\.

Sources and evidence:

Source: [meeting\_minutes/meeting\_2009-07-20\_minutes\.txt](<../data/corpus/meeting_minutes/meeting_2009-07-20_minutes.txt>); document ID: DOC-5ab1dd8bc97af3b1ab2e378495f0e0d75fd501fcc19f923c0d8fda831074281b; normalized lines 43–43.

>   - Data quality reports are needed

### REQ-313 — Email Delivery for Reports

- Internal key: REQ-9df10e7759c5f2c8ec63077923cea5c298616a4e8907431da10b02b38862a26c
- Type: functional
- Priority: P3
- Priority basis: inferred
- Priority rationale: The source identifies email delivery as a requested reporting capability but does not establish a higher priority\.
- Originating candidates: CAND-bb9937f47c2f0fa6dbfd70b206f3c74cfc87e41c1024ab58643d228f500fe25d

The system shall support delivery of reports by email\.

Sources and evidence:

Source: [survey\_results\_2009\.txt](<../data/corpus/survey_results_2009.txt>); document ID: DOC-aac7bceef7a883652805583e98ec513b6ae2e7951e2ecfa18722127b1f12a5c4; normalized lines 65–65.

>   - Email delivery of reports: 45%

### REQ-314 — Current Patron Bills Report

- Internal key: REQ-9e7f49fdddb3eee3c42f36a7e472c91a4918daf3b5e08c36b24a2486de377fe2
- Type: functional
- Priority: P2
- Priority basis: inferred
- Priority rationale: This is a specific financial and patron-account reporting capability\.
- Originating candidates: CAND-424dff222e8481322d23bb9321119b0961b3b486b10dc377a34b7472c7fdd201

The system shall provide a report of bills currently owed by patrons\.

Sources and evidence:

Source: [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>); document ID: DOC-091180de9b2d4ea83267d989411ac89f415d4def3bbf7cd51651fb7fda8d8bf9; normalized lines 582–582.

> - Bills currently Owed by Patrons

### REQ-315 — Deletions Broken Down by Location

- Internal key: REQ-9f3aa7e6a95ffe19b1d3e7f6799a7a93e8ece53b74eef326ef1425bf6b228388
- Type: functional
- Priority: P2
- Priority basis: inferred
- Priority rationale: Location-based deletion reporting supports oversight and accountability, but no explicit priority is supplied\.
- Originating candidates: CAND-5f97ee0a781e0bd8e84f48fdfe563700c395e660218cd6d244e4209c806f7411

Reports shall include deletions broken down by location\.

Sources and evidence:

Source: [conversations/conv\_pines022\_deletions\.eml](<../data/corpus/conversations/conv_pines022_deletions.eml>); document ID: DOC-7b8da7c05931fc99bc80d4a4bb0c8563e690e0c415b57f5ca1ae394462dc26c8; normalized lines 72–72.

> - Deletions by location

### REQ-316 — Configure Organizational Scope for Reports and Lists

- Internal key: REQ-a089b86d6ade163bc3a5fc8250e8bf76d8cace1d40f96544cb31c6d60283b1c7
- Type: functional
- Priority: P2
- Priority basis: inferred
- Priority rationale: Inferred as high priority because configurable organizational scope is important for reporting across the stated levels\.
- Originating candidates: CAND-77044be17fd85b79b4783b7e4101855bba06292905b6059bc880c7b9a8f467a3

The system shall allow report and list scope to be configured for organizational levels including System, Home Library, County, and other required levels\.

Sources and evidence:

Source: [conversations/conv\_pines024\_inactive\_patrons\.eml](<../data/corpus/conversations/conv_pines024_inactive_patrons.eml>); document ID: DOC-705ab8a51bf22b7b619dae61bf8d2be1cf2487e749f13e7ac55fdde430357793; normalized lines 5–6.

> The list should be configurable to different levels - System, Home Library,
> County, etc\.

Source: [conversations/conv\_pines024\_inactive\_patrons\.eml](<../data/corpus/conversations/conv_pines024_inactive_patrons.eml>); document ID: DOC-705ab8a51bf22b7b619dae61bf8d2be1cf2487e749f13e7ac55fdde430357793; normalized lines 132–136.

> The list should be configurable to:
> - System
> - Home Library
> - County
> - \(Other levels as needed\)

### REQ-317 — Last-Copy Report with Per-Library and System Views

- Internal key: REQ-a08f6429a3f24e2739cba78f7be907fdadf698ad67e94db216d67ed10c4129e8
- Type: functional
- Priority: P1
- Priority basis: explicitly specified
- Priority rationale: The source explicitly identifies the last-copy report as critical because it helps prevent deletion of the only copy in the consortium\.
- Originating candidates: CAND-9753eb313538f11c366970b91f785c1f3dcb05cf80c7c2e7501e2e23685a412b

The system shall provide a last-copy report identifying a library system's last copies and shall provide both per-library and system-wide views\.

Sources and evidence:

Source: [conversations/conv\_pines021\_item\_purging\.eml](<../data/corpus/conversations/conv_pines021_item_purging.eml>); document ID: DOC-74ccbb6ac77183c0d1b34b1e79ed8fcbbfb4e7525cb33798c3af832fed733ad8; normalized lines 13–15.

> 3\. CRITICAL: We need a "last copy report" that identifies our library
>    system's last copies\. This helps catalogers update WorldCat entries
>    so we don't accidentally delete the only copy in the consortium\.

Source: [conversations/conv\_pines021\_item\_purging\.eml](<../data/corpus/conversations/conv_pines021_item_purging.eml>); document ID: DOC-74ccbb6ac77183c0d1b34b1e79ed8fcbbfb4e7525cb33798c3af832fed733ad8; normalized lines 35–37.

> For the last copy report - is this per library or per system? I think
> we need both views\. Sometimes we delete the last copy at our branch,
> sometimes the last copy in the entire PINES system\.

Source: [conversations/conv\_pines021\_item\_purging\.eml](<../data/corpus/conversations/conv_pines021_item_purging.eml>); document ID: DOC-74ccbb6ac77183c0d1b34b1e79ed8fcbbfb4e7525cb33798c3af832fed733ad8; normalized lines 107–109.

> This is all great\. One more thing - the "last copy report" should definitely
> be available per system, not just per library\. We need to make sure no one
> accidentally deletes the last copy at the consortium level\.

Source: [conversations/conv\_pines021\_item\_purging\.eml](<../data/corpus/conversations/conv_pines021_item_purging.eml>); document ID: DOC-74ccbb6ac77183c0d1b34b1e79ed8fcbbfb4e7525cb33798c3af832fed733ad8; normalized lines 131–132.

> - Provide a last copy report singling out a library system's last copies,
>   to assist catalogers who need to edit WorldCat entries

### REQ-318 — Role-Based Access Control for Staff Privileges

- Internal key: REQ-a0939a4781f15141395b2db72bbfd3ada0f5e5279f36b6fcdc769fabb4cdf11a
- Type: functional
- Priority: P1
- Priority basis: inferred
- Priority rationale: Access control supports system security and is critical under the priority scale\.
- Originating candidates: CAND-c091b48a8b02e8704a2b7c20041bad484598c24807fc1be08be52e99f4e376cb

The system shall control user rights and privileges through security groups and/or roles, supporting access control for individuals, workgroups, and arbitrary staff groups\.

Sources and evidence:

Source: [email\_staff\_login\.eml](<../data/corpus/email_staff_login.eml>); document ID: DOC-64b10e94c42508c5aea1af877ec9d2fe34485b099b29994b8b1a76cadc55e8b3; normalized lines 60–63.

> Adding to this - we need user rights and privileges to be controlled through
> security groups and/or "roles\." This would allow access control for individuals,
> workgroups, and arbitrary staff groups\.
> 

### REQ-319 — Annual Holds Placed Report

- Internal key: REQ-a2a9aec8b2692fd22012ceacd6189d18558e0b71b08f2754d60f363eab41f67d
- Type: functional
- Priority: P2
- Priority basis: inferred
- Priority rationale: This is a specific operational statistic requested for reporting\.
- Originating candidates: CAND-3ee99cd63b9925250a0ac535d498632ffd5437791657f7b1f79ea7109e4f8625

The system shall provide a report of the annual number of holds placed\.

Sources and evidence:

Source: [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>); document ID: DOC-091180de9b2d4ea83267d989411ac89f415d4def3bbf7cd51651fb7fda8d8bf9; normalized lines 570–570.

> - Annual \# of holds placed

### REQ-320 — Circulation Count by Shelving Location Report

- Internal key: REQ-a3c572278b7e31abc04e9bee9b9ca18cb8323813cf331d635985a15b21b48aab
- Type: functional
- Priority: P2
- Priority basis: inferred
- Priority rationale: The report is a specific requested circulation analysis capability, but the source does not assign an explicit priority\.
- Originating candidates: CAND-abf295f393ae9df51dd44f8201dacfacba1ae2a088885ce2c5e4848dedaf43b1

The system shall provide a circulation count report by shelving location\.

Sources and evidence:

Source: [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>); document ID: DOC-091180de9b2d4ea83267d989411ac89f415d4def3bbf7cd51651fb7fda8d8bf9; normalized lines 504–505.

> - Circulation Count by Circ Modifier
> - Circulation Count by Shelving Location

### REQ-321 — Circulation Count by Dewey Report

- Internal key: REQ-a3da459550d75b60d6a16322a829d9a85c7efbfa7548a1f90ebca0dcd66e2962
- Type: functional
- Priority: P3
- Priority basis: inferred
- Priority rationale: Inferred as useful collection-analysis reporting; no explicit source priority is supplied\.
- Originating candidates: CAND-76e30c9d0a1e875e80be4518fd391a3d1aef0c59e71a558008c0a9d5ad4121f8

The system shall provide a Circulation Count by Dewey report\.

Sources and evidence:

Source: [evergreen\_reference\_2009\.txt](<../data/corpus/evergreen_reference_2009.txt>); document ID: DOC-e6aa9f8c6308ab748459f87b578a0df9df9c865b7911bac3686e865963b7af6f; normalized lines 137–137.

> - Circulation Count by Dewey \(not available\)

### REQ-322 — Cross-Branch Capacity Aggregation

- Internal key: REQ-a40d1eaa1adb0459cfec99c490ebd0c3dfa4af30d9e45d4ded325f5f36d5160e
- Type: nonfunctional
- Priority: P3
- Priority basis: inferred
- Priority rationale: Useful management analysis, but not established as essential\.
- Originating candidates: CAND-d5ed7024da0ab982c0a88d261f5b52207d5c1b4de080ce148178e46966991d4d

The system shall aggregate capacity data across all branches using the centralized database\.

Sources and evidence:

Source: [conversations/conv\_pines015\_capacity\_interface\.eml](<../data/corpus/conversations/conv_pines015_capacity_interface.eml>); document ID: DOC-4acf2fdb375b86d49420e5743267e19b3f0af9ebe8bd764c1a88379aa9f5b662; normalized lines 46–48.

> From a technical standpoint, this is doable\. The data is centralized in
> our database, so we can build queries that aggregate across all branches\.
> 

### REQ-323 — Event-Based Item Reversion on Non-Time-Based Criteria

- Internal key: REQ-a420ca09e1918b6c76cd11134754200494c9ac8d60581632cd72c6b1b166dab1
- Type: functional
- Priority: P2
- Priority basis: inferred
- Priority rationale: Inferred as important transfer functionality; no explicit source priority is supplied\.
- Originating candidates: CAND-66432579ce33b1655d319e2bb5370fb361673755135f2b0ba8fc575a81747760

The system shall automatically revert or otherwise handle transferred items when configured non-time-based criteria occur, including a change of item status to sold\.

Sources and evidence:

Source: [conversations/conv\_pines018\_item\_transfer\.eml](<../data/corpus/conversations/conv_pines018_item_transfer.eml>); document ID: DOC-a47eb1f11286ff9099687b72a901e4a6ed2455b431087c0742aa78583c5bd80a; normalized lines 35–36.

> Can we also revert "based on other criteria"? Like, if the item's status
> changes to "sold" at the book sale, automatically revert it?

Source: [conversations/conv\_pines018\_item\_transfer\.eml](<../data/corpus/conversations/conv_pines018_item_transfer.eml>); document ID: DOC-a47eb1f11286ff9099687b72a901e4a6ed2455b431087c0742aa78583c5bd80a; normalized lines 59–60.

> 5\. Auto-revert mechanism - a scheduled task that checks transferred items
>    and reverts them based on time or status criteria\.

### REQ-324 — Edit and Run On-Demand Criteria Reports

- Internal key: REQ-a46a4e6b208a43c6201b22de73aeee5cd384639afdce9333481e5673f95e9a34
- Type: functional
- Priority: P2
- Priority basis: inferred
- Priority rationale: Inferred as high priority because the evidence requires editable, on-demand reports for maintenance and collections-development uses\.
- Originating candidates: CAND-7f42590c9c8fd44883d12c427caada8ce5f09cf9eaa8e3e32f67baf0071efaae

The system shall support reports with pre-selected criteria that can be edited and run on demand for maintenance reports or collections development\.

Sources and evidence:

Source: [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>); document ID: DOC-091180de9b2d4ea83267d989411ac89f415d4def3bbf7cd51651fb7fda8d8bf9; normalized lines 611–613.

> 15\.3 On Demand Reports
> On Demand Reports would be for pre-selected criteria but for things like
> maintenance reports or collections development and would be set to run on demand\.

### REQ-325 — Historical Reporting by Past Date Even After Shelving Changes

- Internal key: REQ-a48922cf4522fc9f2316b57f0815863c27af6b5b89983b902fa10c1aeea7431c
- Type: functional
- Priority: P2
- Priority basis: inferred
- Priority rationale: Historical state reporting supports operational analysis and accountability, but no explicit priority is supplied\.
- Originating candidates: CAND-ad9a5c256eff099f5bb0fdbd5acddcd86b88396e097b400461f3d556c4becbd1

The system shall provide historical reporting that shows what the data looked like on a specific past date, even if the shelving location has since changed\.

Sources and evidence:

Source: [survey\_results\_2009\.txt](<../data/corpus/survey_results_2009.txt>); document ID: DOC-aac7bceef7a883652805583e98ec513b6ae2e7951e2ecfa18722127b1f12a5c4; normalized lines 95–96.

>   - "Historical reporting - I want to see what the data looked like on a
>     specific date in the past, even if the shelving location has changed"

### REQ-326 — Prevent Excessive Duplicate Rows in Excel Exports

- Internal key: REQ-a5ea3b71c1fba37231c3b844008a58f35e0bcdaa31cbac7c459d9c7eab0ae620
- Type: functional
- Priority: P2
- Priority basis: inferred
- Priority rationale: The requirement addresses reported export data-quality problems that affect usability, although the source does not define the threshold for excessive duplication or assign a priority\.
- Originating candidates: CAND-ae275e9acb8701c1a5e815d2eb5d47272661d31ed137b8f603c0b356fad76cdf

The system shall ensure that exported Excel data does not contain excessive duplicate rows\.

Sources and evidence:

Source: [survey\_results\_2009\.txt](<../data/corpus/survey_results_2009.txt>); document ID: DOC-aac7bceef7a883652805583e98ec513b6ae2e7951e2ecfa18722127b1f12a5c4; normalized lines 73–73.

>   - "I need to export to Excel but the data has too many duplicate rows"

### REQ-327 — Defined Report Criteria Selection

- Internal key: REQ-a66ea459d93e9e8eced27d07b449db5f20246b2e91fec4e36b6740dc210113d4
- Type: nonfunctional
- Priority: P2
- Priority basis: inferred
- Priority rationale: Clear criteria are important for report interpretability and trustworthy results\.
- Originating candidates: CAND-a6d80f950131aa716a2cd14dcdd4c514d461de244d3e582280dfeb8bb5106f88

The system shall clearly define the selection criteria for reports\.

Sources and evidence:

Source: [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>); document ID: DOC-091180de9b2d4ea83267d989411ac89f415d4def3bbf7cd51651fb7fda8d8bf9; normalized lines 658–658.

> - Selection criteria is clearly defined

### REQ-328 — Report Delivery Address Book

- Internal key: REQ-a6970cad392e9fff0c23ce83719f7ca4ae431f5885cd72a75fa8c3ad4f2a9e7f
- Type: functional
- Priority: P3
- Priority basis: inferred
- Priority rationale: The evidence identifies the capability but does not establish it as critical\.
- Originating candidates: CAND-ce4e56e22d58b576bb17bf7430d70a3130b29a76322c122f5d8b99fcd8c69826

The system shall provide an address book for report delivery destinations\.

Sources and evidence:

Source: [evergreen\_reference\_2009\.txt](<../data/corpus/evergreen_reference_2009.txt>); document ID: DOC-e6aa9f8c6308ab748459f87b578a0df9df9c865b7911bac3686e865963b7af6f; normalized lines 174–174.

> - No address book for report delivery

### REQ-329 — Missing and Damaged Item Reports by Branch

- Internal key: REQ-a69f5fc255e3d252b61bdef16f7663e97ad5528674095cde7175afdb578eee49
- Type: functional
- Priority: P3
- Priority basis: inferred
- Priority rationale: Branch-level missing and damaged reports support collection operations but are not shown to be essential to basic operation\.
- Originating candidates: CAND-4ba8842b2402edd9ed4ecc2556dd7e5f6b55243a506cbef63e99b6b8a1217984

The system shall provide missing and damaged item reports on a per-branch basis\.

Sources and evidence:

Source: [meeting\_minutes/meeting\_2009-07-20\_minutes\.txt](<../data/corpus/meeting_minutes/meeting_2009-07-20_minutes.txt>); document ID: DOC-5ab1dd8bc97af3b1ab2e378495f0e0d75fd501fcc19f923c0d8fda831074281b; normalized lines 48–48.

>   - Missing/damaged item reports are needed per branch

### REQ-330 — Configure Report Age Ranges Per Report

- Internal key: REQ-a6b71cbb1d302592ff479c6bf037bb43d558a686c0ae16aa4de0d17a7cff542b
- Type: functional
- Priority: P2
- Priority basis: inferred
- Priority rationale: Configurable age ranges support demographic reporting across varying report needs, but the source does not assign an explicit priority\.
- Originating candidates: CAND-b5f21738c7a985c7da8d784217590291f79bc66d23a5bc94bd32539e86931d8e

The system shall allow age ranges to be configurable per report\.

Sources and evidence:

Source: [conversations/conv\_pines023\_patron\_characteristics\.eml](<../data/corpus/conversations/conv_pines023_patron_characteristics.eml>); document ID: DOC-d2b26a6e7678ca4e82bfa7bb06566f329dea692ea22e8987b516fa8bc98c544b; normalized lines 43–44.

> The age ranges need to be configurable too\. Like, 0-5, 6-10, 11-15, etc\.
> Or 0-6, 7-12, 13-17, 18-24, 25-34\.\.\. Whatever makes sense for the report\.

Source: [conversations/conv\_pines023\_patron\_characteristics\.eml](<../data/corpus/conversations/conv_pines023_patron_characteristics.eml>); document ID: DOC-d2b26a6e7678ca4e82bfa7bb06566f329dea692ea22e8987b516fa8bc98c544b; normalized lines 122–122.

> - Age ranges should be configurable per report

### REQ-331 — Item Purge Identification

- Internal key: REQ-a7bfa6f58351cd5eedfb27e9c7ae4dde13b26bcdc7fa7328244a01ef7406a9fa
- Type: functional
- Priority: P2
- Priority basis: inferred
- Priority rationale: The source identifies purge identification as a required operational capability and provides example criteria, but no P-level priority\.
- Originating candidates: CAND-2f79953a96cb13e7fbbbbce06eaee523589620b12b6d59e802f99dc5c564a65a

The system shall provide a utility and reports for identifying item records to purge according to customizable criteria, including an item being in missing status for more than configurable X months or having discard/weed status\.

Sources and evidence:

Source: [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>); document ID: DOC-091180de9b2d4ea83267d989411ac89f415d4def3bbf7cd51651fb7fda8d8bf9; normalized lines 376–381.

> 10\.8 Item Record Purging
> The system should provide a utility and reports for identifying item records
> to purge, based on customizable criteria such as:
>   - An item has been in status "missing" for more than X months
>   - An item has status "discard/weed"
> 

### REQ-332 — Transfer Delay and Problem Alerts

- Internal key: REQ-a7d3944ec28bbf71a050e3802a91aeeeee5702e7fea2557b60f39d6a087f26e8
- Type: functional
- Priority: P2
- Priority basis: inferred
- Priority rationale: Transfer alerts support timely operational intervention, but no explicit priority is supplied\.
- Originating candidates: CAND-602f67ebb6be5e2e20c6ce0b264ca4a6e60301368c5362ac3f75c7603ccdc22e

The system shall provide alerts or notifications for delayed or problematic item transfers between library locations\.

Sources and evidence:

Source: [conversations/conv\_pines018\_item\_transfer\.eml](<../data/corpus/conversations/conv_pines018_item_transfer.eml>); document ID: DOC-a47eb1f11286ff9099687b72a901e4a6ed2455b431087c0742aa78583c5bd80a; normalized lines 117–118.

> And can we set up alerts? If an item transfer is delayed or has issues,
> notify me\.

### REQ-333 — Hold Counts by Placement Method

- Internal key: REQ-a87e8fe76a954e6206b6914182ccbf509f98dc4c002e5b35d197e9495e54fa12
- Type: functional
- Priority: P2
- Priority basis: inferred
- Priority rationale: Supports analysis of service use and operational demand\.
- Originating candidates: CAND-d7e90cfc3e7cf14f18a5b6abd55d535fad5dfe7edea53b916745d20bc82e8b3a

The system shall count holds and indicate the placement method as staff desk, public computer, or remote\.

Sources and evidence:

Source: [survey\_results\_2009\.txt](<../data/corpus/survey_results_2009.txt>); document ID: DOC-aac7bceef7a883652805583e98ec513b6ae2e7951e2ecfa18722127b1f12a5c4; normalized lines 121–122.

> 5\. Holds counted with method of placement: at staff desk, public computer,
>    or remotely\.

### REQ-334 — OPAC Functionality Must Not Be Constrained by Management Processes

- Internal key: REQ-a8852f951fadacede135ecbf61945a89b15145d04e092194f44aea737705749f
- Type: nonfunctional
- Priority: P1
- Priority basis: inferred
- Priority rationale: Inferred as critical because preserving OPAC functionality is essential to public access\.
- Originating candidates: CAND-800d56b22ec0b0bf78deefc4bb3d32ed789abc16f7ba9d2bc35e383760d12c11

The Management Processes requirements shall not constrain or interfere with the functionality or features of the Online Public Access Catalog \(OPAC\) module\.

Sources and evidence:

Source: [meeting\_minutes/meeting\_2009-07-20\_minutes\.txt](<../data/corpus/meeting_minutes/meeting_2009-07-20_minutes.txt>); document ID: DOC-5ab1dd8bc97af3b1ab2e378495f0e0d75fd501fcc19f923c0d8fda831074281b; normalized lines 126–130.

> CO-5: These requirements shall not constrain functionality or features of the
>       Online Public Access Catalog \(OPAC\) module\.
>       \[Discussion: The management processes are separate from the public-
>       facing catalog\. Changes to management reporting should not affect
>       patron access\.\]

### REQ-335 — Flag Last-Copy Items by Specified Scope

- Internal key: REQ-a8b07d5110c25ca4fd5f2802911d36e77e2d07c40e090f0636878b0288d42624
- Type: functional
- Priority: P1
- Priority basis: inferred
- Priority rationale: Inferred as critical because the evidence requires identifying items that may be the last copy within a selected library or system scope\.
- Originating candidates: CAND-85b248a3e52b310f531ac1901f26940c4fe781d0562ee089d2e7d02a8fddf7cc

For each item record, the system shall check whether the item is the only copy within the specified scope, either a library or the entire system, and shall flag it in the last-copy report\.

Sources and evidence:

Source: [conversations/conv\_pines021\_item\_purging\.eml](<../data/corpus/conversations/conv_pines021_item_purging.eml>); document ID: DOC-74ccbb6ac77183c0d1b34b1e79ed8fcbbfb4e7525cb33798c3af832fed733ad8; normalized lines 35–37.

> For the last copy report - is this per library or per system? I think
> we need both views\. Sometimes we delete the last copy at our branch,
> sometimes the last copy in the entire PINES system\.

Source: [conversations/conv\_pines021\_item\_purging\.eml](<../data/corpus/conversations/conv_pines021_item_purging.eml>); document ID: DOC-74ccbb6ac77183c0d1b34b1e79ed8fcbbfb4e7525cb33798c3af832fed733ad8; normalized lines 74–76.

> For the last copy report, the system would check: for each item record,
> is this the only copy in the specified scope \(library or system\)? If yes,
> flag it\.

### REQ-336 — Items In Transit by Sending Library Report

- Internal key: REQ-a9c1fe56eb21a58649812d9fa0c4d2e024f35375b70cafecb70daac4b69b3d24
- Type: functional
- Priority: P3
- Priority basis: inferred
- Priority rationale: The source requests this operational report but does not establish it as essential to basic operation\.
- Originating candidates: CAND-be22ff819c69459c7e3a0d374d369bfdb953b4aa23d80952ab42a23810a41573

The system shall provide an Items In Transit by Sending Library report\.

Sources and evidence:

Source: [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>); document ID: DOC-091180de9b2d4ea83267d989411ac89f415d4def3bbf7cd51651fb7fda8d8bf9; normalized lines 579–579.

> - Items In Transit by Sending Library

### REQ-337 — Support Boolean AND and OR in Report Queries

- Internal key: REQ-a9e0da65c8b5d1610ec1f08f178585b5cc8973875a6a8d88c69a856c79dd424a
- Type: functional
- Priority: P2
- Priority basis: inferred
- Priority rationale: Boolean operators materially improve report expressiveness, but no explicit priority is supplied\.
- Originating candidates: CAND-4fb7a4be2983fec72fc8f401274ce684bc93002ee58fb6ab10f0ba74c2e9964c

The system shall provide Boolean AND and OR operators in report queries in addition to simple filters\.

Sources and evidence:

Source: [evergreen\_reference\_2009\.txt](<../data/corpus/evergreen_reference_2009.txt>); document ID: DOC-e6aa9f8c6308ab748459f87b578a0df9df9c865b7911bac3686e865963b7af6f; normalized lines 39–39.

> - No Boolean operators \(AND/OR\) beyond simple filters

### REQ-338 — Pre-defined Executive Reports for Board Reporting

- Internal key: REQ-abca8b3fc46f890b197fbc849ca15f2fef7b1e43dd54251818127eeee6bf23f5
- Type: functional
- Priority: P2
- Priority basis: inferred
- Priority rationale: Pre-defined Board and executive reporting is important functionality with substantial reporting impact, but the supplied evidence does not establish that it is essential for core operation or mandatory compliance\.
- Originating candidates: CAND-fed7ae4fce588f342fd72ea30bdd289dbe6945e3ef9dbbde7eeef75c735f9a39

The system shall provide pre-defined reports for Board and executive reporting\.

Sources and evidence:

Source: [meeting\_minutes/meeting\_2009-07-20\_minutes\.txt](<../data/corpus/meeting_minutes/meeting_2009-07-20_minutes.txt>); document ID: DOC-5ab1dd8bc97af3b1ab2e378495f0e0d75fd501fcc19f923c0d8fda831074281b; normalized lines 42–42.

>   - Board/executive reports need to be pre-defined

### REQ-339 — Export Capacity Data to CSV

- Internal key: REQ-ac10eab4f27dc09e759b285bc5d2f42f124eb2333c861406552a9263f795c311
- Type: functional
- Priority: P3
- Priority basis: inferred
- Priority rationale: This is a useful reporting convenience and is not identified as essential to core operation\.
- Originating candidates: CAND-9683aedbb525c3a513746d370af45bd0a4f91c5e101e60ec466304e307d462c5

The system shall export capacity data to CSV for use in spreadsheets\.

Sources and evidence:

Source: [conversations/conv\_pines015\_capacity\_interface\.eml](<../data/corpus/conversations/conv_pines015_capacity_interface.eml>); document ID: DOC-4acf2fdb375b86d49420e5743267e19b3f0af9ebe8bd764c1a88379aa9f5b662; normalized lines 68–69.

> current load\.\.\. And export to CSV for the directors who want spreadsheets\.
> 

Source: [conversations/conv\_pines015\_capacity\_interface\.eml](<../data/corpus/conversations/conv_pines015_capacity_interface.eml>); document ID: DOC-4acf2fdb375b86d49420e5743267e19b3f0af9ebe8bd764c1a88379aa9f5b662; normalized lines 88–89.

> - Trend data \(growth/shrink patterns\)
> - Export to CSV

### REQ-340 — Patron Count by Age Demographic

- Internal key: REQ-ac7888ed04614e37914c1510256f4e83ebe9593cf8e7602d10ef3946dd2c76e3
- Type: functional
- Priority: P3
- Priority basis: inferred
- Priority rationale: This is a useful demographic report but is not identified as essential for basic operation\.
- Originating candidates: CAND-0bcb2f73ef5fe367b5456085c4ddde37ee7fa97c668e116f6cc55185ff281fe0

The system shall provide a report presenting patron count grouped by age range\.

Sources and evidence:

Source: [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>); document ID: DOC-091180de9b2d4ea83267d989411ac89f415d4def3bbf7cd51651fb7fda8d8bf9; normalized lines 546–546.

> - Patron Count by Age Demographic

### REQ-341 — Assistive Technology Accessibility Support

- Internal key: REQ-ad09182361450643289287a1e11fc87e208ea4307205e1e406997dcab4b8daea
- Type: nonfunctional
- Priority: P1
- Priority basis: inferred
- Priority rationale: Accessibility is a mandatory system quality and is essential for equitable access\.
- Originating candidates: CAND-9fe2d71f0e6f1d6abbaefd186b12757a25042d052b624ad566921b83c366ee2d

The system shall be accessible with screen-reading software, screen-magnification software, and other assistive technology programs designed to increase accessibility\.

Sources and evidence:

Source: [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>); document ID: DOC-091180de9b2d4ea83267d989411ac89f415d4def3bbf7cd51651fb7fda8d8bf9; normalized lines 144–146.

> OE-5: The system must be accessible with screen-reading software, screen-
>       magnification software, and other assistive technology programs designed
>       to increase accessibility\.

### REQ-342 — Save Queries for Repeated Use Including Recurring Runs

- Internal key: REQ-ad6c3a1b1223a8a9bd142d0defc24a1a4501af501e069422f6d15f0090fe495d
- Type: functional
- Priority: P3
- Priority basis: inferred
- Priority rationale: Inferred as medium priority because saving queries supports repeated reporting work but is not identified as essential to basic operation\.
- Originating candidates: CAND-796309b89945d06faaf2cfa9eedc1069d771880aeb7443058d2e4ab3f6b41cd9

The system shall allow queries to be saved for repeated use, including recurring uses such as monthly runs\.

Sources and evidence:

Source: [interview\_cataloging\_2009-05-08\.txt](<../data/corpus/interview_cataloging_2009-05-08.txt>); document ID: DOC-a79fab45108210e6bce7d92153dfcf055f2ef6b2cdab49a3f6f5717a3e35f29f; normalized lines 49–50.

> save these queries for repeated use - we do this monthly\. Third, we need to
> manually select titles from query results if we want to be more targeted\.

### REQ-343 — Threshold Balance Queries

- Internal key: REQ-ae32d7f02c17e0f882540ab000301ce472b37856a6d7d994b45c6240a804508c
- Type: functional
- Priority: P2
- Priority basis: inferred
- Priority rationale: This supports operational identification of accounts requiring attention and has substantial staff impact; no explicit source priority is provided\.
- Originating candidates: CAND-ee2df40e218ee6ce2f69e5c374f7ddf26465f664207b705c5f4d905f6be5cf2a

The system shall allow staff to query patron accounts with balances greater than a specified dollar threshold\.

Sources and evidence:

Source: [email\_financial\_reports\.eml](<../data/corpus/email_financial_reports.eml>); document ID: DOC-8b6cfb3cf368b794d82567933f9c85062740814819b1e28b4837f6021cbcbee6; normalized lines 67–69.

> - For fines and charges, the staff should be able to query patron accounts
>   with balances greater than X dollars\. This is useful for identifying accounts
>   that need attention\.

Source: [email\_financial\_reports\.eml](<../data/corpus/email_financial_reports.eml>); document ID: DOC-8b6cfb3cf368b794d82567933f9c85062740814819b1e28b4837f6021cbcbee6; normalized lines 86–88.

> - We need to easily query patron accounts with balances greater than X dollars\.
>   Right now it takes forever to find these accounts manually\.
> 

### REQ-344 — Collection use analysis tools

- Internal key: REQ-ae64f14e017ccb885104ea8e6761064f76fa2852ebeec1746fb06109a1c3656b
- Type: functional
- Priority: P2
- Priority basis: inferred
- Priority rationale: Collection and patron-use analysis supports important management decisions; the source does not establish a more specific priority\.
- Originating candidates: CAND-8c6a5631b7ac10b221ae1c014e3e5b176b1e8f687e5c75a7f4415f8295b6d204

The Management Processes shall provide tools to analyze the library collection and its use by patrons\.

Sources and evidence:

Source: [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>); document ID: DOC-091180de9b2d4ea83267d989411ac89f415d4def3bbf7cd51651fb7fda8d8bf9; normalized lines 86–86.

>   - Analyzing the Library collection and its use by patrons\.

### REQ-345 — Hold request origin tracking

- Internal key: REQ-af341348a59519bb122bb99bc94d6fbbcc095dadc7a43036d46e250ba3ce63fd
- Type: functional
- Priority: P2
- Priority basis: inferred
- Priority rationale: Hold counts and placement origin support important operational analysis; the source does not establish a more specific priority\.
- Originating candidates: CAND-8bde7e66d6d9fc1eea4a4ae3ddd889eb37975d961dfee15212833c7591e1545c

The system shall count all hold requests and record whether each hold was placed at a staff desk, at a public computer inside the library, or remotely\.

Sources and evidence:

Source: [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>); document ID: DOC-091180de9b2d4ea83267d989411ac89f415d4def3bbf7cd51651fb7fda8d8bf9; normalized lines 440–445.

> 12\.5 Holds and Locations
> The system counts all hold requests, including how the hold was placed:
>   - at a staff desk
>   - at a public computer inside the library
>   - remotely
> 

### REQ-346 — Patron Count by County, City, and Zip Code

- Internal key: REQ-af4d86fd077e78af1b0bc2f09218ac63b117de3bb73a9ccf71951d3e9010aeee
- Type: functional
- Priority: P2
- Priority basis: inferred
- Priority rationale: Inferred as high priority because the evidence explicitly enumerates this report\.
- Originating candidates: CAND-7f792351645a4e8833f72681e892d38ef94208a7489f22c574c17425d73823f2

The system shall provide a Patron Count by County, City, and Zip Code report\.

Sources and evidence:

Source: [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>); document ID: DOC-091180de9b2d4ea83267d989411ac89f415d4def3bbf7cd51651fb7fda8d8bf9; normalized lines 548–548.

> - Patron Count by County, City, and Zip Code

### REQ-347 — IntraPINES Loans for All Facilities

- Internal key: REQ-afca43f28caaee09141a99a7c4b58160ebcd6f48552525a2809060f6ada50b40
- Type: functional
- Priority: P2
- Priority basis: inferred
- Priority rationale: Reports covering all facilities support important system-wide operational reporting\.
- Originating candidates: CAND-11d9417c85f393fb70bf73137ff3d2cfc673b87e0ccc22df2071c639f9016d9d

The system shall provide IntraPINES Loans reports covering all facilities\.

Sources and evidence:

Source: [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>); document ID: DOC-091180de9b2d4ea83267d989411ac89f415d4def3bbf7cd51651fb7fda8d8bf9; normalized lines 566–566.

> - IntraPINES Loans for all Facilities

### REQ-348 — MARC Field Reporting Without Row Spreading

- Internal key: REQ-afd32b7d2ad8dd28a557b8cfb8b5ead5b57aa3ce024078afa320effe9f3e32a6
- Type: functional
- Priority: P2
- Priority basis: inferred
- Priority rationale: The capability addresses a stated reporting usability need, but the source does not assign a formal priority level\.
- Originating candidates: CAND-114e2eeface91605a4b66c8814c1fef72a24a8a2ffbb97aece7e5bfdc6fc8012

The system shall allow users to retrieve specific MARC fields and present each requested field without spreading it across multiple rows\.

Sources and evidence:

Source: [survey\_results\_2009\.txt](<../data/corpus/survey_results_2009.txt>); document ID: DOC-aac7bceef7a883652805583e98ec513b6ae2e7951e2ecfa18722127b1f12a5c4; normalized lines 75–75.

>   - "Need to pull specific MARC fields but they're spread across multiple rows"

### REQ-349 — Allow Users to Save Queries

- Internal key: REQ-afeecc228381066d15e3eb43f6868b883ad2c4bf2d5b7ca99d916193dd808bf2
- Type: functional
- Priority: P3
- Priority basis: inferred
- Priority rationale: Saved queries improve convenience and efficiency but are not essential to basic reporting; no explicit source priority is provided\.
- Originating candidates: CAND-f9d16451de6c45d7e5f0db5ddb40baad236ed434e076bb0e4806555b7cc159de

The system shall allow users to save queries for repeated use\.

Sources and evidence:

Source: [survey\_results\_2009\.txt](<../data/corpus/survey_results_2009.txt>); document ID: DOC-aac7bceef7a883652805583e98ec513b6ae2e7951e2ecfa18722127b1f12a5c4; normalized lines 87–87.

>   - Save queries for repeated use: 58%

### REQ-350 — Hover Pop-Up Descriptions for Canned Reports

- Internal key: REQ-b00a32939a08725b82df7d62298a3af285e2d4ea29d9142f04fbaf2fdd9aa427
- Type: functional
- Priority: P4
- Priority basis: inferred
- Priority rationale: The source describes a convenience feature and does not establish it as important to core operation\.
- Originating candidates: CAND-c07b36a66760097dd28fdfdeddbc8d945e9eaa117a0e6c2341359f690d9a1787

The system shall provide quick access to the description of each canned report or template through a pop-up box displayed when the user hovers over its title\.

Sources and evidence:

Source: [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>); document ID: DOC-091180de9b2d4ea83267d989411ac89f415d4def3bbf7cd51651fb7fda8d8bf9; normalized lines 620–622.

> 15\.5 Quick Access Interface
> - Ability to hover over each title of canned report/template with pop-up box
>   with description

### REQ-351 — OPAC Interface for Management Processes

- Internal key: REQ-b0a5e6dfed37fa79b7bc78414f1a54585b709c114477c95df571819ce96fa2ae
- Type: nonfunctional
- Priority: P2
- Priority basis: inferred
- Priority rationale: OPAC interaction is an explicit Management Processes dependency; no explicit source priority is supplied\.
- Originating candidates: CAND-f70f44e72dc93569af2c299e88a59a23a3dac1696fe0d722bd005dbc70436d08

Management Processes shall interact with the patron interface, also known as the Online Public Access Catalog \(OPAC\)\.

Sources and evidence:

Source: [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>); document ID: DOC-091180de9b2d4ea83267d989411ac89f415d4def3bbf7cd51651fb7fda8d8bf9; normalized lines 215–216.

> DE-3: Management Processes interact with a patron interface, also known as an
>       Online Public Access Catalog \(OPAC\)\.

### REQ-352 — Batch Status Conversion Assistance Report

- Internal key: REQ-b0ae4fb264b052e1ae7956d4bea1854eee4fccd2a49b08a56e3a736340e19fbd
- Type: functional
- Priority: P2
- Priority basis: inferred
- Priority rationale: Inferred as high priority because the evidence identifies this report as an operational capability for batch status conversion\.
- Originating candidates: CAND-79ce1c2996009aed76fd9815eafed8df91d85a511073cf47bd0a5ff4e77d036e

The system shall provide a report to assist with batch conversion of statuses\.

Sources and evidence:

Source: [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>); document ID: DOC-091180de9b2d4ea83267d989411ac89f415d4def3bbf7cd51651fb7fda8d8bf9; normalized lines 634–634.

> - The system provides a report to assist in the batch conversion of statuses

### REQ-353 — Multiple Report Output Formats

- Internal key: REQ-b0d60abaae7398ad32b123e1a9b2889e84ec2c8332fe4bcb56c0cfc75258f3c4
- Type: functional
- Priority: P2
- Priority basis: inferred
- Priority rationale: Multiple output formats support practical report use and are explicitly identified in the source, which does not assign a P-level priority\.
- Originating candidates: CAND-3f8acaf3f9e550a313971437559d2b40c11e6d8ce41ba7b35db5952c5f0010d8

Reports shall support output in Excel, CSV, and HTML formats\.

Sources and evidence:

Source: [survey\_results\_2009\.txt](<../data/corpus/survey_results_2009.txt>); document ID: DOC-aac7bceef7a883652805583e98ec513b6ae2e7951e2ecfa18722127b1f12a5c4; normalized lines 64–64.

>   - Multiple output formats \(Excel, CSV, HTML\): 61%

### REQ-354 — Collection Value Report by Call Number

- Internal key: REQ-b10023f80640b3b5643b1f8efcd43db35d40e40c225c8410ae6b2c5b24fe4382
- Type: functional
- Priority: P3
- Priority basis: inferred
- Priority rationale: This is a useful collection-analysis report but is not identified as essential to basic operation\.
- Originating candidates: CAND-5d69492cb020d5badc1d0492b8300a1c6ec7178260576abd148b787a9d8768cd

The system shall provide reports of the price value of the collection by call number\.

Sources and evidence:

Source: [evergreen\_reference\_2009\.txt](<../data/corpus/evergreen_reference_2009.txt>); document ID: DOC-e6aa9f8c6308ab748459f87b578a0df9df9c865b7911bac3686e865963b7af6f; normalized lines 150–150.

> - Price value of collection by call number \(not available\)

### REQ-355 — Support Report Template Management

- Internal key: REQ-b17846e8aa9640e29bff60834df4af0793761e57020867832a8628402509f783
- Type: functional
- Priority: P2
- Priority basis: inferred
- Priority rationale: Template management supports staff and administrator report configuration, but the source does not assign an explicit priority\.
- Originating candidates: CAND-b2df79f1f799c3170d02a5434f7185ce7ec6cd9638a6fb80f5fc763d5c1e546a

The system shall provide a report template management system\.

Sources and evidence:

Source: [evergreen\_reference\_2009\.txt](<../data/corpus/evergreen_reference_2009.txt>); document ID: DOC-e6aa9f8c6308ab748459f87b578a0df9df9c865b7911bac3686e865963b7af6f; normalized lines 184–184.

> - No report template management system

### REQ-356 — Items by Creation Date Range Report

- Internal key: REQ-b1acc564dd39d20ad26851a72484f666fa67ef00cf52463df15499c3febfa292
- Type: functional
- Priority: P3
- Priority basis: inferred
- Priority rationale: Inferred as useful specific reporting functionality; no explicit source priority is supplied\.
- Originating candidates: CAND-6749805eefe2dec31d7436c9b391995ed74634fef104179e3958d7067ee2de82

The system shall provide a report listing items within a specified creation-date range\.

Sources and evidence:

Source: [evergreen\_reference\_2009\.txt](<../data/corpus/evergreen_reference_2009.txt>); document ID: DOC-e6aa9f8c6308ab748459f87b578a0df9df9c865b7911bac3686e865963b7af6f; normalized lines 146–146.

> - List of Items by Creation Date Range \(not available\)

### REQ-357 — Manual selection from query results

- Internal key: REQ-b2995f84e38e2b92fa0d37c901b064f30fc9439c1d83c32b8b24e6473cedc3f5
- Type: functional
- Priority: P3
- Priority basis: inferred
- Priority rationale: Manual selection is a useful administrative capability but is not identified as essential to basic operation\.
- Originating candidates: CAND-8d99926ff7571a9550c86da97a707194c02656248b258fdf13e070f6ebc9eec9

The system shall allow authorized users to manually select records from query results\.

Sources and evidence:

Source: [survey\_results\_2009\.txt](<../data/corpus/survey_results_2009.txt>); document ID: DOC-aac7bceef7a883652805583e98ec513b6ae2e7951e2ecfa18722127b1f12a5c4; normalized lines 88–88.

>   - Manually select from query results: 39%

### REQ-358 — Cross-Tabulated Board and Activity Reports

- Internal key: REQ-b39df83f47073c709add8d25e258fbd7db3ba1aff3466bee050d6cdde498c567
- Type: functional
- Priority: P2
- Priority basis: inferred
- Priority rationale: Cross-tabulated activity reporting supports operational and board analysis and is explicitly described in the sources; the source does not assign a priority\.
- Originating candidates: CAND-dd84aec4ea69298917dae1455e70a8b51cd46976d6b0e09c2dd758593c4e3a70

The system shall support cross-tabulation of board and activity reports by terminal, branch, system, hour, age range, patron type, and patron location\.

Sources and evidence:

Source: [email\_report\_features\.eml](<../data/corpus/email_report_features.eml>); document ID: DOC-d9e168e0c03903021bf9e636e1d8e5f56dfcb79cc110d3839e38175a7c54344e; normalized lines 27–29.

>    volume of use - checkouts, check-ins, holds placed, holds filled\. Cross-
>    tabulated per terminal, per branch, per system, per hour, per age range,
>    per patron type, per patron location\.

Source: [email\_report\_features\.eml](<../data/corpus/email_report_features.eml>); document ID: DOC-d9e168e0c03903021bf9e636e1d8e5f56dfcb79cc110d3839e38175a7c54344e; normalized lines 110–111.

> 4\. BOARD REPORTS: Pre-defined reports for boards\. Cross-tabulated per
>    terminal/branch/system/hour/age/patron type/location\.

### REQ-359 — Candidate Selection Query Builder

- Internal key: REQ-b3aac13b23d77b7e6051d02c63e4db409611bf798ac601692873f240a109ea8b
- Type: functional
- Priority: P2
- Priority basis: inferred
- Priority rationale: Candidate selection is an important query capability, while the source permits reuse of an existing tool\.
- Originating candidates: CAND-18f92cc633ca4280eb067974d6777d4723e2a816dfb0490d86777eb6ffd95117

The system shall provide a query builder for candidate selection; the existing report query tool may be reused\.

Sources and evidence:

Source: [conversations/conv\_pines018\_item\_transfer\.eml](<../data/corpus/conversations/conv_pines018_item_transfer.eml>); document ID: DOC-a47eb1f11286ff9099687b72a901e4a6ed2455b431087c0742aa78583c5bd80a; normalized lines 49–50.

> 1\. Query builder for candidate selection - we can reuse the report query
>    tool for this\.

### REQ-360 — Quick Report Access with Title Hover Tooltips and Descriptions

- Internal key: REQ-b4e87e83411a5dea31f12805a443db52e7d3873ffcce3ed2e1150339494894e8
- Type: functional
- Priority: P3
- Priority basis: inferred
- Priority rationale: The interface improves discoverability and usability but is not identified as essential functionality\.
- Originating candidates: CAND-afca3180097b44cb79dacede455476a8c7f1712fd97b52e88e8d53adc32c8688

The system shall provide a quick-access interface for reports, including pop-up descriptions and hover tooltips for report titles\.

Sources and evidence:

Source: [evergreen\_reference\_2009\.txt](<../data/corpus/evergreen_reference_2009.txt>); document ID: DOC-e6aa9f8c6308ab748459f87b578a0df9df9c865b7911bac3686e865963b7af6f; normalized lines 178–179.

> - No quick access interface with pop-up descriptions
> - No hover tooltips for report titles

### REQ-361 — Report for Patrons with Invalid Home Libraries

- Internal key: REQ-b541c5e21367401e0e5fb76dbb63fba32fc4a6caf9bccd85614c1c5d6e09d2d9
- Type: functional
- Priority: P2
- Priority basis: inferred
- Priority rationale: The source enumerates this as an operational reporting need but does not assign an explicit priority\.
- Originating candidates: CAND-c174918e4ea8ea57394de28cc3d453279847ee6815eb8e7e504b9230531d8401

The system shall provide a report identifying patrons with an invalid home library\.

Sources and evidence:

Source: [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>); document ID: DOC-091180de9b2d4ea83267d989411ac89f415d4def3bbf7cd51651fb7fda8d8bf9; normalized lines 285–287.

>   - Missing items
>   - Bibliographic records with no item records
>   - Patrons with invalid home library

### REQ-362 — Core Report Types Including Custom or On-Demand Reports

- Internal key: REQ-b5532db78ede5824c50d8f6b701cb4109b322b216253e30bf898a61dee208fdf
- Type: functional
- Priority: P2
- Priority basis: inferred
- Priority rationale: These report categories represent the principal staff reporting scope, but no explicit priority is supplied\.
- Originating candidates: CAND-5267255ded67334c52e7cc4b18133bc68e9e1c1d75f67f89829b2afad7c58837

The system shall support circulation, item, patron, financial, hold, and custom or on-demand report types\.

Sources and evidence:

Source: [survey\_results\_2009\.txt](<../data/corpus/survey_results_2009.txt>); document ID: DOC-aac7bceef7a883652805583e98ec513b6ae2e7951e2ecfa18722127b1f12a5c4; normalized lines 22–29.

> QUESTION 2: "Which types of reports do you use most often? \(Select all that
>             apply\)"
>   - Circulation reports \(checkouts, check-ins, renewals\): 78%
>   - Item reports \(inventory, weeding, missing\): 65%
>   - Patron reports \(demographics, inactive accounts\): 52%
>   - Financial reports \(fines, payments\): 34%
>   - Hold reports \(placed, filled, stale\): 41%
>   - Custom/on-demand reports: 29%

### REQ-363 — Purge Operations Audit Trail

- Internal key: REQ-b5db3ca2db4d921edb169ca79ae7bc2e7a92ec90e866f8a9e7b1243248fcab92
- Type: nonfunctional
- Priority: P1
- Priority basis: inferred
- Priority rationale: The source identifies the audit trail as a safety measure supporting accountability and troubleshooting for purge operations\.
- Originating candidates: CAND-5c943301a02ad13f1854f93a28854a5138041110a9928032cf282b0b54fdc936

The system shall maintain an audit trail for all purge operations, recording who performed each purge and when\.

Sources and evidence:

Source: [conversations/conv\_pines021\_item\_purging\.eml](<../data/corpus/conversations/conv_pines021_item_purging.eml>); document ID: DOC-74ccbb6ac77183c0d1b34b1e79ed8fcbbfb4e7525cb33798c3af832fed733ad8; normalized lines 72–73.

> 3\. Audit trail for all purges
> 

Source: [conversations/conv\_pines021\_item\_purging\.eml](<../data/corpus/conversations/conv_pines021_item_purging.eml>); document ID: DOC-74ccbb6ac77183c0d1b34b1e79ed8fcbbfb4e7525cb33798c3af832fed733ad8; normalized lines 97–98.

> Also, for safety - YES on the audit trail\. We need to track who purged what
> and when\. This is for accountability and troubleshooting\.

Source: [conversations/conv\_pines021\_item\_purging\.eml](<../data/corpus/conversations/conv_pines021_item_purging.eml>); document ID: DOC-74ccbb6ac77183c0d1b34b1e79ed8fcbbfb4e7525cb33798c3af832fed733ad8; normalized lines 136–139.

> Safety measures:
> - Read-only reports for identifying candidates
> - Separate confirmation step for actual deletions
> - Audit trail for all purges

### REQ-364 — Anonymize Demographic Data to Remove Personally Identifiable Information

- Internal key: REQ-b63c4b011377afd50fa29a840314ecaa823a0e27b680067772f00c93b2b638e6
- Type: nonfunctional
- Priority: P1
- Priority basis: inferred
- Priority rationale: Protection of personally identifiable information is a critical privacy and security requirement\.
- Originating candidates: CAND-abb42577e6289b4e5fb64f696130dd64f78bc24546be96ede7e46378586c3efe

The system shall anonymize demographic data so that it contains no personally identifiable information\.

Sources and evidence:

Source: [survey\_results\_2009\.txt](<../data/corpus/survey_results_2009.txt>); document ID: DOC-aac7bceef7a883652805583e98ec513b6ae2e7951e2ecfa18722127b1f12a5c4; normalized lines 127–128.

> 7\. Demographic statistics include transactions by geographical regions and age
>    ranges\. Data must be anonymized\.

### REQ-365 — Three Reporting Interfaces

- Internal key: REQ-b65a935072e139b3418526b987074f2c02d0b7eefcf18b23a40268705df980cd
- Type: functional
- Priority: P2
- Priority basis: inferred
- Priority rationale: The three interfaces define the principal reporting modes and are important to the reporting system scope\.
- Originating candidates: CAND-20788446eb843450003516c57df8e1e72c9b4d3c086c0e70a31c8fa9338dbd7d

The reporting interface shall provide canned reports, noncanned or on-demand reports, and open template reporting; canned reports shall support ASAP or recurring execution; noncanned or on-demand reports shall allow editing of selection criteria and display options; and open template reporting shall allow selection from attributes associated with circulation, items, patrons, bills, and bibliographic records for filtering and display\.

Sources and evidence:

Source: [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>); document ID: DOC-091180de9b2d4ea83267d989411ac89f415d4def3bbf7cd51651fb7fda8d8bf9; normalized lines 595–603.

> 15\.1 Three Interfaces
> Three interfaces are needed:
>   a\) Canned reports - generic reports set to run by the individual either ASAP
>      or recurring
>   b\) Noncanned or On Demand Reports - preset but have the ability to edit
>      selection criteria and display options
>   c\) Open Template Reporting - all attributes associated with circulation,
>      items, patrons, bills, and bibs to select from for filtering and display
> 

### REQ-366 — Bibliographic Records with Holds Report

- Internal key: REQ-b6e16a43d1fdb11716fe9a42d6c7625c2be712ce84e03b17597fd1a0a482ff02
- Type: functional
- Priority: P2
- Priority basis: inferred
- Priority rationale: The report is explicitly listed among the periodic report examples; the source does not assign a priority\.
- Originating candidates: CAND-e77c7d63f80e4776ab2e964dbe538170728976e1c3589709731d887cfd4187a5

The system shall provide a report of bibliographic records with holds\.

Sources and evidence:

Source: [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>); document ID: DOC-091180de9b2d4ea83267d989411ac89f415d4def3bbf7cd51651fb7fda8d8bf9; normalized lines 275–279.

> 8\.7 Periodic Report Examples
> Examples of periodic reports include:
>   - Bibliographic records with holds
>   - Items that have not been checked out in X days
>   - Item-level holds

### REQ-367 — Vendor Integration

- Internal key: REQ-b74d4e8fd2c04d794ceea2095028af424d32a85eeea9c89921bd51eef238d3b9
- Type: functional
- Priority: P2
- Priority basis: inferred
- Priority rationale: Vendor integration supports acquisition and management processes, but the source does not assign a P-level priority\.
- Originating candidates: CAND-2d1cb052d090dce2083f4efedd5b94f5307b4b12e2a1b628c56eec9bb1995e2e

The system shall interface with vendor websites through published APIs and/or automated transfer of standard-format data files, including USMARC21 and EDIFACT when applicable\.

Sources and evidence:

Source: [meeting\_tech\_subcommittee\_2009-06-30\.txt](<../data/corpus/meeting_tech_subcommittee_2009-06-30.txt>); document ID: DOC-e081aa7bd57bf5e59c75a8a86f592124757b74dff1ee0df4badc10c025092d96; normalized lines 143–146.

> 4\.4 VENDOR INTEGRATION
> DE-2: Management Processes interface with a variety of vendor websites, via
> published APIs and/or automated transfer of standard-format data files
> \(e\.g\., USMARC21, EDIFACT\)\.

### REQ-368 — Support Complex Query Construction in Report Writer

- Internal key: REQ-b79c7e93b49bba321aa4077b9e5777464fb6254bbbe8f721141be67505d2000f
- Type: functional
- Priority: P2
- Priority basis: inferred
- Priority rationale: Complex query construction is important to the stated reporting purpose; no explicit source priority is provided\.
- Originating candidates: CAND-fccbce87e5e68cf0cf6f04365aa8a3e08d727590d17bbfd55970230d0012d139

The report writer shall support construction of complex queries\.

Sources and evidence:

Source: [evergreen\_reference\_2009\.txt](<../data/corpus/evergreen_reference_2009.txt>); document ID: DOC-e6aa9f8c6308ab748459f87b578a0df9df9c865b7911bac3686e865963b7af6f; normalized lines 37–37.

> Limitations:

### REQ-369 — Inactive Patron List Report

- Internal key: REQ-b7dfe7f29d3af0ea09356a370c0cad4196982b536fb02d92a483a41566444541
- Type: functional
- Priority: P2
- Priority basis: inferred
- Priority rationale: The list supports patron-account administration, but the source does not assign an explicit priority\.
- Originating candidates: CAND-ad9b24e74895dd5629a573b99dc88b041d51bbaaae8cea1c72c609234f9c081b

The system shall provide a list of patrons with inactive status\.

Sources and evidence:

Source: [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>); document ID: DOC-091180de9b2d4ea83267d989411ac89f415d4def3bbf7cd51651fb7fda8d8bf9; normalized lines 557–557.

> - List of Patrons with inactive status

### REQ-370 — Claims Returned Report

- Internal key: REQ-b83f243dd4caff5a2982cfd1fff3f9ac1854a2719d08f527ea803a1ac06b64c6
- Type: functional
- Priority: P2
- Priority basis: inferred
- Priority rationale: Supports circulation exception management\.
- Originating candidates: CAND-d1b29571923af634aaf2b2333f5b92cc163bb629d8be8f769012bccb12904b4d

The system shall provide a Claims Returned report\.

Sources and evidence:

Source: [evergreen\_reference\_2009\.txt](<../data/corpus/evergreen_reference_2009.txt>); document ID: DOC-e6aa9f8c6308ab748459f87b578a0df9df9c865b7911bac3686e865963b7af6f; normalized lines 147–147.

> - Claims Returned report \(not available\)

### REQ-371 — Display Branch Growth and Shrink Trends

- Internal key: REQ-b86723d8da0e0daf49c3760e357f7eb818738e2bd2e9b8702d6839588b91deaa
- Type: functional
- Priority: P2
- Priority basis: inferred
- Priority rationale: Trend analysis supports stated long-term planning and branch management decisions\.
- Originating candidates: CAND-3ea7c0ada82784adeedcad6f8209cf12e494bfe279bae7c435be6e9ee06387f2

The system shall display branch trend data, including growth or shrink patterns, to support long-term planning\.

Sources and evidence:

Source: [conversations/conv\_pines015\_capacity\_interface\.eml](<../data/corpus/conversations/conv_pines015_capacity_interface.eml>); document ID: DOC-4acf2fdb375b86d49420e5743267e19b3f0af9ebe8bd764c1a88379aa9f5b662; normalized lines 70–71.

> One more thing - can the capacity interface also show trends? Like, is
> this branch growing or shrinking? That helps with long-term planning\.

Source: [conversations/conv\_pines015\_capacity\_interface\.eml](<../data/corpus/conversations/conv_pines015_capacity_interface.eml>); document ID: DOC-4acf2fdb375b86d49420e5743267e19b3f0af9ebe8bd764c1a88379aa9f5b662; normalized lines 88–88.

> - Trend data \(growth/shrink patterns\)

### REQ-372 — Configurable transaction history retention with indefinite aggregates

- Internal key: REQ-b9fcd55343f17bd51b0347c0e321f4ac23425e66cac9310541b1573bc9104c6f
- Type: nonfunctional
- Priority: P2
- Priority basis: inferred
- Priority rationale: Transaction history retention supports important operational and historical analysis; the source does not establish a more specific priority\.
- Originating candidates: CAND-8ed52d5f9bd9975008a4eb1a682b4f01ec1ad6dde125117d065556b26e1721f5

The system shall maintain transaction history for a configurable number of days, with monthly and annual aggregates retained indefinitely\.

Sources and evidence:

Source: [survey\_results\_2009\.txt](<../data/corpus/survey_results_2009.txt>); document ID: DOC-aac7bceef7a883652805583e98ec513b6ae2e7951e2ecfa18722127b1f12a5c4; normalized lines 109–111.

> 1\. Transaction history maintained for X days \(configurable\), with monthly and
>    annual aggregates retained indefinitely\.
> 

### REQ-373 — Report creation vs execution permissions

- Internal key: REQ-ba53da7b466cfb8817b3052a5c7ab8476e04df2e307523024641b9bc0074b549
- Type: functional
- Priority: P2
- Priority basis: inferred
- Priority rationale: Separating report creation and execution permissions materially affects access control and report governance; the source does not establish a higher priority\.
- Originating candidates: CAND-8ad6b8ce568e7c3aef1e4e9b2d01665f72b703d8483f4830d47a276c5f86757c

The system shall provide fine-grained permission controls that distinguish users who may create reports from users who may run reports\.

Sources and evidence:

Source: [evergreen\_reference\_2009\.txt](<../data/corpus/evergreen_reference_2009.txt>); document ID: DOC-e6aa9f8c6308ab748459f87b578a0df9df9c865b7911bac3686e865963b7af6f; normalized lines 81–85.

> 2\.4 PERMISSIONS
> Current permission model:
> - Staff can run any report they can access
> - No fine-grained control over who can create vs\. run reports
> - No shared folders concept

### REQ-374 — Candidate Material Query Capability

- Internal key: REQ-bbf5ddc24bfa77581600764a41060bf5809b743c27ba85945e10a17586a176ec
- Type: functional
- Priority: P2
- Priority basis: inferred
- Priority rationale: Candidate-material queries support transfer and material-selection workflows, but no explicit priority is supplied\.
- Originating candidates: CAND-5a602fc5e67480500dab31a57deeec413d7d00e4b2a59ffc6eb784226d774e33, CAND-5c4ec9e6d30a58ce848d6a54a209c90a5b78d9aa948fc50ad8cbb2615706646b

The system shall allow users to query for candidate materials\.

Sources and evidence:

Source: [conversations/conv\_pines018\_item\_transfer\.eml](<../data/corpus/conversations/conv_pines018_item_transfer.eml>); document ID: DOC-a47eb1f11286ff9099687b72a901e4a6ed2455b431087c0742aa78583c5bd80a; normalized lines 6–6.

> - Query for candidate materials

Source: [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>); document ID: DOC-091180de9b2d4ea83267d989411ac89f415d4def3bbf7cd51651fb7fda8d8bf9; normalized lines 359–361.

> The utility should include:
>   - Ability to query for candidate materials
>   - Ability to save queries for repeated use

### REQ-375 — Configurable Aged In-Transit Report \(Branch and System\)

- Internal key: REQ-bc6eb82bede0efa6ce10b1f3b98c1f6ab44253e02b292a31212ee57130c1929c
- Type: functional
- Priority: P2
- Priority basis: inferred
- Priority rationale: The report addresses lost or delayed transfers between branches and includes explicit operational scope; the source does not assign a priority\.
- Originating candidates: CAND-e19910163f256a30185b9d3ec9b1d0c289defb7335370fb91d451aead4841035

The system shall provide an in-transit items report showing items in transit for more than a configurable number of days, viewable per branch and per system, with transit-to and transit-from combined in one report\.

Sources and evidence:

Source: [interview\_cataloging\_2009-05-08\.txt](<../data/corpus/interview_cataloging_2009-05-08.txt>); document ID: DOC-a79fab45108210e6bce7d92153dfcf055f2ef6b2cdab49a3f6f5717a3e35f29f; normalized lines 64–68.

> I also need the in-transit items report\. When items are being transferred
> between branches, they sometimes get lost\. The report should show items that
> have been in-transit for more than X days \(configurable\), per branch and per
> system\. It should merge the transit-to and transit-from into one report for
> ease of use\.

### REQ-376 — Transfer Location Updates and Printable Pull Lists

- Internal key: REQ-bc8036ee36d5b4f86da1391523d862267ef6cad4a254882af196ed994a1b5cec
- Type: functional
- Priority: P2
- Priority basis: inferred
- Priority rationale: Inferred as important operational functionality; no explicit source priority is supplied\.
- Originating candidates: CAND-664a736c7fe1a44b5420ab0b2df667aa06e176510f09e1f8a881401ee417a1b6

The system shall support item transfers by allowing the item location field to be changed and by generating printable pull lists of items to be moved\.

Sources and evidence:

Source: [conversations/conv\_pines018\_item\_transfer\.eml](<../data/corpus/conversations/conv_pines018_item_transfer.eml>); document ID: DOC-a47eb1f11286ff9099687b72a901e4a6ed2455b431087c0742aa78583c5bd80a; normalized lines 10–10.

> - Mechanisms: changing location field, generating pull lists

Source: [conversations/conv\_pines018\_item\_transfer\.eml](<../data/corpus/conversations/conv_pines018_item_transfer.eml>); document ID: DOC-a47eb1f11286ff9099687b72a901e4a6ed2455b431087c0742aa78583c5bd80a; normalized lines 57–57.

> 4\. Pull list generation - create a printable list of items to be moved\.

### REQ-377 — Sortable In-Transit Report by Due Date

- Internal key: REQ-bd08cc5baa7105633ffeaa962f1b9519114f33e4a96cd0f15e1b3de0fa9e55a1
- Type: functional
- Priority: P2
- Priority basis: inferred
- Priority rationale: Due-date sorting directly supports timely operational handling of in-transit items\.
- Originating candidates: CAND-961f2c34759c754b880424202ee391f1dcf0aaeaf2650d8681ae2d5b119c0640

The in-transit report shall allow sorting by due date\.

Sources and evidence:

Source: [conversations/conv\_pines019\_020\_missing\_intransit\.eml](<../data/corpus/conversations/conv_pines019_020_missing_intransit.eml>); document ID: DOC-b233b12122cae48b5821d685f6dc058d2d2e3cc8d7f77622fa4e7e55bddc5399; normalized lines 94–95.

> Also, for the in-transit report - can we sort by due date? Front-line staff
> need to chase the oldest items first\.

### REQ-378 — Displayed Query Criteria with Results

- Internal key: REQ-bd3ec11e234a90583bd4292ad74181033b162aa711b58109abb045c077e96162
- Type: functional
- Priority: P3
- Priority basis: inferred
- Priority rationale: Showing criteria improves result transparency and usability but is not essential to basic reporting operation; no explicit source priority is provided\.
- Originating candidates: CAND-efbc4ad832f42f8da24820e05b075f750304c8a33329ba5eb79c38e4621074c5

When presenting query results, the system shall show the query selections and criteria used to produce those results\.

Sources and evidence:

Source: [email\_report\_features\.eml](<../data/corpus/email_report_features.eml>); document ID: DOC-d9e168e0c03903021bf9e636e1d8e5f56dfcb79cc110d3839e38175a7c54344e; normalized lines 34–35.

> 6\. QUERY SELECTIONS: System provides query selections along with results\.
> 

Source: [email\_report\_features\.eml](<../data/corpus/email_report_features.eml>); document ID: DOC-d9e168e0c03903021bf9e636e1d8e5f56dfcb79cc110d3839e38175a7c54344e; normalized lines 115–115.

> 6\. QUERY SELECTIONS: Show criteria with results\.

### REQ-379 — Iterative Functional-First Specification

- Internal key: REQ-be47529142a5ada1c4c3aa738a9b845d051ab53636bc881ca67513364346b5ed
- Type: nonfunctional
- Priority: P3
- Priority basis: inferred
- Priority rationale: Governs the specification process rather than runtime operation\.
- Originating candidates: CAND-d09c0175bfd6b7c30ed57e4e077a067f3a7ff37472ff68095df4c9be372d319c

The project shall specify functional requirements before detailed user-interface and data-structure requirements, with the latter defined later using an iterative, prototype-oriented methodology\.

Sources and evidence:

Source: [meeting\_minutes/meeting\_2009-03-15\_minutes\.txt](<../data/corpus/meeting_minutes/meeting_2009-03-15_minutes.txt>); document ID: DOC-defef992db2ae0e10167fd94902eac93f82c59c4c070df030ca2f77811082818; normalized lines 71–75.

> Dana Peeler raised the question of user interface specification\. Katherine
> noted that while UI would eventually need detailed specification, for now the
> focus should be on functional requirements\. She mentioned that UI and data
> structures would require further specification using an iterative, prototype-
> oriented methodology\.

### REQ-380 — Deletion Count Tracking by Location and System

- Internal key: REQ-be94c3919ab5d0714c081af3874bcc70f9daad8d1c7bf97a199089263a35167d
- Type: functional
- Priority: P1
- Priority basis: inferred
- Priority rationale: Deletion tracking supports system-wide accountability for destructive record operations; no explicit priority is supplied\.
- Originating candidates: CAND-46753964acc52b2ba175eee48ab89e67d52b4722a1be8a81019bd22c679332c0

The system shall count and track record deletions, including item, patron, and bibliographic record deletions, by location and by system\.

Sources and evidence:

Source: [conversations/conv\_pines022\_deletions\.eml](<../data/corpus/conversations/conv_pines022_deletions.eml>); document ID: DOC-7b8da7c05931fc99bc80d4a4bb0c8563e690e0c415b57f5ca1ae394462dc26c8; normalized lines 104–106.

> The system should count and track record deletions \(e\.g\., item records,
> patron records\) per location and per system\. Tracking should include:
> - Record type

### REQ-381 — Fine-grained reporting requirements \(Appendix B\)

- Internal key: REQ-bf3e61bd179254985f4f8aa789bc1e3302d88e90e92651744dfe30610f9958d9
- Type: functional
- Priority: P2
- Priority basis: inferred
- Priority rationale: The requirement covers a specified set of reporting needs, but the supplied evidence does not establish criticality\.
- Originating candidates: CAND-8ca2ed80dc991870ad8dffcd80c78d7f427b1c7dccec8d11a24f9fd0a4b728b6

The system shall support the fine-grained reporting requirements described in Appendix B\.

Sources and evidence:

Source: [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>); document ID: DOC-091180de9b2d4ea83267d989411ac89f415d4def3bbf7cd51651fb7fda8d8bf9; normalized lines 301–303.

> 8\.11 Fine-Grained Reporting Requirements
> The system must be able to support the fine-grained reports requirements as
> described in the attached specification \(see Appendix B\)\.

### REQ-382 — Demographic Analysis Reports for Program Planning

- Internal key: REQ-bf8512a398e32dcf007140a734b7981d514c6b573e5b3f3ce270486bf72b37bb
- Type: functional
- Priority: P2
- Priority basis: inferred
- Priority rationale: This supports program planning and has substantial management value, but the source does not identify it as essential to core operation\.
- Originating candidates: CAND-9845760de35b6b3a202f175e5dc71d7409d2b90091411d89d378faf86b87a77e

The system shall provide demographic analysis reports to support program planning\.

Sources and evidence:

Source: [meeting\_minutes/meeting\_2009-07-20\_minutes\.txt](<../data/corpus/meeting_minutes/meeting_2009-07-20_minutes.txt>); document ID: DOC-5ab1dd8bc97af3b1ab2e378495f0e0d75fd501fcc19f923c0d8fda831074281b; normalized lines 53–53.

>   - Demographic analysis for program planning

### REQ-383 — Capacity Summary Dashboard Across All Branches

- Internal key: REQ-c01fe7ab443cd0227e385540dd185804ba4172c292d7b8cd4e350553177e9f00
- Type: functional
- Priority: P2
- Priority basis: inferred
- Priority rationale: This provides a system-wide operational view with substantial planning and monitoring value; the supplied evidence does not define the capacity measure\.
- Originating candidates: CAND-9e77d31e02b4993148b6e1d25dff30b0391b51fb0b71eea07d10202cfc5f0373

The system shall provide a high-level summary view displaying all branches' capacity at once with key metrics\.

Sources and evidence:

Source: [conversations/conv\_pines015\_capacity\_interface\.eml](<../data/corpus/conversations/conv_pines015_capacity_interface.eml>); document ID: DOC-4acf2fdb375b86d49420e5743267e19b3f0af9ebe8bd764c1a88379aa9f5b662; normalized lines 30–36.

> This reminds me of the capacity interface from the King County spec\. It
> was basically a dashboard showing all libraries' capacity at once\.
> 
> I think we need:
> 1\. A high-level summary view \(all branches, key metrics\)
> 2\. Ability to drill down into individual branches
> 3\. Maybe color-coding - green for under capacity, yellow for getting full,

Source: [conversations/conv\_pines015\_capacity\_interface\.eml](<../data/corpus/conversations/conv_pines015_capacity_interface.eml>); document ID: DOC-4acf2fdb375b86d49420e5743267e19b3f0af9ebe8bd764c1a88379aa9f5b662; normalized lines 81–86.

> Quick summary on the system capacity interface discussion:
> 
> The system should provide an interface showing the capacity of all branches\.
> This should include:
> - High-level overview of all branches' capacity at once
> - Ability to drill down into individual branches

### REQ-384 — Track and Verify Financial Transactions

- Internal key: REQ-c0640d8210c3aea90a16e5105f2ae15748c2f98282dd9046a90d055bc2aecc54
- Type: functional
- Priority: P2
- Priority basis: inferred
- Priority rationale: Inferred as high priority because the evidence requires both tracking and verification of financial transactions\.
- Originating candidates: CAND-7bc8a57a40eb7785860f45bb4214b0f836f0903b3fe2218c3c830f44c1bb5e58

The Management Processes shall provide tools to track and verify financial transactions\.

Sources and evidence:

Source: [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>); document ID: DOC-091180de9b2d4ea83267d989411ac89f415d4def3bbf7cd51651fb7fda8d8bf9; normalized lines 90–90.

>   - Tracking and verifying financial transactions\.

### REQ-385 — Provide Deletion Totals for Month, Quarter, and Year

- Internal key: REQ-c21071092848505eebbd6bdeda465cfb14fbfa18f362247f23ce5c1524f1881f
- Type: functional
- Priority: P2
- Priority basis: inferred
- Priority rationale: Periodic deletion totals support administrative auditing, but no explicit priority is supplied\.
- Originating candidates: CAND-4bdbb953689aac51560b9bb50f0906670fed75f9a4b2f8914f9d313bb9beaaee

The system shall provide total deletion reports for month, quarter, and year periods\.

Sources and evidence:

Source: [conversations/conv\_pines022\_deletions\.eml](<../data/corpus/conversations/conv_pines022_deletions.eml>); document ID: DOC-7b8da7c05931fc99bc80d4a4bb0c8563e690e0c415b57f5ca1ae394462dc26c8; normalized lines 69–71.

> From an administrative perspective, we need reports showing:
> - Total deletions per period \(month, quarter, year\)
> - Deletions by type \(item vs patron vs other\)

### REQ-386 — Transaction Reports for Key Transaction Types

- Internal key: REQ-c2bebfaa1cf67be2e28a51f27b91850c6b592f5c2ef371a7258aef65f2f1aab1
- Type: functional
- Priority: P2
- Priority basis: inferred
- Priority rationale: This covers core operational statistics and has substantial reporting impact\.
- Originating candidates: CAND-9ecf0c4a0018aa776bf6901ae5f0cd91e8e71013f3189aa1805f10f6e90b0f1f

The system shall provide transaction reports that include check-ins, check-outs, fines collected, patron registrations, and similar transaction types\.

Sources and evidence:

Source: [survey\_results\_2009\.txt](<../data/corpus/survey_results_2009.txt>); document ID: DOC-aac7bceef7a883652805583e98ec513b6ae2e7951e2ecfa18722127b1f12a5c4; normalized lines 34–36.

>   Transactions can be grouped by hour, terminal, branch, and system\.
>   Transactions include check-ins, check-outs, fines collected, patron
>   registrations, etc\.

### REQ-387 — Define and Create PINES Report Templates

- Internal key: REQ-c3db002a14dfedfd3da9401aacc815e33685211e2d6acbce3fd703f9fbd25a9a
- Type: functional
- Priority: P2
- Priority basis: inferred
- Priority rationale: Templates are required to support the stated consortium-wide reporting scope; no explicit source priority is provided\.
- Originating candidates: CAND-f8c692d46fb6948abfef92f2690ea13ea96f65e1cd01c72a16fb9a4b393120ed

The project shall determine and create the report templates needed for all PINES libraries\.

Sources and evidence:

Source: [meeting\_minutes/meeting\_2009-03-15\_minutes\.txt](<../data/corpus/meeting_minutes/meeting_2009-03-15_minutes.txt>); document ID: DOC-defef992db2ae0e10167fd94902eac93f82c59c4c070df030ca2f77811082818; normalized lines 44–46.

>      would be filtered\.
>    - Compile a list of reports needed for an Executive Reports Interface\.
>    - Determine and create templates needed for all PINES libraries\."

### REQ-388 — Include Null and Blank Fields in Report Results by Default

- Internal key: REQ-c42c8dcbcbcb4357a68a3eb72c553896f2bff1d4b4b7848cbc49ebc5efd58dcc
- Type: functional
- Priority: P2
- Priority basis: inferred
- Priority rationale: Inferred as important for complete reporting results; no explicit source priority is supplied\.
- Originating candidates: CAND-72171ec470b8383e0311d21373bcadb03c55794bd97bb4b9806af66675ccbe77

The system shall include null and blank fields in report results by default and shall not filter them out by default\.

Sources and evidence:

Source: [evergreen\_reference\_2009\.txt](<../data/corpus/evergreen_reference_2009.txt>); document ID: DOC-e6aa9f8c6308ab748459f87b578a0df9df9c865b7911bac3686e865963b7af6f; normalized lines 204–205.

> - All nulls and blank fields included in results - current system may filter
>   some nulls

### REQ-389 — Missing and Damaged Items Reports by Branch

- Internal key: REQ-c4d72b9a148ccfffb525d21b1217f5b8e5d8d74c42bc74b985ef81413cc57116
- Type: functional
- Priority: P2
- Priority basis: inferred
- Priority rationale: The report supports branch-level inventory operations, but the source does not assign an explicit priority\.
- Originating candidates: CAND-a86a2363b8b0dcdcb802561d3634ba57ccf22e0dfa65a87446dabfebc976b97f

The system shall provide reports of missing and damaged items per branch\.

Sources and evidence:

Source: [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>); document ID: DOC-091180de9b2d4ea83267d989411ac89f415d4def3bbf7cd51651fb7fda8d8bf9; normalized lines 367–369.

> 10\.6 Missing and Damaged Items Report
> The system should provide reports of missing and damaged items per branch\.
> 

### REQ-390 — Patrons Report by Survey Answer

- Internal key: REQ-c556932e61ebe1eb1f18ecab1adda4a88e5b6ba8783dad44f339001c821a2d3c
- Type: functional
- Priority: P3
- Priority basis: inferred
- Priority rationale: This is a useful specialized report but is not essential to basic system operation\.
- Originating candidates: CAND-15e2e0a1aa9d84721ff93cb0e7cce7699ec1cfd8591c5efd818517d0f7f80146

The system shall provide a report listing patrons by survey answer\.

Sources and evidence:

Source: [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>); document ID: DOC-091180de9b2d4ea83267d989411ac89f415d4def3bbf7cd51651fb7fda8d8bf9; normalized lines 552–552.

> - List of patrons by survey answer

### REQ-391 — Patron Count Report

- Internal key: REQ-c63ab9695a805fffc87a7e5c4c76fed55cc9b72be34838cabd083f12285fbb89
- Type: functional
- Priority: P2
- Priority basis: inferred
- Priority rationale: The report is explicitly identified as a needed report type; the source does not assign a priority\.
- Originating candidates: CAND-dd61040f25203f497c75947db22c18a802e7943d9a5723aa8988aecb04fef16d

The system shall provide a Patron Count report\.

Sources and evidence:

Source: [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>); document ID: DOC-091180de9b2d4ea83267d989411ac89f415d4def3bbf7cd51651fb7fda8d8bf9; normalized lines 543–543.

> - Patron Count

### REQ-392 — Comparative Report Output with Month and Year Variance

- Internal key: REQ-c64b467dbd6b73129990452767485644aa7c902352ac4e7c99ea42d2de4d967d
- Type: functional
- Priority: P2
- Priority basis: inferred
- Priority rationale: Comparative reporting supports meaningful analysis and includes specific requested calculations, but no explicit priority is supplied\.
- Originating candidates: CAND-a8d5d50225b80bfd4b548945a13318e04bc07ea1d356cff22e9a3a1ca0f26c6c

The system shall allow report output to include comparative columns, including last month's circulation, the previous month's circulation, a percent difference, the corresponding month of the previous year, and the percent difference between last month and the corresponding month of the previous year\.

Sources and evidence:

Source: [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>); document ID: DOC-091180de9b2d4ea83267d989411ac89f415d4def3bbf7cd51651fb7fda8d8bf9; normalized lines 630–633.

> - Ability to determine the output results in a way such that a result could have
>   one column for last month's circs, another for previous month's circ, a percent
>   difference column, previous year's month column, a percent difference from
>   last month to last year's month column

### REQ-393 — Barred Patrons Report

- Internal key: REQ-c6630d70e8b3ce1a7155818aaff2e9a28ff3284a8c61290ada11e063ee3b1093
- Type: functional
- Priority: P2
- Priority basis: inferred
- Priority rationale: Supports enforcement of patron restrictions and staff decisions\.
- Originating candidates: CAND-cfa0ef0f5d7099abf8bda7d1b7d45db93eaef8b483314b9c1c194d9d24f8f7b0

The system shall provide a report listing patrons who are barred\.

Sources and evidence:

Source: [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>); document ID: DOC-091180de9b2d4ea83267d989411ac89f415d4def3bbf7cd51651fb7fda8d8bf9; normalized lines 556–556.

> - List of patrons who are BARRED

### REQ-394 — Candidate Material Queries with Example Filters

- Internal key: REQ-c97ef62d268adf8c393bbbd0fe1eceef277aa3447fcaf0652c22b2a5253140ef
- Type: functional
- Priority: P2
- Priority basis: inferred
- Priority rationale: Inferred as important collection-analysis functionality; no explicit source priority is supplied\.
- Originating candidates: CAND-66c37bfd6aafebf9eb2f2d535c0f045fa410d484fc9eb80e190b03ee8b6feca1

The system shall allow users to query for candidate materials using filters, including filters such as a children's section and no circulation during the previous 6 months\.

Sources and evidence:

Source: [interview\_cataloging\_2009-05-08\.txt](<../data/corpus/interview_cataloging_2009-05-08.txt>); document ID: DOC-a79fab45108210e6bce7d92153dfcf055f2ef6b2cdab49a3f6f5717a3e35f29f; normalized lines 47–49.

> First, we need to query for candidate materials\. Maybe we want all items in
> the children's section that haven't circulated in 6 months\. Second, we need to
> save these queries for repeated use - we do this monthly\. Third, we need to

### REQ-395 — Report Template Cloning

- Internal key: REQ-c9d0f819d4ed7c5f9decf4e72e1929fa63a3305550ac5a7a8ab7af2eb8999e3e
- Type: functional
- Priority: P3
- Priority basis: inferred
- Priority rationale: Cloning is a useful template-management capability but is not essential to basic reporting\.
- Originating candidates: CAND-130d2d443ad1cbcd94f138c9ba35450163220236f546b7ee0e40708b58cd893e

The system shall allow a user to create a new report or template variant based on an existing template without modifying the original template\.

Sources and evidence:

Source: [email\_report\_features\.eml](<../data/corpus/email_report_features.eml>); document ID: DOC-d9e168e0c03903021bf9e636e1d8e5f56dfcb79cc110d3839e38175a7c54344e; normalized lines 51–53.

> We also need the ability to "clone" reports - take an existing template and
> create a new one based on it\. This is different from modifying the template -
> it's creating a new variant\.

### REQ-396 — Patron Behavior Analysis for Return Speed and Renewal Rates

- Internal key: REQ-ca268ed9556dcf203eacc910492da68481df2879d0b235013be232affc25c437
- Type: functional
- Priority: P2
- Priority basis: inferred
- Priority rationale: The capability supports planning and behavioral analysis, but the source does not assign a formal priority level\.
- Originating candidates: CAND-0530577eccda48dc14e04a5c2edef3b73ee284be9d5f3435720ee7f6bde583c3

The system shall support demographic analysis of patron behavior, including how quickly books are returned and renewal rates\.

Sources and evidence:

Source: [survey\_results\_2009\.txt](<../data/corpus/survey_results_2009.txt>); document ID: DOC-aac7bceef7a883652805583e98ec513b6ae2e7951e2ecfa18722127b1f12a5c4; normalized lines 51–57.

>   - Transactions by age ranges
>   - Patron behavior analysis \(how quickly books are returned, renewal rates\)
>   - Demographic statistics \(must be anonymized - no personally identifiable info\)
>   - "I use demographic data to plan programming\. Age ranges and zip codes
>     are most useful\."
>   - "We need to predict patron behavior\. How likely is a book to be renewed?
>     What percent of check-outs are renewals?"

### REQ-397 — Patron Count by County Report

- Internal key: REQ-cafc0446d75c014b8e37727e28ebeaacabbefef252b93df2f9c79a32ccce3414
- Type: functional
- Priority: P3
- Priority basis: inferred
- Priority rationale: This is a specific administrative report and is useful but not shown to be essential to basic operation\.
- Originating candidates: CAND-484458b773afde4efa6f89874866fa9be9ebfcca62bf9fc60a0fe68f8a20d142

The system shall provide Patron Count by County reports\.

Sources and evidence:

Source: [evergreen\_reference\_2009\.txt](<../data/corpus/evergreen_reference_2009.txt>); document ID: DOC-e6aa9f8c6308ab748459f87b578a0df9df9c865b7911bac3686e865963b7af6f; normalized lines 155–155.

> - Patron Count by County \(not available\)

### REQ-398 — Standards-Compliant HTML Output for Web Components

- Internal key: REQ-cb082c2aeeccd4d279e1435a58b3adbcc98a7a71af12a38d83c687c98ef32dc5
- Type: nonfunctional
- Priority: P2
- Priority basis: explicitly specified
- Priority rationale: The supplied review identifies this as High Priority, which maps to P2; the priority is explicit in the review evidence\.
- Originating candidates: CAND-83b500323341e44e76d6e129dbca0f794420db375942babc4d8fca470ecd27c1

The system shall produce standards-compliant HTML output for web-based components\.

Sources and evidence:

Source: [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>); document ID: DOC-091180de9b2d4ea83267d989411ac89f415d4def3bbf7cd51651fb7fda8d8bf9; normalized lines 155–156.

> CO-2: The system must produce standards-compliant HTML output for web-based
>       components\.

### REQ-399 — Missing and Damaged Collection Report

- Internal key: REQ-cc850a0e8bb1a2805fcb12628f43ffdfbd5e1c95e4ffe6020c321e1dd012c3a1
- Type: functional
- Priority: P2
- Priority basis: inferred
- Priority rationale: Supports collection decisions with operational and financial impact\.
- Originating candidates: CAND-d3f6712c08e7d44922f0fe04ed990f57212c3c8f77e30fa30b96554da045dc53

The system shall provide a missing and damaged report with information that enables collection staff to identify whether the same titles are repeatedly lost\.

Sources and evidence:

Source: [conversations/conv\_pines019\_020\_missing\_intransit\.eml](<../data/corpus/conversations/conv_pines019_020_missing_intransit.eml>); document ID: DOC-b233b12122cae48b5821d685f6dc058d2d2e3cc8d7f77622fa4e7e55bddc5399; normalized lines 16–17.

> 2\. Collection decisions - if we keep losing the same titles, maybe we need
>    different copies or to move them to a different location

### REQ-400 — Provide Usable Report Discovery Interface

- Internal key: REQ-ccb00f03f4fa4c2a14f847a285293594b7530a66dfe327b56f1c20bff98a1e38
- Type: nonfunctional
- Priority: P2
- Priority basis: inferred
- Priority rationale: Inferred as important because report discoverability affects access to reporting functionality; no explicit source priority is supplied\.
- Originating candidates: CAND-74b20e98c3ed05986504b5bef67276866e937041a8ab9283f5756c12b0b8bbde

The reports interface shall be usable and shall allow users to find the reports they need\.

Sources and evidence:

Source: [survey\_results\_2009\.txt](<../data/corpus/survey_results_2009.txt>); document ID: DOC-aac7bceef7a883652805583e98ec513b6ae2e7951e2ecfa18722127b1f12a5c4; normalized lines 72–72.

>   - "The interface is confusing - I can't find the reports I need"

### REQ-401 — Circulation Counts by Age Demographic

- Internal key: REQ-ccfe3165ec823a23895831671c993789ea0b0653d751c602fb5717b131d9f1b2
- Type: functional
- Priority: P2
- Priority basis: inferred
- Priority rationale: Demographic circulation reporting is an important analytical capability identified as unavailable\.
- Originating candidates: CAND-18081af877f991a802132babbe7136612d56084c49dd17470790bfefaa6495ac

The system shall provide circulation count reports by age demographic\.

Sources and evidence:

Source: [evergreen\_reference\_2009\.txt](<../data/corpus/evergreen_reference_2009.txt>); document ID: DOC-e6aa9f8c6308ab748459f87b578a0df9df9c865b7911bac3686e865963b7af6f; normalized lines 140–140.

> - Circulation Count by Age Demographic \(not available\)

### REQ-402 — Configurable Item Reversion Behaviors

- Internal key: REQ-cd28ed99f62a1eaa2f8cb4f361dd5d9b9eee3e861a9470cfb53e60e5cac20237
- Type: functional
- Priority: P2
- Priority basis: inferred
- Priority rationale: Automated reversion supports operational control, but the source does not assign a formal priority level\.
- Originating candidates: CAND-0a11d6a6c6777690202274564edb434ab646222968ded51a3c42143500f5a7bd

The system shall support configurable item reversion behaviors, including reverting after a specified number of days, reverting when an item's status changes to returned, and reverting when the item is checked out at the destination\.

Sources and evidence:

Source: [conversations/conv\_pines018\_item\_transfer\.eml](<../data/corpus/conversations/conv_pines018_item_transfer.eml>); document ID: DOC-a47eb1f11286ff9099687b72a901e4a6ed2455b431087c0742aa78583c5bd80a; normalized lines 75–78.

> I like the auto-revert based on criteria\. For example:
> - Revert after X days \(date-based\)
> - Revert when item status changes to "returned" \(event-based\)
> - Revert when item is checked out at the destination \(event-based\)

### REQ-403 — All-Branch Capacity Interface

- Internal key: REQ-cdd500fe7e1bcb73b2c251da24a83a7ca3c1601a2f86194692bbb259840b70d4
- Type: functional
- Priority: P2
- Priority basis: inferred
- Priority rationale: System-wide capacity visibility supports resource allocation, but the evidence does not define the capacity measure; no explicit source priority is supplied\.
- Originating candidates: CAND-feac7279a16874f96776f98fd95775d52879b3e9b8a203c0736e4895936b3960

The system shall provide an interface showing the capacity of all branches in the system, not only the current user's branch\.

Sources and evidence:

Source: [conversations/conv\_pines015\_capacity\_interface\.eml](<../data/corpus/conversations/conv_pines015_capacity_interface.eml>); document ID: DOC-4acf2fdb375b86d49420e5743267e19b3f0af9ebe8bd764c1a88379aa9f5b662; normalized lines 3–7.

> As a branch manager, I need to see the capacity of all branches in our
> system, not just my own\. When we're deciding where to move items or
> allocate resources, it helps to see the big picture\.
> 
> Is there a way to see an overview of all branches' capacity?

### REQ-404 — Query Design Usability

- Internal key: REQ-cdf419cb18f8111c0ab93700605c3b9bb9608628eb71c153f8fdd435e8650f3e
- Type: nonfunctional
- Priority: P2
- Priority basis: inferred
- Priority rationale: Usable query design materially affects staff reporting work, but the source does not assign an explicit priority\.
- Originating candidates: CAND-25b0fe1c717bb18f40e06944be576f442ab4260b37b32f33ce93f6a7d1faf437

The query design interface shall be user-friendly\.

Sources and evidence:

Source: [email\_report\_features\.eml](<../data/corpus/email_report_features.eml>); document ID: DOC-d9e168e0c03903021bf9e636e1d8e5f56dfcb79cc110d3839e38175a7c54344e; normalized lines 6–9.

> 1\. QUERY TOOL: We need a user-friendly interface for designing queries against
>    all record types\. Staff should be able to select fields to query, select
>    values from picklists, use regular expressions from a dropdown, and use
>    Boolean operators\.

### REQ-405 — Report Access Folders

- Internal key: REQ-d12923023339df94bed4aa799fb0a18a5ab900c1d89b7ecce30f6658a6a19a67
- Type: functional
- Priority: P2
- Priority basis: inferred
- Priority rationale: Controlling staff access to reports is important for operational and administrative control, but no explicit priority is supplied\.
- Originating candidates: CAND-2d12b9a22022ba2d37420c93054e36acb67ab428385feacce108e28c2e959038

The system shall provide shared folders that allow or disallow staff from running specific reports\.

Sources and evidence:

Source: [survey\_results\_2009\.txt](<../data/corpus/survey_results_2009.txt>); document ID: DOC-aac7bceef7a883652805583e98ec513b6ae2e7951e2ecfa18722127b1f12a5c4; normalized lines 137–137.

> 11\. Shared folders to allow/disallow staff from running specific reports\.

### REQ-406 — Aggregate Patron and Circulation Metrics by Demographic or Other Attributes

- Internal key: REQ-d1604f4690e341661d46c22b2d89e58f20ae8082ce4ffc6f86d218d15626612f
- Type: functional
- Priority: P2
- Priority basis: inferred
- Priority rationale: Inferred as high priority because the evidence explicitly requests grouped circulation and patron metrics\.
- Originating candidates: CAND-7c685f0cc4bc21f8ac76d7ffb7361d3556e6e3605c829629088695dccd06a53d

The system shall provide aggregate metrics, including checkout or circulation counts and patron counts, grouped by demographic or other patron characteristics; examples include checkout counts grouped by age range and patron counts grouped by home branch\.

Sources and evidence:

Source: [conversations/conv\_pines023\_patron\_characteristics\.eml](<../data/corpus/conversations/conv_pines023_patron_characteristics.eml>); document ID: DOC-d2b26a6e7678ca4e82bfa7bb06566f329dea692ea22e8987b516fa8bc98c544b; normalized lines 25–26.

> Can we also GROUP BY these fields? Like, show me circulation by age range,
> or patron count by home branch?

Source: [conversations/conv\_pines023\_patron\_characteristics\.eml](<../data/corpus/conversations/conv_pines023_patron_characteristics.eml>); document ID: DOC-d2b26a6e7678ca4e82bfa7bb06566f329dea692ea22e8987b516fa8bc98c544b; normalized lines 41–41.

> - Group By: Show me checkout counts grouped by age range

Source: [conversations/conv\_pines023\_patron\_characteristics\.eml](<../data/corpus/conversations/conv_pines023_patron_characteristics.eml>); document ID: DOC-d2b26a6e7678ca4e82bfa7bb06566f329dea692ea22e8987b516fa8bc98c544b; normalized lines 111–116.

> - Age range
> - Zip code
> - County of residence
> - Home branch
> - Patron type
> - Preferred language

### REQ-407 — Assistive technology accessibility support

- Internal key: REQ-d18c52b5fbda674dc0f503fffd358372243cf96b23b55f8da9ecfb023dfb2511
- Type: nonfunctional
- Priority: P1
- Priority basis: explicitly specified
- Priority rationale: The source describes Section 508 accessibility compliance as non-negotiable, making it essential for mandatory compliance\.
- Originating candidates: CAND-8859d15565740cee359ee3d053a7581b23fdc5055e744b63ce68a133616ef023

The system shall work with assistive technologies including screen readers such as JAWS and NVDA, screen magnification software such as ZoomText, and other assistive technology programs\.

Sources and evidence:

Source: [interview\_sysadmin\_2009-05-10\.txt](<../data/corpus/interview_sysadmin_2009-05-10.txt>); document ID: DOC-b1738fd7a6de9498f19ede6747ba156ecb29ead86ad1c9a2768b53e862ece1a9; normalized lines 56–60.

> ROBERTY: This is non-negotiable\. As a public institution, we MUST comply with
> Section 508 accessibility requirements\. The system needs to work with:
>   - Screen readers like JAWS and NVDA
>   - Screen magnification software like ZoomText
>   - Other assistive technology programs

### REQ-408 — Accounting and Auditing Compliance for Reports and Archives

- Internal key: REQ-d1b647653268590579a6efe10ccbaf189feb43c07ca1786bc50905db6a9c6ee3
- Type: nonfunctional
- Priority: P1
- Priority basis: inferred
- Priority rationale: The requirement concerns mandatory accounting and governmental auditing compliance, which is critical compliance functionality\.
- Originating candidates: CAND-ac29e918f53aeec17db31951a5de7cab32991a9346e84c938a2939e2769b04d5

All reports and data archiving shall comply with standard accounting practice and state, county, and municipal auditing requirements\.

Sources and evidence:

Source: [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>); document ID: DOC-091180de9b2d4ea83267d989411ac89f415d4def3bbf7cd51651fb7fda8d8bf9; normalized lines 463–465.

> 13\.2 Standard Accounting Practice and Auditing Requirements
> All reports and data archiving must comply with standard accounting practice
> and state, county, and municipal auditing requirements\.

### REQ-409 — Administrative Item Location Changes

- Internal key: REQ-d23411927c5705fb0c113d7e4397dcaa6491d9f0d8e1656e92f1b42cf4039b65
- Type: functional
- Priority: P2
- Priority basis: inferred
- Priority rationale: Important administrative operation affecting collection organization\.
- Originating candidates: CAND-d4d736e3d0384a555e15ac95c1d4b632a75a9ce51740052a84143f158deb18e8

The system shall allow authorized users to change records to move items to a new location\.

Sources and evidence:

Source: [survey\_results\_2009\.txt](<../data/corpus/survey_results_2009.txt>); document ID: DOC-aac7bceef7a883652805583e98ec513b6ae2e7951e2ecfa18722127b1f12a5c4; normalized lines 89–89.

>   - Change records to move items to new location: 31%

### REQ-410 — Deletion Audit Tracking by Location and System with Reasons

- Internal key: REQ-d2696c041209b3af3e5a7f8e5f87651bb1960b00d180d868dc6b1bb1ceec382f
- Type: functional
- Priority: P2
- Priority basis: inferred
- Priority rationale: Deletion auditing supports accountability and troubleshooting with substantial operational impact, but the source does not establish it as critical\.
- Originating candidates: CAND-c581fd4f45eaf4540fbd52ec18e1e3ff13679b0bca0cdc2b1540a47883fb69a1

The system shall count and track record deletions by branch and by system and shall record the reasons for deletions to support auditing and troubleshooting\.

Sources and evidence:

Source: [interview\_cataloging\_2009-05-08\.txt](<../data/corpus/interview_cataloging_2009-05-08.txt>); document ID: DOC-a79fab45108210e6bce7d92153dfcf055f2ef6b2cdab49a3f6f5717a3e35f29f; normalized lines 91–94.

> THOMAS: Yes, we need to count and track record deletions per location and per
> system\. This is important for auditing - our directors want to know how many
> records we've deleted and why\. It also helps with troubleshooting if something
> goes missing from the catalog\.

### REQ-411 — Protect OPAC Responsiveness from Reporting Query Impact

- Internal key: REQ-d28f68b20f43ad6d365884634938ad247dce3e9ef6ea3461934efef991fe0c60
- Type: nonfunctional
- Priority: P1
- Priority basis: inferred
- Priority rationale: Fast patron access to the catalog is explicitly required for core operation, although no formal priority is supplied\.
- Originating candidates: CAND-47e24ba0fc59bca7f7679ce23baab7b1340d0c2b7fdb1238cc6eeec843bb8162

The management reporting system shall not constrain OPAC access or reduce OPAC responsiveness when reporting queries execute\.

Sources and evidence:

Source: [interview\_sysadmin\_2009-05-10\.txt](<../data/corpus/interview_sysadmin_2009-05-10.txt>); document ID: DOC-b1738fd7a6de9498f19ede6747ba156ecb29ead86ad1c9a2768b53e862ece1a9; normalized lines 101–104.

> ROBERT: Yes - the OPAC module\. The management reporting system must not
> constrain the OPAC in any way\. These are separate concerns\. Patrons need
> fast, responsive access to the catalog\. If the reporting system is doing a
> big query, it should NOT slow down the OPAC\.

### REQ-412 — Inactive Patron Status Report

- Internal key: REQ-d29d0f486142c33bb4c83b82d8a6c815a213413432aeb25c117b21d902ddc423
- Type: functional
- Priority: P2
- Priority basis: inferred
- Priority rationale: Inactive-patron status reporting is an important administrative capability, but no explicit priority is supplied\.
- Originating candidates: CAND-51c2839ac1c5c390bd5211c03c7947213fad8a6e18343168a3dd991e4afdcf9e

The system shall provide a report listing patrons with inactive status\.

Sources and evidence:

Source: [evergreen\_reference\_2009\.txt](<../data/corpus/evergreen_reference_2009.txt>); document ID: DOC-e6aa9f8c6308ab748459f87b578a0df9df9c865b7911bac3686e865963b7af6f; normalized lines 158–158.

> - List of Patrons with inactive status \(not available\)

### REQ-413 — Isolate Reporting to Avoid OPAC Performance Impact

- Internal key: REQ-d3b1aec41f48d0399de3eeb823e8fbfb84723fa669e2826cd1f4b61a2ac35e6d
- Type: nonfunctional
- Priority: P1
- Priority basis: inferred
- Priority rationale: Inferred as critical because the evidence states that reporting must not slow or interfere with the public catalog\.
- Originating candidates: CAND-8605bb41f899a282e44b60c17009adb4f4c9196d0c3fb71fd417ded3491590c7

The reporting system shall not constrain, interfere with, or slow down the OPAC or public catalog; reporting activity shall be isolated from OPAC performance\.

Sources and evidence:

Source: [meeting\_tech\_subcommittee\_2009-06-30\.txt](<../data/corpus/meeting_tech_subcommittee_2009-06-30.txt>); document ID: DOC-e081aa7bd57bf5e59c75a8a86f592124757b74dff1ee0df4badc10c025092d96; normalized lines 75–77.

> "We absolutely cannot constrain the OPAC," Robert emphasized\. "The management
> reporting system is separate from the public catalog\. If a report is running,
> it should not slow down the OPAC\."

### REQ-414 — Editable Display Fields for Canned Reports

- Internal key: REQ-d3e96b7a6e5b39fbffd47beebd2633fda0d21b94226a25556b0fcfb870f63fbb
- Type: functional
- Priority: P3
- Priority basis: inferred
- Priority rationale: Inferred as useful report customization; no explicit source priority is supplied\.
- Originating candidates: CAND-6b207c4fc26b18a238340c717d7bc5f081933d4c29c03cb9865138c3d279dac0

The system shall allow users to edit the display fields of a predefined report, including adding fields such as shelving location\.

Sources and evidence:

Source: [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>); document ID: DOC-091180de9b2d4ea83267d989411ac89f415d4def3bbf7cd51651fb7fda8d8bf9; normalized lines 635–636.

> - Ability to edit canned report for display purposes such as adding shelving
>   location as a display

### REQ-415 — Open Template Reporting with Attribute Filtering

- Internal key: REQ-d43b435d85005b904ebee7be3f3cd9894dfd5641df5d4206ec0c4fe11de0edfd
- Type: functional
- Priority: P2
- Priority basis: inferred
- Priority rationale: The original specification normatively requires open-template reporting with the stated filtering and display attributes, but does not assign a formal priority level\.
- Originating candidates: CAND-0eac9bd1b3990e377378abff6a437d8c1a802b4fc006b424f9eab55526732ef5

The system shall provide open template reporting in which attributes associated with circulation, patrons, items, bills, and bibliographic records are available for filtering and display\.

Sources and evidence:

Source: [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>); document ID: DOC-091180de9b2d4ea83267d989411ac89f415d4def3bbf7cd51651fb7fda8d8bf9; normalized lines 615–618.

> 15\.4 Open Template Reporting
> Open template would have all attributes associated with say circulation,
> patrons, items, bills, and bibs to select from for filtering and the same
> attributes for displaying\.

### REQ-416 — Deletion Log for Traceability and Accountability

- Internal key: REQ-d473b44f695f3eae8cf58829ac3f81ab5dd1eef738c287cc8ec984815efed028
- Type: functional
- Priority: P1
- Priority basis: inferred
- Priority rationale: Deletion accountability and traceability support security, auditability, and troubleshooting of potentially consequential data loss\.
- Originating candidates: CAND-aa11c7137274f313cd691dfdebf80c43e28280fe321cd6c81fe47291bbd7183e

The system shall provide a deletion log that allows users to trace deletions for accountability and troubleshooting, including investigating why a patron record disappeared\.

Sources and evidence:

Source: [conversations/conv\_pines022\_deletions\.eml](<../data/corpus/conversations/conv_pines022_deletions.eml>); document ID: DOC-7b8da7c05931fc99bc80d4a4bb0c8563e690e0c415b57f5ca1ae394462dc26c8; normalized lines 53–57.

> I agree with George - this is about accountability\. If we accidentally
> delete something we shouldn't have, we need to be able to trace it\.
> 
> Also, the deletion log would help with troubleshooting\. "Why did this
> patron's record disappear?" - check the log\.

### REQ-417 — Collection Age Reports

- Internal key: REQ-d4d3a796d19421135bcf413b6e3a5b677cc98471ad9d1c6a350e17d7e67d7527
- Type: functional
- Priority: P3
- Priority basis: inferred
- Priority rationale: This is a useful collection-analysis report, but the source does not indicate that it is essential to basic operation\.
- Originating candidates: CAND-3667b7f07ca36c5ad267494f8549580978de8578176517783797a1a6548e69e1

The system shall provide age-of-collection reports by call number\.

Sources and evidence:

Source: [evergreen\_reference\_2009\.txt](<../data/corpus/evergreen_reference_2009.txt>); document ID: DOC-e6aa9f8c6308ab748459f87b578a0df9df9c865b7911bac3686e865963b7af6f; normalized lines 149–149.

> - Age of collection by call number \(not available\)

### REQ-418 — Open-Hours Processing Without Disruption \(Highly Desirable\)

- Internal key: REQ-d51ad6fcb102275e5fa971142968e1fa6051a21b5e00031c4ad0e3c2e2dfa509
- Type: nonfunctional
- Priority: P3
- Priority basis: inferred
- Priority rationale: The source labels this capability highly desirable rather than mandatory, so it is treated as a useful but nonessential performance and availability preference\.
- Originating candidates: CAND-df016350837281f634cb397b3d1d31c88211e938f4701339cd9b54cb40188ff4

The system shall support processing searches and reports during open hours without disrupting other system functions, as a highly desirable capability\.

Sources and evidence:

Source: [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>); document ID: DOC-091180de9b2d4ea83267d989411ac89f415d4def3bbf7cd51651fb7fda8d8bf9; normalized lines 128–129.

>       It is highly desirable that searches and reports can be processed during
>       open hours without disrupting other system functions\.

### REQ-419 — Real-Time Reporting Including Busy Periods

- Internal key: REQ-d57d5296e629b8980c231ff304e333628dee47017c28850693b93312c33f5425
- Type: functional
- Priority: P2
- Priority basis: inferred
- Priority rationale: Real-time reporting is identified as a needed reporting capability, but no explicit priority is supplied\.
- Originating candidates: CAND-46cf96a343e04929d1ccef7c3f9f84fdcf02294a5e8de9723d936fa074eebbb9, CAND-486756b6cedb8d4ab9e4e0b56f5b19654991e40e0c1f557a5efcf2343a71c26f

The system shall support real-time reporting, including for busy periods\.

Sources and evidence:

Source: [evergreen\_reference\_2009\.txt](<../data/corpus/evergreen_reference_2009.txt>); document ID: DOC-e6aa9f8c6308ab748459f87b578a0df9df9c865b7911bac3686e865963b7af6f; normalized lines 170–170.

> - No real-time reporting \(all reports are run on current data\)

Source: [survey\_results\_2009\.txt](<../data/corpus/survey_results_2009.txt>); document ID: DOC-aac7bceef7a883652805583e98ec513b6ae2e7951e2ecfa18722127b1f12a5c4; normalized lines 98–98.

>   - "Real-time reporting for busy periods"

### REQ-420 — Real-Time Reporting Support

- Internal key: REQ-d5fd2cdf349e1983bec192b4eb768ae65ed45d13911604cb596f3f640c5dee59
- Type: functional
- Priority: P2
- Priority basis: inferred
- Priority rationale: Real-time reporting can materially affect operational decision-making, but the source does not establish a more specific priority\.
- Originating candidates: CAND-9509453ac6e0b28ed5f03b75e51425c97fa270d882bc854211d4da781c6edb98

The system shall support real-time reporting\.

Sources and evidence:

Source: [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>); document ID: DOC-091180de9b2d4ea83267d989411ac89f415d4def3bbf7cd51651fb7fda8d8bf9; normalized lines 655–655.

> - Ability to have real time reporting

### REQ-421 — Total Use Count Report

- Internal key: REQ-d6788da5598c6cea601bd5ee6c8f91d48bf76514b190467aacd1e73ae90d4332
- Type: functional
- Priority: P3
- Priority basis: inferred
- Priority rationale: Useful collection-use reporting, but not essential to basic operation\.
- Originating candidates: CAND-cc52dd7278fcf306a9bc29a24ad8bdcb140c19832924ba3b73843e3d2dd01032

The system shall provide a report listing items with their total use count\.

Sources and evidence:

Source: [evergreen\_reference\_2009\.txt](<../data/corpus/evergreen_reference_2009.txt>); document ID: DOC-e6aa9f8c6308ab748459f87b578a0df9df9c865b7911bac3686e865963b7af6f; normalized lines 144–144.

> - List of Items with specific Total Use Count \(not available\)

### REQ-422 — Configuration Migration for Report Configurations and Templates

- Internal key: REQ-d859a0ba10e78959c7c0d7ba2b4e9332f78e5f6ebfd0bbd0d45d7f07fbeda938
- Type: nonfunctional
- Priority: P2
- Priority basis: inferred
- Priority rationale: Configuration migration is identified as a required management capability, but the source does not assign a formal priority level\.
- Originating candidates: CAND-0003949c2d2ce1f2fe45c76e382d2c4c6ff6a3e881aa87224837a4b327aa5731

The system shall provide configuration migration between environments for report configurations and templates\.

Sources and evidence:

Source: [evergreen\_reference\_2009\.txt](<../data/corpus/evergreen_reference_2009.txt>); document ID: DOC-e6aa9f8c6308ab748459f87b578a0df9df9c865b7911bac3686e865963b7af6f; normalized lines 187–187.

> - No configuration migration between environments

### REQ-423 — Items Not Checked Out in Specified Period

- Internal key: REQ-d90e07518a4dcac124e6c0529ede02d1bf245da9661ccf721941c46ebd7167a2
- Type: functional
- Priority: P3
- Priority basis: inferred
- Priority rationale: This supports inventory and collection management but is not shown to be essential to basic operation\.
- Originating candidates: CAND-505b347f91609a09079a50d102633715a472959275690e9c907e4daa96ad8715

The system shall provide a report listing items that have not been checked out in a specified number of days\.

Sources and evidence:

Source: [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>); document ID: DOC-091180de9b2d4ea83267d989411ac89f415d4def3bbf7cd51651fb7fda8d8bf9; normalized lines 277–279.

>   - Bibliographic records with holds
>   - Items that have not been checked out in X days
>   - Item-level holds

### REQ-424 — Group and Role-Based Access Control

- Internal key: REQ-da5b82ffef316e3d9074e055fe0dd4ecb19fdce1ca08e6f1bbd17a83299b5f32
- Type: nonfunctional
- Priority: P1
- Priority basis: inferred
- Priority rationale: Access control is essential for protecting system functions and data\.
- Originating candidates: CAND-9d3462625b7e63c50d1e35d15d0af6a7edb5a70aed396ea4fc1542cfa71577e5

The system shall control user rights and privileges through security groups and/or roles that provide access control for individuals, workgroups, and arbitrary staff groups\.

Sources and evidence:

Source: [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>); document ID: DOC-091180de9b2d4ea83267d989411ac89f415d4def3bbf7cd51651fb7fda8d8bf9; normalized lines 163–165.

> CO-4: User rights and privileges will be controlled through security groups and
>       or "roles" that allow access control for individuals, workgroups, and
>       arbitrary staff groups\.

### REQ-425 — Unfilled Holds and Stale Holds Reports

- Internal key: REQ-da7a4b4bedd8da13c1273bcc6a5832c2493ea4777aab55605d574a6ef269e7ce
- Type: functional
- Priority: P2
- Priority basis: inferred
- Priority rationale: The reports address operational hold exceptions and are identified as unavailable requested functionality, but no explicit priority is supplied\.
- Originating candidates: CAND-aa5410337ef1b7439bd5a1058ff24d95d7f9d1ba845d79c210f8ef716e145849

The system shall provide Unfilled Holds and Stale Holds reports\.

Sources and evidence:

Source: [evergreen\_reference\_2009\.txt](<../data/corpus/evergreen_reference_2009.txt>); document ID: DOC-e6aa9f8c6308ab748459f87b578a0df9df9c865b7911bac3686e865963b7af6f; normalized lines 161–162.

> - Unfilled Holds \(not available\)
> - Stale Holds \(not available\)

### REQ-426 — Readable and Specific Documentation

- Internal key: REQ-daba49d0be7838dfae3529944f71dad32c939b30e275edd1c65205f02817b8a8
- Type: nonfunctional
- Priority: P2
- Priority basis: inferred
- Priority rationale: Documentation readability and implementation specificity are important for stakeholder use and delivery\.
- Originating candidates: CAND-1f9af3d8cfafc1a79b14ad82a43a7ccc259d8e4992ec3489c83d57eebf387189

The SRS and related documentation shall be readable by non-technical library managers and staff while providing sufficient specificity for software developers\.

Sources and evidence:

Source: [meeting\_minutes/meeting\_2009-03-15\_minutes\.txt](<../data/corpus/meeting_minutes/meeting_2009-03-15_minutes.txt>); document ID: DOC-defef992db2ae0e10167fd94902eac93f82c59c4c070df030ca2f77811082818; normalized lines 111–117.

> 5\. INTENDED AUDIENCE
> --------------------------------------------------------------------------------
> Katherine stated that this SRS would be intended both for library managers and
> staff who may contribute additional requirements, and for software project
> managers and developers who will implement the requirements\. She emphasized
> the need to aim for a high level of readability for a non-technical audience
> while providing enough specificity for developers\.

### REQ-427 — Provide IntraPINES Loans Reports for All Systems

- Internal key: REQ-db35fce9a845b58a4873b121735c4bf5cc443172401968ac0f0633d03e1c939c
- Type: functional
- Priority: P3
- Priority basis: inferred
- Priority rationale: The source requests this report but provides no explicit criticality or priority; it is therefore treated as useful functionality that is not established as essential to basic operation\.
- Originating candidates: CAND-ba4fcc948dccffc971be6171e69d11c7b35420c4c1ca0f38f2ad8ad9e5ca2785

The system shall provide IntraPINES Loans reports for all systems\.

Sources and evidence:

Source: [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>); document ID: DOC-091180de9b2d4ea83267d989411ac89f415d4def3bbf7cd51651fb7fda8d8bf9; normalized lines 565–565.

> - IntraPINES Loans for all Systems

### REQ-428 — Staff Card-Swipe Login

- Internal key: REQ-db975f9e2b8eb2bd106cef17674bd91e6e005e90b976e2fc5a3dc096779f382e
- Type: functional
- Priority: P2
- Priority basis: inferred
- Priority rationale: Staff authentication is important system functionality, although the evidence does not establish that it is mandatory for every site\.
- Originating candidates: CAND-eaf45ec50a8f86836a0cdb9abac7f25c886e5ab364647207f4b9b799a1dc241e

The system shall support staff login via card swipe\.

Sources and evidence:

Source: [meeting\_minutes/meeting\_2009-07-20\_minutes\.txt](<../data/corpus/meeting_minutes/meeting_2009-07-20_minutes.txt>); document ID: DOC-5ab1dd8bc97af3b1ab2e378495f0e0d75fd501fcc19f923c0d8fda831074281b; normalized lines 46–46.

>   - Staff login needs \(card swipe\) - already discussed via email

### REQ-429 — Combine Patron Demographic and Activity Filters

- Internal key: REQ-dba1573e94e93bcbb636662d0569f4c75f556b400afa80de184a788372ea820f
- Type: functional
- Priority: P2
- Priority basis: inferred
- Priority rationale: Combined patron filtering supports targeted analysis and is an important reporting capability; the source does not assign a priority\.
- Originating candidates: CAND-df28e114db86cde167ee8c617846543d59cabe26d69a6d069eeddd0e48a94edf

The system shall support combining demographic filters with activity-based filters, including selecting patrons who have not checked out items within a specified time window\.

Sources and evidence:

Source: [conversations/conv\_pines023\_patron\_characteristics\.eml](<../data/corpus/conversations/conv_pines023_patron_characteristics.eml>); document ID: DOC-d2b26a6e7678ca4e82bfa7bb06566f329dea692ea22e8987b516fa8bc98c544b; normalized lines 61–63.

> Can we combine demographic filters? Like "show me all Juvenile patrons in
> zip code 30505 who haven't checked anything out in 6 months"?
> 

### REQ-430 — Invalid Item Type Report

- Internal key: REQ-dbdeecc38b3a0d1140bd17181b88eef0f06a8dad6885d377c9f48bda0c9db257
- Type: functional
- Priority: P2
- Priority basis: inferred
- Priority rationale: The source explicitly identifies this report, but does not establish it as essential to basic operation\.
- Originating candidates: CAND-ca960eb5a90f3ea2b379e68a5e90ab77b9cd3005bae369b733d274273059a07b

The system shall provide a report of items with an invalid item type\.

Sources and evidence:

Source: [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>); document ID: DOC-091180de9b2d4ea83267d989411ac89f415d4def3bbf7cd51651fb7fda8d8bf9; normalized lines 280–280.

>   - Items with invalid item type

### REQ-431 — Audit-Compliant Reporting and Data Archiving

- Internal key: REQ-dbf327c03cf29ea9551b738993c8c3775c4ad1a460e18229fe09a6665a03e2b8
- Type: nonfunctional
- Priority: P1
- Priority basis: inferred
- Priority rationale: Inferred as critical because the source requires compliance with accounting and governmental auditing requirements\.
- Originating candidates: CAND-67cdd29e03ee6b04f5050e938bbda03b78a72eef7f2d1690350bd532965105b4

The system shall ensure that reports and data archiving comply with standard accounting practice and state, county, and municipal auditing requirements\.

Sources and evidence:

Source: [email\_financial\_reports\.eml](<../data/corpus/email_financial_reports.eml>); document ID: DOC-8b6cfb3cf368b794d82567933f9c85062740814819b1e28b4837f6021cbcbee6; normalized lines 25–26.

> 4\. Compliance - all reports and data archiving must comply with standard
>    accounting practice and state, county, and municipal auditing requirements\.

Source: [email\_financial\_reports\.eml](<../data/corpus/email_financial_reports.eml>); document ID: DOC-8b6cfb3cf368b794d82567933f9c85062740814819b1e28b4837f6021cbcbee6; normalized lines 112–115.

> 2\. COMPLIANCE:
>    All reports and data archiving must comply with standard accounting practice
>    and state, county, and municipal auditing requirements\.
> 

### REQ-432 — Enhanced Detailed Aged Debt Report

- Internal key: REQ-dc8673fa44b4a60ae680f42eafc76986598f270c996ead53aa067a78ac633007
- Type: functional
- Priority: P2
- Priority basis: inferred
- Priority rationale: The source identifies this as an existing report needing enhancement, indicating important financial functionality without establishing criticality\.
- Originating candidates: CAND-c6ca6db558320760100809a27201bb3d8908951adc676e457071b0040593270a

The system shall provide an enhanced detailed Aged Debt report\.

Sources and evidence:

Source: [evergreen\_reference\_2009\.txt](<../data/corpus/evergreen_reference_2009.txt>); document ID: DOC-e6aa9f8c6308ab748459f87b578a0df9df9c865b7911bac3686e865963b7af6f; normalized lines 163–163.

> - Aged Debt detailed report \(partially available, needs enhancement\)

### REQ-433 — Circulation Count Reports Filtered by Selected MARC Fields

- Internal key: REQ-dc8bf974feab6a41ea64c95956f6a2157bc7d7f1e622c25709b16017a6cad4ab
- Type: functional
- Priority: P2
- Priority basis: inferred
- Priority rationale: The report is identified as unavailable and requested functionality, making it important reporting capability, but no explicit priority is supplied\.
- Originating candidates: CAND-a87f0fb4d2226b1365e3b636f939e3d5f75901e610c1fffc763098c1313384f3

The system shall provide circulation count reports grouped or filtered by selected MARC fields\.

Sources and evidence:

Source: [evergreen\_reference\_2009\.txt](<../data/corpus/evergreen_reference_2009.txt>); document ID: DOC-e6aa9f8c6308ab748459f87b578a0df9df9c865b7911bac3686e865963b7af6f; normalized lines 138–138.

> - Circulation Count by MARC fields \(not available\)

### REQ-434 — Historical Snapshot Bills Report

- Internal key: REQ-dd339030fc9431951c3c9bd8643de814c2e61efed7cb83d39832cf4e10f99963
- Type: functional
- Priority: P2
- Priority basis: inferred
- Priority rationale: Historical bills reporting supports important financial and account analysis\.
- Originating candidates: CAND-21a5d65bfd2cc8d54ddfc0b454248cec0f82e2c7aabb3d118c6a9ebf4ab706ba

The system shall provide a snapshot bills report that can retrieve data from an earlier point in time\.

Sources and evidence:

Source: [survey\_results\_2009\.txt](<../data/corpus/survey_results_2009.txt>); document ID: DOC-aac7bceef7a883652805583e98ec513b6ae2e7951e2ecfa18722127b1f12a5c4; normalized lines 101–101.

>   - "Need a snapshot bills report going back in time"

### REQ-435 — Provide Holds Purchase Alert Report

- Internal key: REQ-dd39afb13a3d552adde49376cfce9baa9b23299e94197f6472a8f4173d9456d3
- Type: functional
- Priority: P3
- Priority basis: inferred
- Priority rationale: This specific management report is not shown to be essential to basic operation; no explicit source priority is provided\.
- Originating candidates: CAND-f4d7b321c9a56869fcbfd4418432072925db090b2fbe0581675fbdcbc4d178c0

The system shall provide a Holds Purchase Alert report\.

Sources and evidence:

Source: [evergreen\_reference\_2009\.txt](<../data/corpus/evergreen_reference_2009.txt>); document ID: DOC-e6aa9f8c6308ab748459f87b578a0df9df9c865b7911bac3686e865963b7af6f; normalized lines 160–160.

> - Holds Purchase Alert \(not available\)

### REQ-436 — Report Coverage Expansion

- Internal key: REQ-dd5e4aab34ad1f30eed68d71ed9f66c1e1be398ab1a18fb6b92da7d460366846
- Type: functional
- Priority: P2
- Priority basis: inferred
- Priority rationale: The source explicitly identifies expansion of report coverage as a management-level requirement; it does not assign a P-level priority\.
- Originating candidates: CAND-256c8209b11df7aa149ad954bcd18bbe20f6e344ffdf1e8aef8aac79c5dcabb8

The system shall expand the available report types to cover all identified reporting gaps\.

Sources and evidence:

Source: [evergreen\_reference\_2009\.txt](<../data/corpus/evergreen_reference_2009.txt>); document ID: DOC-e6aa9f8c6308ab748459f87b578a0df9df9c865b7911bac3686e865963b7af6f; normalized lines 214–214.

> 1\. Expand the available report types to cover all identified gaps

### REQ-437 — Web or Windows Client Access

- Internal key: REQ-de70dda33ee3be7e7ed90b39ce8fa8fc27f384bca6ab288f52fbe9dfe0d6597e
- Type: nonfunctional
- Priority: P2
- Priority basis: explicitly specified
- Priority rationale: The review identifies browser-or-Windows access as High Priority, which maps to P2; this priority is explicit in the supplied review feedback\.
- Originating candidates: CAND-6f5236be44966ed2c699a62259d4144e6748ff7fb65d465edc6536420ef3f150

The system shall be accessible through a web browser or a Windows-compatible client\.

Sources and evidence:

Source: [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>); document ID: DOC-091180de9b2d4ea83267d989411ac89f415d4def3bbf7cd51651fb7fda8d8bf9; normalized lines 135–136.

> OE-3: The system must be accessible through a web browser or a Windows-compatible
>       client\.

### REQ-438 — Streamlined Staff Login via Card Reader or Swipe

- Internal key: REQ-df7d84a99e4c5d334f09662aab74f7aeb94c7223846fea2de072f152a669cdf6
- Type: nonfunctional
- Priority: P2
- Priority basis: inferred
- Priority rationale: The source identifies both service-speed and security benefits, making this important, but does not establish it as critical or mandatory compliance\.
- Originating candidates: CAND-c7203c53d0d60c5c36e711452a21601b682bc60a8c33212a30d68c672ef62f66

The system shall provide a streamlined login method, such as card-reader login or card-swipe login, that is faster than manually typing a full username and password, supports faster service during busy periods, and improves security by reducing password sharing and preventing terminals from being left logged in\.

Sources and evidence:

Source: [email\_staff\_login\.eml](<../data/corpus/email_staff_login.eml>); document ID: DOC-64b10e94c42508c5aea1af877ec9d2fe34485b099b29994b8b1a76cadc55e8b3; normalized lines 9–16.

> 1\. It slows down service - especially during busy periods, staff are spending
>    precious seconds logging in instead of helping patrons\.
> 2\. It leads to security issues - staff get in a hurry and sometimes share
>    passwords or leave terminals logged in\.
> 
> We've seen other library systems implement card-swipe login for their ILS
> terminals\. The staff member simply swipes their employee ID badge and is logged
> in immediately\. This is much faster and more secure\.

### REQ-439 — Separate Development, Training, and Production Environments

- Internal key: REQ-e17884bd89d6e507fbba4f4e181ef3f1111c5d82b19faa3163a9c87629ad9e36
- Type: nonfunctional
- Priority: P3
- Priority basis: explicitly specified
- Priority rationale: The review identifies development and training environment support as Medium Priority, which maps to P3; this priority is explicit in the supplied review feedback\.
- Originating candidates: CAND-6dae8ec2820d2d9e062e45b2d94cdb80d15819b65bd1a645a015e1f5b2b53028

The system shall provide separate development, training, and production environments\.

Sources and evidence:

Source: [meeting\_tech\_subcommittee\_2009-06-30\.txt](<../data/corpus/meeting_tech_subcommittee_2009-06-30.txt>); document ID: DOC-e081aa7bd57bf5e59c75a8a86f592124757b74dff1ee0df4badc10c025092d96; normalized lines 49–55.

> 2\.3 DEVELOPMENT AND TRAINING ENVIRONMENT
> The need for separate development, training, and production environments was
> discussed\.
> 
> "We have a dev server, a training server, and production," Robert explained\.
> "What we need is a way to migrate configurations between them\. Export/import
> of templates, permission settings, and saved queries\."

### REQ-440 — Time-Based Item Reversion to Original Location

- Internal key: REQ-e1999db196c744b6763264bcf9683eab9f1904e559fd3f2ede45f99fcb56647d
- Type: functional
- Priority: P2
- Priority basis: inferred
- Priority rationale: Automatic reversion supports transfer and location management, but no explicit priority is supplied\.
- Originating candidates: CAND-628659d7e54565c7142b34c645ad3aacdf376128c95a35f36a963e93a00eff11

The system shall revert items to their original location after a configured period of time\.

Sources and evidence:

Source: [conversations/conv\_pines018\_item\_transfer\.eml](<../data/corpus/conversations/conv_pines018_item_transfer.eml>); document ID: DOC-a47eb1f11286ff9099687b72a901e4a6ed2455b431087c0742aa78583c5bd80a; normalized lines 11–11.

> - Revert items to original location after a set period of time

Source: [conversations/conv\_pines018\_item\_transfer\.eml](<../data/corpus/conversations/conv_pines018_item_transfer.eml>); document ID: DOC-a47eb1f11286ff9099687b72a901e4a6ed2455b431087c0742aa78583c5bd80a; normalized lines 75–76.

> I like the auto-revert based on criteria\. For example:
> - Revert after X days \(date-based\)

### REQ-441 — Controlled Report Templates with Restricted Modifications

- Internal key: REQ-e1d92790466974fc198f225f7c73bbf0455ee79e499911a16bb9838689050657
- Type: functional
- Priority: P2
- Priority basis: inferred
- Priority rationale: Inferred as high priority because the evidence requires reusable staff templates with administrator-controlled safeguards for accuracy\.
- Originating candidates: CAND-7f44ee73048fd67a14b16385384c01c18fd590c7eadf8a36b1a8eab65074103f

The system shall allow system administrators to create report templates available to staff; templates shall be runnable as-is or modifiable for individual needs, and administrators shall be able to limit which filters and display fields can be altered so that modifications do not compromise result accuracy\.

Sources and evidence:

Source: [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>); document ID: DOC-091180de9b2d4ea83267d989411ac89f415d4def3bbf7cd51651fb7fda8d8bf9; normalized lines 231–236.

> 8\.2 Report Templates
> System administrators should be able to create report templates that are
> available to staff\. These templates should be runnable as-is or modifiable
> for individual needs\. Changes to templates should not compromise the accuracy
> of results\. Administrators should be able to limit which filters and display
> fields can be altered, to certify a dependable output\.

Source: [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>); document ID: DOC-091180de9b2d4ea83267d989411ac89f415d4def3bbf7cd51651fb7fda8d8bf9; normalized lines 238–240.

> For example, front-line staff could set a call number range for a weeding
> report or add/remove display fields from a pick list, but they should not be
> able to alter the template to display deleted items\.

### REQ-442 — Validated Report Output

- Internal key: REQ-e1f083ff6431150ab09c9b0dceafffdafe1bcb791bf007e9409e51e5cca6d71e
- Type: nonfunctional
- Priority: P2
- Priority basis: inferred
- Priority rationale: Validated output supports reporting reliability, but no explicit priority is supplied\.
- Originating candidates: CAND-5664e5b7c6b7a93ac02a7f27a0232ff513f282457ae7056ad06ac7a87c3f430f

The system shall provide report outputs that are tested and proven\.

Sources and evidence:

Source: [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>); document ID: DOC-091180de9b2d4ea83267d989411ac89f415d4def3bbf7cd51651fb7fda8d8bf9; normalized lines 650–650.

> - Tested and proven output

### REQ-443 — Prioritize Reports in the Queue Based on Configured Rules or Authorization

- Internal key: REQ-e2198787a3bf0d0b9cccf0d6a403c423ee5ddf2c442dbee047c6b41f970fe238
- Type: functional
- Priority: P2
- Priority basis: inferred
- Priority rationale: Inferred as high priority because the evidence describes report prioritization as important and requires important reports to advance in the queue\.
- Originating candidates: CAND-7aee1d495375912cd5549097c76e182df045d40ca73333de5751b0b4126407e5, CAND-7bb3e03cee1a1e2e3e8186753a4808d455c327b48d71aba2591ff3135482cc85

The system shall support report prioritization so that configured report types or authorized users can place important reports ahead of lower-priority, ad-hoc, or resource-consuming reports in the queue, including advancing a director's board report ahead of a staff member's ad-hoc query\.

Sources and evidence:

Source: [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>); document ID: DOC-091180de9b2d4ea83267d989411ac89f415d4def3bbf7cd51651fb7fda8d8bf9; normalized lines 640–641.

> - Ability to prioritize certain types of reports so they will pop to the top of
>   the queue over resource-consuming reports

Source: [email\_report\_features\.eml](<../data/corpus/email_report_features.eml>); document ID: DOC-d9e168e0c03903021bf9e636e1d8e5f56dfcb79cc110d3839e38175a7c54344e; normalized lines 89–91.

> Also, the ability to prioritize certain reports is crucial\. A director's
> board report should be able to jump ahead of a staff member's ad-hoc query\.
> 

Source: [email\_report\_features\.eml](<../data/corpus/email_report_features.eml>); document ID: DOC-d9e168e0c03903021bf9e636e1d8e5f56dfcb79cc110d3839e38175a7c54344e; normalized lines 119–119.

> 8\. PRIORITY: Important reports can jump queue\.

### REQ-444 — Concurrent Report Execution

- Internal key: REQ-e232db84f6ac3702fbcf9c21b5950240207156619faab648f54686921672b66f
- Type: functional
- Priority: P3
- Priority basis: inferred
- Priority rationale: Concurrent execution improves convenience and workflow efficiency but is not identified as essential to basic operation\.
- Originating candidates: CAND-635ccdd5fb895245a950d18fd6fdb89c74f0797cfa517a043b96112ea4f4464a

The system shall allow users to select and run multiple reports at the same time\.

Sources and evidence:

Source: [evergreen\_reference\_2009\.txt](<../data/corpus/evergreen_reference_2009.txt>); document ID: DOC-e6aa9f8c6308ab748459f87b578a0df9df9c865b7911bac3686e865963b7af6f; normalized lines 78–78.

> - No ability to check multiple reports to run at the same time

### REQ-445 — Historical Reporting Data Store

- Internal key: REQ-e26676d4799d8384065b88af0e33d7aba467b420e3732dc6a47af1d4a1ea0fbb
- Type: nonfunctional
- Priority: P2
- Priority basis: inferred
- Priority rationale: Historical reporting supports important longitudinal analysis, although it is not stated to be critical to core operation\.
- Originating candidates: CAND-164438fbe48accb869f6b3804cb33fad34b8de9e9748cecedcb4c830e3d4716a

The system shall provide a separate historical data store for reporting\.

Sources and evidence:

Source: [evergreen\_reference\_2009\.txt](<../data/corpus/evergreen_reference_2009.txt>); document ID: DOC-e6aa9f8c6308ab748459f87b578a0df9df9c865b7911bac3686e865963b7af6f; normalized lines 171–171.

> - No historical reporting warehouse

### REQ-446 — Include Current Patron Mailing Addresses in Reports

- Internal key: REQ-e2db554d38f3a259cecbe1e6307b6a98451dedeb6b607ba8ac5cf996b5ca3114
- Type: functional
- Priority: P2
- Priority basis: inferred
- Priority rationale: This capability directly supports a stated outreach process; no explicit source priority is provided\.
- Originating candidates: CAND-f57fe321b939800cda35c43a17b8ffe76d6308432deffddc7b22f6b5583ffe1c

Reports shall include current mailing addresses for patrons to support outreach activities such as mailing postcards\.

Sources and evidence:

Source: [conversations/conv\_pines024\_inactive\_patrons\.eml](<../data/corpus/conversations/conv_pines024_inactive_patrons.eml>); document ID: DOC-705ab8a51bf22b7b619dae61bf8d2be1cf2487e749f13e7ac55fdde430357793; normalized lines 37–39.

> We use this for outreach - trying to re-engage patrons who haven't visited
> in a while\. We mail postcards to inactive patrons, so the report needs to
> include current mailing addresses\.

Source: [conversations/conv\_pines024\_inactive\_patrons\.eml](<../data/corpus/conversations/conv_pines024_inactive_patrons.eml>); document ID: DOC-705ab8a51bf22b7b619dae61bf8d2be1cf2487e749f13e7ac55fdde430357793; normalized lines 139–139.

> - Include current mailing addresses for outreach

### REQ-447 — Uncataloged Materials as Inventory in Transactions and Reports

- Internal key: REQ-e2eff6b1289d96bc472a9d3d168a8051671274c83c616d8b2facc3d0d52c74a4
- Type: functional
- Priority: P2
- Priority basis: inferred
- Priority rationale: This supports operational tracking and complete circulation reporting for a stated material category\.
- Originating candidates: CAND-38347359ecd64e6f3b5259ee4662a4064320da13a262c77b8d49d2e7625929c5

The system shall track uncataloged materials as inventory without requiring individual catalog records and shall include those materials in transaction counts, circulation statistics, and reports\.

Sources and evidence:

Source: [interview\_cataloging\_2009-05-08\.txt](<../data/corpus/interview_cataloging_2009-05-08.txt>); document ID: DOC-a79fab45108210e6bce7d92153dfcf055f2ef6b2cdab49a3f6f5717a3e35f29f; normalized lines 29–37.

> THOMAS: Well, one big area is uncataloged material\. At Augusta-Reed, we get
> large shipments of paperback books and children's board books that arrive
> without individual catalog records\. We need to be able to track these as
> inventory even though they're not fully cataloged\.
> 
> The requirements are: quick distribution \(we need to process these fast\),
> minimal branch labor \(we can't spend a lot of time per item\), and ability to
> identify how the material is being used\. We also need to count transactions
> and include them in circulation statistics and reports\.

### REQ-448 — Separate Last Circulation Date Field

- Internal key: REQ-e35ea609977c0d2a3d5fbfbc5159370bc498b31e12b22835dbfac2750e96099f
- Type: functional
- Priority: P2
- Priority basis: inferred
- Priority rationale: A separate last circulation field supports accurate circulation reporting\.
- Originating candidates: CAND-1d3d76e10504136345e256da383aa1d63e199b729b65196e3c778ef4ca11c116

The system shall provide last circulation date as a separate field for reporting\.

Sources and evidence:

Source: [evergreen\_reference\_2009\.txt](<../data/corpus/evergreen_reference_2009.txt>); document ID: DOC-e6aa9f8c6308ab748459f87b578a0df9df9c865b7911bac3686e865963b7af6f; normalized lines 201–201.

> - Ability to indicate last circulation date - not available as separate field

### REQ-449 — Report Error Diagnostics for Failed Reports

- Internal key: REQ-e3efb036940ae38a74331cd1264012393e1a642ee1aa7f844b5008c6197a2f8d
- Type: functional
- Priority: P2
- Priority basis: inferred
- Priority rationale: Detailed failure diagnostics substantially affect administration and problem resolution\.
- Originating candidates: CAND-9df1892823dbd97242e29618d71d67b7d47c32dac4c7eb78e7e0eb71d12390fa

The system shall provide high-level error reporting and low-level, query-specific feedback for administrators, including the table, field, and type of error when a report fails\.

Sources and evidence:

Source: [meeting\_tech\_subcommittee\_2009-06-30\.txt](<../data/corpus/meeting_tech_subcommittee_2009-06-30.txt>); document ID: DOC-e081aa7bd57bf5e59c75a8a86f592124757b74dff1ee0df4badc10c025092d96; normalized lines 110–116.

> 3\.4 ERROR REPORTING
> The system shall provide thorough high-level error reporting and feedback,
> and shall allow low-level query-specific feedback for administrators\.
> 
> "When a report fails, we need to know WHY," Robert said\. "Generic error messages
> like 'query failed' are useless\. We need specifics - which table, which field,
> what kind of error\."

### REQ-450 — Save Queries for Repeated Use

- Internal key: REQ-e5e63226521d5090fd23cb5fdfce274284d697110f0f9548135d6d10f80e46bf
- Type: functional
- Priority: P3
- Priority basis: inferred
- Priority rationale: Saved queries are useful for repeated reporting work but are not established as essential to basic operation\.
- Originating candidates: CAND-c68129e739b4c92aa50e9bec0220d181d11d2c1a903531983d35e63b4bd3096f

The system shall allow users to save queries for repeated use\.

Sources and evidence:

Source: [conversations/conv\_pines018\_item\_transfer\.eml](<../data/corpus/conversations/conv_pines018_item_transfer.eml>); document ID: DOC-a47eb1f11286ff9099687b72a901e4a6ed2455b431087c0742aa78583c5bd80a; normalized lines 7–7.

> - Save queries for repeated use

### REQ-451 — Prioritize Certain Types of Reports

- Internal key: REQ-e69392fbdb660afaa2585affc41e908523213a9e0695ba6d1de65de2737b5482
- Type: functional
- Priority: P3
- Priority basis: inferred
- Priority rationale: Report prioritization can improve operational convenience and scheduling, but the source does not establish that it is essential to basic operation\.
- Originating candidates: CAND-af93cfc45ae68c01a2efc96d2105648c520ed9611dc88a73ab05ba6e64909f7a

The system shall provide the ability to prioritize certain types of reports\.

Sources and evidence:

Source: [evergreen\_reference\_2009\.txt](<../data/corpus/evergreen_reference_2009.txt>); document ID: DOC-e6aa9f8c6308ab748459f87b578a0df9df9c865b7911bac3686e865963b7af6f; normalized lines 167–167.

> - No ability to prioritize certain types of reports

### REQ-452 — Geographic and Age Transaction Statistics

- Internal key: REQ-e786ef7078d004253869bd50b4eb7077b2556dcaceccf0e8b760647dbdf6e9e4
- Type: functional
- Priority: P2
- Priority basis: inferred
- Priority rationale: Geographic and age transaction statistics support important demographic analysis\.
- Originating candidates: CAND-1c7e195090fa0c733afe5d72b2fb565ae726c10cf21dbb23261c93c5302dc7c7

The system shall provide demographic statistics that include transactions by geographical regions and by age ranges\.

Sources and evidence:

Source: [survey\_results\_2009\.txt](<../data/corpus/survey_results_2009.txt>); document ID: DOC-aac7bceef7a883652805583e98ec513b6ae2e7951e2ecfa18722127b1f12a5c4; normalized lines 127–127.

> 7\. Demographic statistics include transactions by geographical regions and age

### REQ-453 — Privacy-Protected Transaction Archive per State Law

- Internal key: REQ-e7cf89b6ef5a4cba4902252400a32e9ed09d14155896fa0ff4a876cb70aa0962
- Type: functional
- Priority: P1
- Priority basis: inferred
- Priority rationale: The source identifies transaction retention as required for compliance and requires privacy protection, making this mandatory compliance functionality\.
- Originating candidates: CAND-e67f59422fc91d9411abb85fd19bb5ad9b6ac282aa2a98c8c943419c178853b7

The system shall archive transaction records in accordance with State Law while protecting patron privacy, retaining transaction data for the period required by State Law and not retaining personally identifiable information, while still providing useful demographic statistics\.

Sources and evidence:

Source: [email\_report\_features\.eml](<../data/corpus/email_report_features.eml>); document ID: DOC-d9e168e0c03903021bf9e636e1d8e5f56dfcb79cc110d3839e38175a7c54344e; normalized lines 31–33.

> 5\. TRANSACTION ARCHIVE: Transactions archived protecting patron privacy per
>    State Law, while providing useful demographic statistics\.
> 

Source: [email\_report\_features\.eml](<../data/corpus/email_report_features.eml>); document ID: DOC-d9e168e0c03903021bf9e636e1d8e5f56dfcb79cc110d3839e38175a7c54344e; normalized lines 73–75.

> Also, for the transaction archive - we need this for compliance\. State law
> requires us to retain transaction data for X years, but patron privacy means
> we can't keep personally identifiable information\.

Source: [email\_report\_features\.eml](<../data/corpus/email_report_features.eml>); document ID: DOC-d9e168e0c03903021bf9e636e1d8e5f56dfcb79cc110d3839e38175a7c54344e; normalized lines 113–114.

> 5\. TRANSACTION ARCHIVE: Archive with privacy protection per State Law\.
> 

### REQ-454 — Missing MARC Fields Report

- Internal key: REQ-e9ac467f7f798d1631dbbb0204c9c5d667add6f82e74d92fc43ced47aa0acaf4
- Type: functional
- Priority: P2
- Priority basis: inferred
- Priority rationale: The report is explicitly listed as a required report type; the source does not assign a priority\.
- Originating candidates: CAND-de58b8c437164bc93b4b4578e2fc3665089ebde96a731d654248585baf38870a

The system shall provide a report listing bibliographic records that are missing specified MARC fields\.

Sources and evidence:

Source: [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>); document ID: DOC-091180de9b2d4ea83267d989411ac89f415d4def3bbf7cd51651fb7fda8d8bf9; normalized lines 540–540.

> - Bib Records missing specific MARC fields

### REQ-455 — IntraPINES Loans by Facility Report

- Internal key: REQ-ea65a8ab239b0ed71a98a0d42b1e321f26841f296eba30e41151ece29387858a
- Type: functional
- Priority: P3
- Priority basis: inferred
- Priority rationale: This is a specific reporting capability and is not identified as essential to basic operation\.
- Originating candidates: CAND-357ef74055519c78e712f94b4a81eefdd6064a2c32e52de493a45ccd12a8c4fa

The system shall provide an IntraPINES Loans by Facility report\.

Sources and evidence:

Source: [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>); document ID: DOC-091180de9b2d4ea83267d989411ac89f415d4def3bbf7cd51651fb7fda8d8bf9; normalized lines 568–568.

> - IntraPINES Loans by Facility

### REQ-456 — Cross-Branch Comparison Reports

- Internal key: REQ-eaa5bc41986bdf9bf15d2098f529a34b840e38a20c8b02df9f56e9f5e6d4ff18
- Type: functional
- Priority: P2
- Priority basis: inferred
- Priority rationale: Cross-branch comparison is an important management capability, but the source does not establish it as essential to basic operation\.
- Originating candidates: CAND-c0b92045823be672ebe7726a1cd36d62fa756e7aa5ae70eb1a2bd58ba8cc131d

The system shall provide reports that compare data across branches\.

Sources and evidence:

Source: [meeting\_minutes/meeting\_2009-07-20\_minutes\.txt](<../data/corpus/meeting_minutes/meeting_2009-07-20_minutes.txt>); document ID: DOC-5ab1dd8bc97af3b1ab2e378495f0e0d75fd501fcc19f923c0d8fda831074281b; normalized lines 37–37.

>   - Need for cross-branch comparison reports

### REQ-457 — Separate Development and Training Environments

- Internal key: REQ-ec44a7ab77b20bde2aed2489d80e4f2d79779ec99ebaf3bfbf4494852dc775e4
- Type: nonfunctional
- Priority: P2
- Priority basis: inferred
- Priority rationale: Isolation protects production operations and supports safe development and training; no explicit source priority is supplied\.
- Originating candidates: CAND-fd23fe468d01937a1a67ba67ed2e1b6b899d4bee995cc7e44fa16cdab110c4f9

The system shall provide separate development and training environments so developers can test new reports and staff can practice running reports without affecting production\.

Sources and evidence:

Source: [interview\_sysadmin\_2009-05-10\.txt](<../data/corpus/interview_sysadmin_2009-05-10.txt>); document ID: DOC-b1738fd7a6de9498f19ede6747ba156ecb29ead86ad1c9a2768b53e862ece1a9; normalized lines 90–93.

> ROBERT: We definitely need separate environments\. Developers need a place to
> test new reports without affecting production\. And new staff members need a
> training environment where they can practice running reports without worrying
> about making mistakes\.

### REQ-458 — Patron Added Count by Month Report

- Internal key: REQ-ec99746c73ea325b9377fa69516b1e84635bc490e5e6d2cdd417932d624537a7
- Type: functional
- Priority: P3
- Priority basis: inferred
- Priority rationale: This is a useful statistical report and is not identified as essential to basic operation\.
- Originating candidates: CAND-9d9a05c21bb6fca74f17f3fc6b64e8e84056de6468e315b645b2601aad09a44e

The system shall provide a Patron Added Count by Month report\.

Sources and evidence:

Source: [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>); document ID: DOC-091180de9b2d4ea83267d989411ac89f415d4def3bbf7cd51651fb7fda8d8bf9; normalized lines 544–544.

> - Patron Added Count by Month

### REQ-459 — Staff Login Methods

- Internal key: REQ-ecbc769f1056fc694caf03cd44651294870989a7fdb0b0372ffb676fe218231a
- Type: functional
- Priority: P2
- Priority basis: inferred
- Priority rationale: Supporting both login methods is important for staff access and fallback operation, but no explicit priority is supplied\.
- Originating candidates: CAND-23c416876ecd9ce780494ec760d72d69f02a06364b3a2e456964b91d3457cfcd

The system shall support both streamlined staff login methods, such as card swipe, and traditional individual username/password login; streamlined login shall be optional and shall not be required for staff access\.

Sources and evidence:

Source: [email\_staff\_login\.eml](<../data/corpus/email_staff_login.eml>); document ID: DOC-64b10e94c42508c5aea1af877ec9d2fe34485b099b29994b8b1a76cadc55e8b3; normalized lines 18–22.

> However, we also need to support the traditional username/password method - not
> all staff may have ID cards, and we need a fallback\. The system should support
> BOTH methods - streamlined login \(e\.g\. card swipe\) AND traditional login
> \(individual login and password\)\. The streamlined method should be optional but
> available\.

### REQ-460 — Patron Count by Age Demographic

- Internal key: REQ-ed845281f30d5a1ad35502abcd90eb5302c896ba4bd48aabb8f55e59f48b98f2
- Type: functional
- Priority: P2
- Priority basis: inferred
- Priority rationale: Inferred as high priority because the evidence explicitly identifies this report as needed\.
- Originating candidates: CAND-848ebbec19c36e8ebee48b881f78c615995128fdc004b3c76e0b0e1890dc0746

The system shall provide Patron Count by Age Demographic reports\.

Sources and evidence:

Source: [evergreen\_reference\_2009\.txt](<../data/corpus/evergreen_reference_2009.txt>); document ID: DOC-e6aa9f8c6308ab748459f87b578a0df9df9c865b7911bac3686e865963b7af6f; normalized lines 154–154.

> - Patron Count by Age Demographic \(not available\)

### REQ-461 — Individual and Cumulative Checkout and Renewal Counts

- Internal key: REQ-ee2e7cfe007eeda5e1eaebe804e65e64436a08bae3fa68ecde19bddb975ab660
- Type: functional
- Priority: P2
- Priority basis: inferred
- Priority rationale: The source explicitly specifies detailed circulation counting needed for reporting; the source does not assign a priority\.
- Originating candidates: CAND-e18a7b6c276d016b8a349ba15fe4f59be90a257dce29dad76e8cfdd59d1c6145

The system shall count each checkout type individually and cumulatively, including staff checkout, self-checkout, staff renewal, self-checkout renewal, online renewal, and OPAC renewal\.

Sources and evidence:

Source: [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>); document ID: DOC-091180de9b2d4ea83267d989411ac89f415d4def3bbf7cd51651fb7fda8d8bf9; normalized lines 431–438.

> 12\.4 Types of Check-Out
> The system counts all types of check-out individually and cumulatively:
>   - staff check-out
>   - self check-out
>   - staff renewal
>   - self checkout renewal
>   - online renewal
>   - OPAC renewal

### REQ-462 — Detailed Payments Received Report

- Internal key: REQ-ee35ed4a1232c864f30d2df70acdc1e1750dbeab7685fcd4ffd533ce1edba04d
- Type: functional
- Priority: P2
- Priority basis: inferred
- Priority rationale: This is a specific financial reporting capability important to management reporting\.
- Originating candidates: CAND-37085161dec2e6b29610dd26689c9e2d08fbeab284a62e9498fc62a42e820102

The system shall provide a detailed report of forgiven, worked, and goods payments received\.

Sources and evidence:

Source: [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>); document ID: DOC-091180de9b2d4ea83267d989411ac89f415d4def3bbf7cd51651fb7fda8d8bf9; normalized lines 584–584.

> - Detailed Forgive, Work, and Goods Payments Received

### REQ-463 — Indicate Last Circulation Date in Item Reports

- Internal key: REQ-ee6eb9e9b5226aef379672a6fcdc30d5240e5c9a25af15f82908d72a4a4d5fc6
- Type: functional
- Priority: P3
- Priority basis: inferred
- Priority rationale: Provides useful item-report detail but is not essential to basic reporting\.
- Originating candidates: CAND-a6d87c309aafb53488bf13e94f82a25008b83a337b2c738bcb15d21f2f42cf8f

The system shall allow item reports to indicate the last circulation date\.

Sources and evidence:

Source: [survey\_results\_2009\.txt](<../data/corpus/survey_results_2009.txt>); document ID: DOC-aac7bceef7a883652805583e98ec513b6ae2e7951e2ecfa18722127b1f12a5c4; normalized lines 102–102.

>   - "Ability to indicate last circulation date on item reports"

### REQ-464 — Safe training environment without risking production data

- Internal key: REQ-eee70acaa10499ac4166451351ac8e306ee26c103653513651a0d8dbb90f9df8
- Type: nonfunctional
- Priority: P1
- Priority basis: inferred
- Priority rationale: Preventing experimentation from risking production data is a safety and data-protection concern\.
- Originating candidates: CAND-8c83e75be4a91be35e1d7cb0479f58aecc37f1c44bff8af359d64a909c6f8ed2

The training environment shall allow staff experimentation without risking production data\.

Sources and evidence:

Source: [meeting\_tech\_subcommittee\_2009-06-30\.txt](<../data/corpus/meeting_tech_subcommittee_2009-06-30.txt>); document ID: DOC-e081aa7bd57bf5e59c75a8a86f592124757b74dff1ee0df4badc10c025092d96; normalized lines 57–58.

> Katherine added: "And the training environment needs to be safe - staff should
> be able to experiment without risking production data\."

### REQ-465 — Check-In Counts by Individual Check-In Type

- Internal key: REQ-ef1d80f81aeb9f3593ccf2f674f9c52389c2232bbae655406da01de7c89f0fce
- Type: functional
- Priority: P2
- Priority basis: inferred
- Priority rationale: Supports operational analysis across circulation service methods\.
- Originating candidates: CAND-d84bd1c959ab64719c7ce6d9066186ddbc089dd72c1afbe5646847503dcc1b74

The system shall count each type of check-in individually and cumulatively, including book-drop, terminal, by-user, and self-service check-ins\.

Sources and evidence:

Source: [survey\_results\_2009\.txt](<../data/corpus/survey_results_2009.txt>); document ID: DOC-aac7bceef7a883652805583e98ec513b6ae2e7951e2ecfa18722127b1f12a5c4; normalized lines 114–116.

> 3\. All types of check-in counted individually and cumulatively: book-drop,
>    terminal, by user or self-service\.
> 

### REQ-466 — Historical Snapshot Bills Report

- Internal key: REQ-ef3ffc4360477da506e4e6425b314b838aa7fcb75b820b38cda49b4bcc065213
- Type: functional
- Priority: P2
- Priority basis: inferred
- Priority rationale: Historical bills reporting supports financial and management analysis over time\.
- Originating candidates: CAND-d9f03b82dd5394344fa58c81d70d1b2533c407f3cd5838e5c538d5df8edfdf9f

The system shall provide a snapshot bills report with historical data going back in time\.

Sources and evidence:

Source: [evergreen\_reference\_2009\.txt](<../data/corpus/evergreen_reference_2009.txt>); document ID: DOC-e6aa9f8c6308ab748459f87b578a0df9df9c865b7911bac3686e865963b7af6f; normalized lines 198–199.

> - Historical reporting warehouse - does not exist
> - Snapshot bills report going back in time - does not exist

### REQ-467 — Deletion Audit Table Query Interface

- Internal key: REQ-ef73c237684788b780936fdb29c0e7100bda45cf315bb857462f7e09f4e0e4b6
- Type: functional
- Priority: P2
- Priority basis: inferred
- Priority rationale: Querying deletion records supports operational oversight and troubleshooting, but no explicit priority is supplied\.
- Originating candidates: CAND-5ceb110c0418391617aca28c5e638f6d5f66d658cf379df9cb24a10012e66191

The system shall provide a report interface that can query the deletion or audit table\.

Sources and evidence:

Source: [conversations/conv\_pines022\_deletions\.eml](<../data/corpus/conversations/conv_pines022_deletions.eml>); document ID: DOC-7b8da7c05931fc99bc80d4a4bb0c8563e690e0c415b57f5ca1ae394462dc26c8; normalized lines 41–42.

> 3\. A report interface to query this audit table
> 

### REQ-468 — Log Denied Deletion Attempts

- Internal key: REQ-f0720e53615fb8b41462a35963377ccdb09d901b776d6e24ef9da2bdc0a1041a
- Type: functional
- Priority: P2
- Priority basis: inferred
- Priority rationale: Inferred as important security monitoring functionality; no explicit source priority is supplied\.
- Originating candidates: CAND-6f95be1136097dd3676b5540c9e1c90138178b67a7af50a56aecfd73141cb1f4

The system shall log attempted deletions that the system denies\.

Sources and evidence:

Source: [conversations/conv\_pines022\_deletions\.eml](<../data/corpus/conversations/conv_pines022_deletions.eml>); document ID: DOC-7b8da7c05931fc99bc80d4a4bb0c8563e690e0c415b57f5ca1ae394462dc26c8; normalized lines 92–93.

> Can we also track attempted deletions that were denied? That would tell
> us if someone is trying to delete things they shouldn't\.

### REQ-469 — Provide Circulation Count by Circ Modifier Report

- Internal key: REQ-f0c4dec7239ca9e4e6db319fa16b4fbf95a3573b3f1dc2e24897a46b06a1a049
- Type: functional
- Priority: P3
- Priority basis: inferred
- Priority rationale: Provides useful circulation analysis and addresses a documented incomplete capability\.
- Originating candidates: CAND-a79b15ef4e3f9237dc25342f8aacf1a15a6dc0279bd0a3492759f83682e33899

The system shall provide a Circulation Count by Circ Modifier report, completing or enhancing the partially available capability\.

Sources and evidence:

Source: [evergreen\_reference\_2009\.txt](<../data/corpus/evergreen_reference_2009.txt>); document ID: DOC-e6aa9f8c6308ab748459f87b578a0df9df9c865b7911bac3686e865963b7af6f; normalized lines 135–136.

> 4\.1 MISSING REPORT TYPES
> - Circulation Count by Circ Modifier \(partially available\)

### REQ-470 — Voter Registration Survey Report by Week

- Internal key: REQ-f0deff9c2294e2aec763ffe5f14e3314c9b0c025357a9b11292fe3c6956deb6c
- Type: functional
- Priority: P3
- Priority basis: inferred
- Priority rationale: Specific reporting capability not identified as essential\.
- Originating candidates: CAND-ccbd410d18c85bb72ff1403fb325c3b066aa72ccc18a5493f032300c728d1b15

The system shall provide a report showing voter registration survey response counts by week\.

Sources and evidence:

Source: [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>); document ID: DOC-091180de9b2d4ea83267d989411ac89f415d4def3bbf7cd51651fb7fda8d8bf9; normalized lines 555–555.

> - Voter Reg Survey Responses Count by Week

### REQ-471 — IntraPINES Loans by System Report

- Internal key: REQ-f183f04f55d29e8d4cf2d0a94ffdd2a082623a90bcddf40a6f1f4f1a1ce8b855
- Type: functional
- Priority: P2
- Priority basis: inferred
- Priority rationale: System-level loan reporting supports important inter-organization operational analysis\.
- Originating candidates: CAND-185a6e51901dd1473b33e9c58ba8c9f4b477bcb2ce144a441beb7d6a0fe119e6

The system shall provide an IntraPINES Loans by System report\.

Sources and evidence:

Source: [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>); document ID: DOC-091180de9b2d4ea83267d989411ac89f415d4def3bbf7cd51651fb7fda8d8bf9; normalized lines 567–567.

> - IntraPINES Loans by System

### REQ-472 — Side-by-Side Branch Comparison View

- Internal key: REQ-f1c98bbddf05406115de6d84228ce345f45f91c9ea781172a4ec56b687bf6505
- Type: functional
- Priority: P2
- Priority basis: inferred
- Priority rationale: Side-by-side branch comparison supports management analysis and identification of outliers\.
- Originating candidates: CAND-3b2af2fb4f37fc16c7548620d95de3e506f97e041b1a9e09c7bc447454436319

The system shall provide a comparison view showing each library's breakdown side by side\.

Sources and evidence:

Source: [conversations/conv\_pines016\_shelf\_space\.eml](<../data/corpus/conversations/conv_pines016_shelf_space.eml>); document ID: DOC-b507e8abe1ba7c996c1d86d688e90bcf2404694ec00528c8361f26dfc8bd82f1; normalized lines 84–88.

> I want this broken down per library AND per system\. Our directors review
> this data quarterly and need both views\.
> 
> Also, can we include a "comparison" view that shows each library's breakdown
> side by side? That would make it easy to spot outliers\.

### REQ-473 — Include Condition Notes in Missing and Damaged Reports

- Internal key: REQ-f204849fdbc1f4630bb2d3081320c2e4c4bd679fdd46b1b04a1847121c34b5eb
- Type: functional
- Priority: P3
- Priority basis: inferred
- Priority rationale: Condition notes provide useful diagnostic detail but are not shown to be essential to basic operation\.
- Originating candidates: CAND-4c589dc6a0daa45b91ff36ce6840b521c7a54ad0f4e867445a101801f2e50bda

The system shall include item condition notes, such as water damage or vandalism, in missing and damaged item reports\.

Sources and evidence:

Source: [conversations/conv\_pines019\_020\_missing\_intransit\.eml](<../data/corpus/conversations/conv_pines019_020_missing_intransit.eml>); document ID: DOC-b233b12122cae48b5821d685f6dc058d2d2e3cc8d7f77622fa4e7e55bddc5399; normalized lines 51–52.

> Also, can the report include item condition notes? Like "water damage" or
> "vandalism"? That helps us understand root causes\.

### REQ-474 — Accessible Help System for Assistive Technologies

- Internal key: REQ-f2244e790b412834b9f4cc3a456321c5719a8a053903f35831974228ee651f91
- Type: nonfunctional
- Priority: P1
- Priority basis: inferred
- Priority rationale: Accessible help is necessary for users relying on assistive technologies to use and understand the system\.
- Originating candidates: CAND-a29f0b67c664ade4075700b7bf2d7bcf3fa8245bc215c07ec4c130619d4848be

The help system and related outputs shall be accessible to screen readers and compatible with assistive technologies\.

Sources and evidence:

Source: [meeting\_tech\_subcommittee\_2009-06-30\.txt](<../data/corpus/meeting_tech_subcommittee_2009-06-30.txt>); document ID: DOC-e081aa7bd57bf5e59c75a8a86f592124757b74dff1ee0df4badc10c025092d96; normalized lines 107–108.

> Robert: "This has to be accessible too\. The help system needs to work with
> screen readers\."

### REQ-475 — Track Payments by Library or Branch

- Internal key: REQ-f245d9515e6c1a8335b36be5d371ce164c76e95657e1444a17d62379986658b7
- Type: functional
- Priority: P2
- Priority basis: inferred
- Priority rationale: Location-based payment reporting supports branch financial accountability; no explicit source priority is provided\.
- Originating candidates: CAND-f47d52a846ff1284a7220b4b60c1de90b2efe9ce24753370d8ee2b35bd56b7d6

The system shall track payments by branch so each branch can see payments collected at its location for end-of-month reporting\.

Sources and evidence:

Source: [email\_financial\_reports\.eml](<../data/corpus/email_financial_reports.eml>); document ID: DOC-8b6cfb3cf368b794d82567933f9c85062740814819b1e28b4837f6021cbcbee6; normalized lines 92–94.

> - Payments tracking by library is important for our end-of-month reports\. Each
>   branch needs to be able to see what payments were collected at their location\.
> 

Source: [email\_financial\_reports\.eml](<../data/corpus/email_financial_reports.eml>); document ID: DOC-8b6cfb3cf368b794d82567933f9c85062740814819b1e28b4837f6021cbcbee6; normalized lines 118–119.

>    and item records\. System tracks fines waived and payments made per library\.
>    Financial information can be updated easily\. A staff user can easily query

### REQ-476 — Voter Survey Responses Reporting Capability

- Internal key: REQ-f27f2affab23df0420adc0ff9e4833f353cd5994c641ef6f44174f65ed836ac0
- Type: functional
- Priority: P2
- Priority basis: inferred
- Priority rationale: The report is identified in the supplied reporting scope, but the source does not assign a formal priority level\.
- Originating candidates: CAND-077695bb41756743b2b58dcb80ef6d2858c3e901f6447b7d1cd4cd568af20149

The system shall provide Voter Survey Responses reporting capability\.

Sources and evidence:

Source: [evergreen\_reference\_2009\.txt](<../data/corpus/evergreen_reference_2009.txt>); document ID: DOC-e6aa9f8c6308ab748459f87b578a0df9df9c865b7911bac3686e865963b7af6f; normalized lines 157–157.

> - Voter Survey Responses \(not available\)

### REQ-477 — Reporting Data Relationships

- Internal key: REQ-f2b2c28b88d4b43310f55eb8418ac71c4c37976ec835f0f3ebf3c0571f377b96
- Type: functional
- Priority: P2
- Priority basis: inferred
- Priority rationale: Necessary for reports spanning core library entities and transactions\.
- Originating candidates: CAND-d3fd2ac63df270bf49a8e15e18edf42901d440f19f5180153ee6158089399086

The system shall maintain the relationships needed for reporting between bibliographic records and items through asset\.copy, items and circulation actions through patron\_id, patrons and money through debt records, and actors and circulation actions through the librarian link\.

Sources and evidence:

Source: [evergreen\_reference\_2009\.txt](<../data/corpus/evergreen_reference_2009.txt>); document ID: DOC-e6aa9f8c6308ab748459f87b578a0df9df9c865b7911bac3686e865963b7af6f; normalized lines 103–109.

> 3\.2 KEY RELATIONSHIPS
> - bibliographic\_record -&gt; item \(through asset\.copy\)
> - item -&gt; action\.circulation \(through circulation transactions\)
> - patron -&gt; action\.circulation \(through patron\_id\)
> - patron -&gt; money \(through debt records\)
> - actor -&gt; action\.circulation \(through librarian link\)
> 

### REQ-478 — Branch Capacity Interface

- Internal key: REQ-f316ec22a2a7a87ce60f2fbf46964094d078e89daf1060e04ccc374d17e3a719
- Type: functional
- Priority: P2
- Priority basis: inferred
- Priority rationale: A system-wide branch capacity view supports operational planning, although the supplied evidence does not define the capacity measure\.
- Originating candidates: CAND-8fd53c5372cfa94f98f06de016a84c25f21ce4b5f511db756b2809e0c5352a3c

The system shall provide an interface showing the capacity of all branches\.

Sources and evidence:

Source: [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>); document ID: DOC-091180de9b2d4ea83267d989411ac89f415d4def3bbf7cd51651fb7fda8d8bf9; normalized lines 333–335.

> 10\.2 System Capacity Interface
> The system should provide an interface showing the capacity of all branches\.
> 

### REQ-479 — Branch Sorting and Filtering by Region, Type, and Current Load

- Internal key: REQ-f3436ac1e95985f6e8b851214b890969ede14548ff8d723f5a4a4d7f4267f528
- Type: functional
- Priority: P2
- Priority basis: inferred
- Priority rationale: Branch analysis is important operational functionality, but the sources do not establish that it is essential for core operation\.
- Originating candidates: CAND-013dddfee8e530f720e1cec8caea828be2aff401f52c51a9fb5e2000e9c630e0

The system shall support sorting and filtering branches by region, library type, and current load\.

Sources and evidence:

Source: [conversations/conv\_pines015\_capacity\_interface\.eml](<../data/corpus/conversations/conv_pines015_capacity_interface.eml>); document ID: DOC-4acf2fdb375b86d49420e5743267e19b3f0af9ebe8bd764c1a88379aa9f5b662; normalized lines 67–68.

> I'd want to be able to sort and filter\. By region, by library type, by
> current load\.\.\. And export to CSV for the directors who want spreadsheets\.

Source: [conversations/conv\_pines015\_capacity\_interface\.eml](<../data/corpus/conversations/conv_pines015_capacity_interface.eml>); document ID: DOC-4acf2fdb375b86d49420e5743267e19b3f0af9ebe8bd764c1a88379aa9f5b662; normalized lines 87–88.

> - Sorting and filtering capabilities \(region, type, load\)
> - Trend data \(growth/shrink patterns\)

### REQ-480 — Required Data Retention for Financial and Audit Data

- Internal key: REQ-f38a510dae1618f355b641d6169156303b85e6a7f01a1aa92e6ba498d71ea3c4
- Type: nonfunctional
- Priority: P1
- Priority basis: inferred
- Priority rationale: Inferred as critical because the source requires compliance with retention obligations and identifies seven-year audit retention for some data\.
- Originating candidates: CAND-657aca844747054123a1fd421492ee631994e6473c818019285d64ceb4e486d0

The system shall enforce data-retention policies required by state and local requirements, including retaining applicable financial and audit data for 7 years where required\.

Sources and evidence:

Source: [email\_financial\_reports\.eml](<../data/corpus/email_financial_reports.eml>); document ID: DOC-8b6cfb3cf368b794d82567933f9c85062740814819b1e28b4837f6021cbcbee6; normalized lines 50–52.

> - On compliance - we need to ensure that data archiving follows state and local
>   requirements\. Some data needs to be retained for 7 years for audit purposes\.
>   The system needs to enforce retention policies\.

Source: [email\_financial\_reports\.eml](<../data/corpus/email_financial_reports.eml>); document ID: DOC-8b6cfb3cf368b794d82567933f9c85062740814819b1e28b4837f6021cbcbee6; normalized lines 112–115.

> 2\. COMPLIANCE:
>    All reports and data archiving must comply with standard accounting practice
>    and state, county, and municipal auditing requirements\.
> 

### REQ-481 — Record Data Specifications for Management Processes

- Internal key: REQ-f449b70934b5a2d0dd30ada53557fbe8ea2f8b3af91fccc9fc8f95b085b2b28c
- Type: nonfunctional
- Priority: P2
- Priority basis: explicitly specified
- Priority rationale: The source marks complete data specifications as High Priority, which maps to P2 under the supplied priority scale\.
- Originating candidates: CAND-042047faaf6cb5354ec24d7f6ded1ec29b5a9778d7355955d5b51e1f31c2bf42

The software developer shall provide complete data specifications for authority records, bibliographic records, order records, item records, hold/request records, and other records maintained or accessed by Management Processes\.

Sources and evidence:

Source: [meeting\_minutes/meeting\_2009-07-20\_minutes\.txt](<../data/corpus/meeting_minutes/meeting_2009-07-20_minutes.txt>); document ID: DOC-5ab1dd8bc97af3b1ab2e378495f0e0d75fd501fcc19f923c0d8fda831074281b; normalized lines 136–139.

> UD-1: The software developer shall provide complete data specifications for
>       authority records, bibliographic records, order records, item records,
>       hold/request records, and other records maintained or accessed by
>       Management Processes\.

### REQ-482 — Transaction Query Dimensions and Type Filters

- Internal key: REQ-f4610c736073a06114b4ccd46e3a66eff83e454e16117c0d0d36031fbdd5483d
- Type: functional
- Priority: P2
- Priority basis: inferred
- Priority rationale: Important operational reporting capability; not established as essential to basic operation\.
- Originating candidates: CAND-c8544ca0c414199e1b5c30bcaf22641939d19576b4ee2ef32a9a306bb9052cc3

The system shall support grouping and querying transactions by hour, terminal, branch, and system; transaction types shall include check-ins, check-outs, fines collected, and patron registrations; and users shall be able to query all transactions or filter by transaction type\.

Sources and evidence:

Source: [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>); document ID: DOC-091180de9b2d4ea83267d989411ac89f415d4def3bbf7cd51651fb7fda8d8bf9; normalized lines 420–423.

> 12\.2 Backroom Statistics Examples
> Transactions can be grouped by hour, terminal, branch, and system\. Transactions
> include check-ins, check-outs, fines collected, patron registrations, etc\., and
> can be queried by all transactions or by type of transaction\.

### REQ-483 — Email Report Delivery

- Internal key: REQ-f4ebd30a18f50a61a95b253cec02f0311c26b4d994453324bc4b2c7700ae36bb
- Type: functional
- Priority: P3
- Priority basis: inferred
- Priority rationale: Email delivery is a useful reporting convenience but is not essential to core operation\.
- Originating candidates: CAND-119b2191d10afac6808c3ea82a355becc29b8db56dbe3cc2abf40da44848c00c

The system shall deliver reports by email in addition to making them downloadable from the web interface\.

Sources and evidence:

Source: [evergreen\_reference\_2009\.txt](<../data/corpus/evergreen_reference_2009.txt>); document ID: DOC-e6aa9f8c6308ab748459f87b578a0df9df9c865b7911bac3686e865963b7af6f; normalized lines 79–79.

> - No email delivery \(reports can only be downloaded from the web interface\)

### REQ-484 — Reusable Saved Queries

- Internal key: REQ-f509cab4cabc2a0227c5aa9ca01c5c4d31de17142cd8919ce15afa79757c8a03
- Type: functional
- Priority: P2
- Priority basis: inferred
- Priority rationale: Saving and reusing queries supports recurring reporting work, but the source does not assign an explicit priority\.
- Originating candidates: CAND-360ad5fe9709f7bc9935576fef35e302bab68c444437c4f9f14e1f443886d17c

The system shall provide the ability to save and reuse queries\.

Sources and evidence:

Source: [survey\_results\_2009\.txt](<../data/corpus/survey_results_2009.txt>); document ID: DOC-aac7bceef7a883652805583e98ec513b6ae2e7951e2ecfa18722127b1f12a5c4; normalized lines 62–63.

>   - Ability to save and reuse queries: 73%
>   - Report queue visibility \(where my report is in the queue\): 68%

### REQ-485 — Circulation by Location and Patron County

- Internal key: REQ-f55c38372edcdb8c9ae8a0864ba093d4c0633a4bfa3ba99a13f56fa6306c21ee
- Type: functional
- Priority: P2
- Priority basis: inferred
- Priority rationale: This report provides useful location and demographic analysis and is identified as unavailable\.
- Originating candidates: CAND-228b6eee0a67fb7cd1e0698e2b493fa9c75c9aeace137a235cec77578c73a9c1

The system shall provide a circulation count report by circulation location, broken down by patron county\.

Sources and evidence:

Source: [evergreen\_reference\_2009\.txt](<../data/corpus/evergreen_reference_2009.txt>); document ID: DOC-e6aa9f8c6308ab748459f87b578a0df9df9c865b7911bac3686e865963b7af6f; normalized lines 139–139.

> - Circulation Count by Circ Location broken down by Patron County \(not available\)

### REQ-486 — Combined In-Transit Report

- Internal key: REQ-f5954718142f9cb4e0cd5f6a701b9a0007cb6a426a3dad34e25733046e8d5f02
- Type: functional
- Priority: P2
- Priority basis: inferred
- Priority rationale: A combined transit report materially supports front-line transfer work, but no explicit priority is supplied\.
- Originating candidates: CAND-5a7562025b68c460565f297950a247300989b019c4cc82637062ee8f35209a87

The system shall provide a single in-transit report that combines transit-to and transit-from information so front-line staff do not have to run two reports\.

Sources and evidence:

Source: [conversations/conv\_pines019\_020\_missing\_intransit\.eml](<../data/corpus/conversations/conv_pines019_020_missing_intransit.eml>); document ID: DOC-b233b12122cae48b5821d685f6dc058d2d2e3cc8d7f77622fa4e7e55bddc5399; normalized lines 34–35.

> And the report should merge transit-to and transit-from so front-line staff
> don't have to run two reports\.

Source: [conversations/conv\_pines019\_020\_missing\_intransit\.eml](<../data/corpus/conversations/conv_pines019_020_missing_intransit.eml>); document ID: DOC-b233b12122cae48b5821d685f6dc058d2d2e3cc8d7f77622fa4e7e55bddc5399; normalized lines 88–89.

>    X days \(X configurable\), per branch and per system\. The report merges
>    transit-to and transit-from into one report for ease of front-line staff\.

### REQ-487 — Date-Range Report Filtering with Period Comparison

- Internal key: REQ-f7867afd8b8cffa993911556e129df9faa3f10b0a069dcddad38a26072bacdaa
- Type: functional
- Priority: P2
- Priority basis: inferred
- Priority rationale: Date-range analysis supports collection decisions and seasonal analysis; the source does not assign a priority\.
- Originating candidates: CAND-dc7536fa423dce18119ad0f758d7f8f84144c4694e15d7d7fb626c74cb4a90a3

The system shall allow reports to be filtered by a date range, including comparison of periods such as Q1 and Q2 for shelf-space-utilization analysis\.

Sources and evidence:

Source: [conversations/conv\_pines016\_shelf\_space\.eml](<../data/corpus/conversations/conv_pines016_shelf_space.eml>); document ID: DOC-b507e8abe1ba7c996c1d86d688e90bcf2404694ec00528c8361f26dfc8bd82f1; normalized lines 51–56.

> I would need this at the system level for sure\. When I look at Twin Lakes
> as a whole, we might have too many romance novels in some branches and not
> enough in others\. Being able to redistribute based on data would help\.
> 
> Can we also filter by date range? Like, what was the shelf space utilization
> in Q1 vs\. Q2? Seasons matter for our collection\.

### REQ-488 — Change User Permissions by Updating Assigned Role

- Internal key: REQ-f7a464b669aad12a2c4e7832e6069f26bdfa83d8b98ce36d317c273b7dc1d4fb
- Type: functional
- Priority: P2
- Priority basis: inferred
- Priority rationale: Inferred as important security administration functionality; no explicit source priority is supplied\.
- Originating candidates: CAND-72ab73a9ea206b0e55e4c665e9f7bd0765e0ad7fe42dbebeb2d773fafa40a0d0

The system shall change a user's permissions by changing the user's assigned role rather than by modifying individual permissions\.

Sources and evidence:

Source: [email\_staff\_login\.eml](<../data/corpus/email_staff_login.eml>); document ID: DOC-64b10e94c42508c5aea1af877ec9d2fe34485b099b29994b8b1a76cadc55e8b3; normalized lines 69–72.

> Each of these should be a role that can be assigned to staff members\. The system
> should make it easy to administer these roles - changing someone's permissions
> should be a simple matter of changing their role assignment, not modifying
> individual permissions\.

### REQ-489 — Deletion Audit Trail Retaining Deleted Records Traceability

- Internal key: REQ-f86672270562466057f799a11a2a7e180a257767c7df6fa9de49224b677fdaa3
- Type: functional
- Priority: P1
- Priority basis: inferred
- Priority rationale: The requirement preserves accountability for destructive actions; P1 is inferred from its audit and record-protection importance\.
- Originating candidates: CAND-46498c1e35b55ed80755bb9305b2dc48a04acf284f7dc39812411c7f530ea4b1

The system shall log and retain deletions so that deleted records remain traceable through an audit trail\.

Sources and evidence:

Source: [conversations/conv\_pines022\_deletions\.eml](<../data/corpus/conversations/conv_pines022_deletions.eml>); document ID: DOC-7b8da7c05931fc99bc80d4a4bb0c8563e690e0c415b57f5ca1ae394462dc26c8; normalized lines 35–36.

> This is actually a good idea from an auditing standpoint\. Currently,
> Evergreen does not log deletions - once something is deleted, it's gone\.

### REQ-490 — Process Searches and Reports During Open Hours

- Internal key: REQ-f9465ad48c7c802e7a16dd763ff61a32a190fe5b92c88920e48380f860057b80
- Type: nonfunctional
- Priority: P1
- Priority basis: inferred
- Priority rationale: Inferred as critical because the evidence requires reporting during open hours without disruption to other system functions\.
- Originating candidates: CAND-877c03879babd7c202432ef6f4fdcb24b0fe568ccbf39937ab565760d7d2fd73

The system shall allow searches and reports to be processed during open hours without disrupting other system functions\.

Sources and evidence:

Source: [meeting\_minutes/meeting\_2009-07-20\_minutes\.txt](<../data/corpus/meeting_minutes/meeting_2009-07-20_minutes.txt>); document ID: DOC-5ab1dd8bc97af3b1ab2e378495f0e0d75fd501fcc19f923c0d8fda831074281b; normalized lines 70–71.

>       desirable that searches and reports can be processed during open hours
>       without disrupting other system functions\.

### REQ-491 — Staff Report Filter Restrictions

- Internal key: REQ-fb2f3effd8f915ef09a758f91efb601fb30c8c4d3281e40fcfdbde3923397c99
- Type: functional
- Priority: P2
- Priority basis: inferred
- Priority rationale: Administrative control over report access is important governance functionality, but the source does not assign a formal priority level\.
- Originating candidates: CAND-096a96cdd6eafa945bc393456f7ac69755ce369e2e9edacef55a54c923deb260

The system shall allow administrators to limit which report filters staff members can use\.

Sources and evidence:

Source: [evergreen\_reference\_2009\.txt](<../data/corpus/evergreen_reference_2009.txt>); document ID: DOC-e6aa9f8c6308ab748459f87b578a0df9df9c865b7911bac3686e865963b7af6f; normalized lines 86–86.

> - No ability to limit which filters staff can use

### REQ-492 — Branch Capacity and Collection Distribution Analysis

- Internal key: REQ-fb3c6e949e2ae17e0b363be5e4b80b6c84aab64725449615d4a92e9ab0194126
- Type: functional
- Priority: P2
- Priority basis: inferred
- Priority rationale: Capacity and collection-distribution analysis supports important branch planning; the source does not define the capacity measure\.
- Originating candidates: CAND-1ed92c8fd785efae8290fe19300a5ec86f30e8e91bd575b3b8a3c0d7319c539d

Management Processes shall provide tools to analyze branch capacity and support optimal distribution of the collection across branches\.

Sources and evidence:

Source: [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>); document ID: DOC-091180de9b2d4ea83267d989411ac89f415d4def3bbf7cd51651fb7fda8d8bf9; normalized lines 87–87.

>   - Analyzing branch capacity and optimal distribution of the collection\.

### REQ-493 — Display Null Values in Report Outputs

- Internal key: REQ-fba42c528f92883d601f4755dd305b9d3cc4f33f34cf071f3217eb9bef1ca595
- Type: functional
- Priority: P1
- Priority basis: inferred
- Priority rationale: Preventing silent exclusion of records is essential to accurate and trustworthy reporting\.
- Originating candidates: CAND-9ef1edbd32466031d633522508aa503fc2d146708111ba2276e1b4402282d913

The system shall include records with missing values in report outputs and shall display null values rather than silently excluding those records\.

Sources and evidence:

Source: [conversations/conv\_pines023\_patron\_characteristics\.eml](<../data/corpus/conversations/conv_pines023_patron_characteristics.eml>); document ID: DOC-d2b26a6e7678ca4e82bfa7bb06566f329dea692ea22e8987b516fa8bc98c544b; normalized lines 95–98.

> One consideration: if patrons haven't provided optional fields, they'll
> show up as null\. We should include them in the report \(with null values\)
> rather than excluding them, because excluding data silently can lead to
> misleading results\.

Source: [conversations/conv\_pines023\_patron\_characteristics\.eml](<../data/corpus/conversations/conv_pines023_patron_characteristics.eml>); document ID: DOC-d2b26a6e7678ca4e82bfa7bb06566f329dea692ea22e8987b516fa8bc98c544b; normalized lines 121–121.

> - Null values should be included in results

### REQ-494 — Predefined Core Library Reports by Category

- Internal key: REQ-fe09c2b761b0d55259c7fb9e8ee0a506fda11a319aa135bdf1e9b311d335c6c7
- Type: functional
- Priority: P2
- Priority basis: inferred
- Priority rationale: Inferred as substantial core reporting functionality; no explicit source priority is supplied\.
- Originating candidates: CAND-6719a2bb02e4df05838aaaa0ec06f92750d7271fdfebe4c2d23cf66bcadf35d4

The system shall provide predefined reports covering Circulation, Items, Bib Records, Patrons, and Bills, including the report types listed in the source\.

Sources and evidence:

Source: [evergreen\_reference\_2009\.txt](<../data/corpus/evergreen_reference_2009.txt>); document ID: DOC-e6aa9f8c6308ab748459f87b578a0df9df9c865b7911bac3686e865963b7af6f; normalized lines 44–71.

> 2\.2 CANNED REPORTS
> Pre-defined reports available in Evergreen 1\.4\.0\.4:
> 
> CIRCULATION:
> - Checkout Count
> - Renewals Count
> - Non-Cataloged Count
> - Circulation Count by Shelving Location
> 
> ITEMS:
> - Items Added Count
> - Items Deleted Count
> - Items Currently Checked Out
> - Items Overdue by X Days
> - List of Items with Missing Status
> 
> BIB RECORDS:
> - Bib Records Count
> - Bib Records with No Volumes Attached
> 
> PATRONS:
> - Patron Count
> - Patron Count by Home Library
> 
> BILLS:
> - Bills Currently Owed by Patrons
> - Detailed Payments Received
> - Aged Debt

### REQ-495 — Record Cleanup Utility for Volume, Copy, and Orphan Bibliographic Records

- Internal key: REQ-fe39af0b4a06f57b550918d4ad8dc601c6ca7993a0cb349147922ec010c181ef
- Type: functional
- Priority: P2
- Priority basis: inferred
- Priority rationale: The capability addresses a stated operational cleanup need, but the sources do not assign a formal priority level or specify whether the method is automated or manual\.
- Originating candidates: CAND-072c8a50a819c0bca3645205db02fb307bf3ceba3f377fb1d668e9f7c525b9e4, CAND-0e812cf02094db283a6a00b74e3acb324fa33ecc60b874f5bd3359943df82f8b

The system shall provide a quick and effective method to delete volume records together with their copy or item entries and to delete bibliographic records that have no items attached\.

Sources and evidence:

Source: [conversations/conv\_pines021\_item\_purging\.eml](<../data/corpus/conversations/conv_pines021_item_purging.eml>); document ID: DOC-74ccbb6ac77183c0d1b34b1e79ed8fcbbfb4e7525cb33798c3af832fed733ad8; normalized lines 17–18.

> 4\. We also need a quick way to delete volume entries along with copy
>    entries, and delete records with no items attached\.

Source: [conversations/conv\_pines021\_item\_purging\.eml](<../data/corpus/conversations/conv_pines021_item_purging.eml>); document ID: DOC-74ccbb6ac77183c0d1b34b1e79ed8fcbbfb4e7525cb33798c3af832fed733ad8; normalized lines 78–80.

> Also, "quick effective method of deleting volume entries along with copy
> entries, as well as records with no items attached" - this is more of a
> cleanup utility\. Should it be automated or manual?

Source: [conversations/conv\_pines021\_item\_purging\.eml](<../data/corpus/conversations/conv_pines021_item_purging.eml>); document ID: DOC-74ccbb6ac77183c0d1b34b1e79ed8fcbbfb4e7525cb33798c3af832fed733ad8; normalized lines 133–134.

> - Provide a quick effective method for deleting volume entries along with
>   copy entries, as well as records with no items attached

Source: [interview\_cataloging\_2009-05-08\.txt](<../data/corpus/interview_cataloging_2009-05-08.txt>); document ID: DOC-a79fab45108210e6bce7d92153dfcf055f2ef6b2cdab49a3f6f5717a3e35f29f; normalized lines 85–87.

> There also needs to be a quick, effective method for deleting volume entries
> along with copy entries, as well as records with no items attached\. Right now,
> cleaning up these orphaned records takes forever\.

### REQ-496 — Run Reports by Branch and System Aggregate

- Internal key: REQ-fe3a9c6ab76dbcc714c2854e545190e84f5ef4cd34007c8395e132c33e0d52d8
- Type: functional
- Priority: P2
- Priority basis: inferred
- Priority rationale: Both local and aggregate views are important to the stated management use case; no explicit source priority is supplied\.
- Originating candidates: CAND-fde005d3da42fc059c16efef159b86fd353eed93fe509617196831ae235559bc

Reports shall be runnable per branch and for the aggregate system so branch managers can view local conditions and compare them with the system average\.

Sources and evidence:

Source: [conversations/conv\_pines016\_shelf\_space\.eml](<../data/corpus/conversations/conv_pines016_shelf_space.eml>); document ID: DOC-b507e8abe1ba7c996c1d86d688e90bcf2404694ec00528c8361f26dfc8bd82f1; normalized lines 32–40.

> This is the "shelf space report" we've been talking about\. The idea is:
> for each genre and format of material, compare:
> 1\. Percentage of total circulations
> 2\. Percentage of the collection
> 3\. Percentage of total shelf space
> 
> The report should be able to run per library and per system\. This way branch
> managers can see their local situation AND see how they compare to the system
> average\.

### REQ-497 — Customizable Report Categories

- Internal key: REQ-fff58904251da36eee185075862137c5e3de74e68126098296d007a5c077d37f
- Type: functional
- Priority: P3
- Priority basis: inferred
- Priority rationale: Customizable categories provide useful flexibility for different libraries but are not identified as essential to basic operation\.
- Originating candidates: CAND-61f8d523ae63b026cca8c024ec246d9e78ce360b3bea61aac99884d6a8f75bfe

The system shall allow the categories used in reports to be customized so different libraries can use different breakdowns\.

Sources and evidence:

Source: [conversations/conv\_pines014\_material\_volume\.eml](<../data/corpus/conversations/conv_pines014_material_volume.eml>); document ID: DOC-f10d646016479a881ae8ff4ab4043844ee55a671d71f1943623db3fbb5589d8a; normalized lines 53–55.

> I second this request\. At Twin Lakes we need this for our quarterly
> assessment\. Can we make the categories customizable? Different libraries
> might want different breakdowns\.

Source: [conversations/conv\_pines014\_material\_volume\.eml](<../data/corpus/conversations/conv_pines014_material_volume.eml>); document ID: DOC-f10d646016479a881ae8ff4ab4043844ee55a671d71f1943623db3fbb5589d8a; normalized lines 101–102.

> - Number of board books
> - Other customizable categories

## Glossary

| Preferred term | Definition | Aliases |
| --- | --- | --- |
| branch | A library location for which reports or operational data may be provided\. | library, location |
| canned report | A predefined report supplied with the product and runnable for specified standard data ranges\. | pre-defined report |
| capacity | The capacity measure displayed for a branch; the supplied evidence does not resolve whether this means items, shelf space, a configured limit, circulation volume, or processing capacity\. | None |
| Global System Administrator | A consortium-level administrative role with system-wide access and responsibility for software changes, configurations, and consortium-wide statistical reports\. | Global Admin |
| item | A physical copy or volume associated with a bibliographic record\. | copy, volume |
| MARC field | A field within a MARC bibliographic record that can be selected for reporting\. | bibliographic field |
| Online Public Access Catalog | The OPAC module used for public catalog access\. | OPAC |
| patron characteristic | A patron attribute used to filter or group reporting results, such as age range, home branch, or preferred language\. | patron attribute |
| query | A saved or executed request for data used to produce or filter reporting results\. | search |
| report | A system-produced presentation or query result containing requested library data\. | reporting output |
| report queue | The ordered set of reports waiting to run or currently running\. | queue |
| role | A security assignment used to administer a user's permissions\. | security role |
| streamlined login | A staff login method such as a card reader or card swipe that identifies a user more conveniently than manually entering credentials\. | card-reader login, card-swipe login |
| transit | The state or movement of an item between library locations\. | in transit |

## Blacklist

Merged duplicates are retained through lineage and are not rejections.

### BL-064819c97e5b44bc574695be8df5ed803f221d600d9baa91a48f717461d3a2ed

- Original candidates: CAND-4c2295e24c9a4efee38b6f1664c8b76a5a47f43febfb323d9c159ec9e04bd2ad
- Reason for rejection: The evidence describes a tedious current manual process but does not establish a normative requirement to automate it\.
- Related retained requirement: None

Original statement:

Automate the generation of the shelf space vs\. usage report to eliminate the current manual process of pulling reports and creating spreadsheets\.

Source: [conversations/conv\_pines016\_shelf\_space\.eml](<../data/corpus/conversations/conv_pines016_shelf_space.eml>); document ID: DOC-b507e8abe1ba7c996c1d86d688e90bcf2404694ec00528c8361f26dfc8bd82f1; normalized lines 21–22.

> Currently I pull reports manually and make spreadsheets\. It's tedious\.
> 

### BL-34bbf122c5373716fa79c8449057e594239b0604dbd9c886daace463aeab4d37

- Original candidates: CAND-a19370a09100fe5ec7da9d12e9223e2c659bfdda1084292beed07fadc9fb4bc7
- Reason for rejection: This statement describes a requirements-development planning decision to use an existing draft as a foundation, rather than a testable system behavior or quality requirement\.
- Related retained requirement: None

Original statement:

The working group shall adapt the King County / Galecia Group draft Software Requirements Specification as a foundation and reference for PINES requirements\.

Source: [meeting\_minutes/meeting\_2009-03-15\_minutes\.txt](<../data/corpus/meeting_minutes/meeting_2009-03-15_minutes.txt>); document ID: DOC-defef992db2ae0e10167fd94902eac93f82c59c4c070df030ca2f77811082818; normalized lines 29–33.

> Katherine explained that King County Library System \(WA\) had previously worked
> with Galecia Group to develop a comprehensive Software Requirements Specification
> for a reports interface\. PINES staff decided to use that as a foundation and
> adapt it for our specific needs\. She mentioned that Lori Ayre and Lucien Kress
> from Galecia Group had been contacted and were willing to share their draft\.

### BL-35de33ac6d6ab0c602755875cf09fc500060ca13cba88c753e98c8718f568676

- Original candidates: CAND-f464a642aa3eb4304c1fddf8107852a6ea93d3f21f1f72f7d44537a3353b560a
- Reason for rejection: The candidate mandates a separate reporting database or replica as one architectural implementation\. The supporting evidence identifies this as a missing or possible architectural element, while the supported requirement is non-disruptive report processing during open hours; the evidence does not justify mandating this implementation\.
- Related retained requirement: REQ-081

Original statement:

Use a separate reporting database or replica for reporting \(do not run reports directly on the production database\)\.

Source: [evergreen\_reference\_2009\.txt](<../data/corpus/evergreen_reference_2009.txt>); document ID: DOC-e6aa9f8c6308ab748459f87b578a0df9df9c865b7911bac3686e865963b7af6f; normalized lines 181–182.

> 4\.3 MISSING ARCHITECTURAL ELEMENTS
> - No separate reporting database/replica \(reports run on production database\)

### BL-3ce8879572a3989134353ab97f452e095bde136b3822690401d3ebbce626a9e1

- Original candidates: CAND-04698cbc5aec87aa9e7db0464fe0bb1afcb1bfa83babed8863524d59e3166e7a
- Reason for rejection: The evidence lists record types as available for reporting but does not establish a normative requirement to expose all listed types through reporting\.
- Related retained requirement: None

Original statement:

Support reporting on the following record types: bibliographic\_record, item, patron, action\_circulation, action\_hold, money, and actor\.

Source: [evergreen\_reference\_2009\.txt](<../data/corpus/evergreen_reference_2009.txt>); document ID: DOC-e6aa9f8c6308ab748459f87b578a0df9df9c865b7911bac3686e865963b7af6f; normalized lines 92–101.

> 3\.1 RECORD TYPES
> The following record types are available for reporting:
> 
> - bibliographic\_record: Title, author, ISBN, publication info, subjects, etc\.
> - item: Call number, barcode, location \(copy location\), status, etc\.
> - patron: Name, address, library, patron type, etc\.
> - action\_circulation: Checkout, checkout, renewal, holds, etc\.
> - action\_hold: Hold requests
> - money: Fines, payments, credits, etc\.
> - actor: Staff accounts and permissions

### BL-540e8d81f81a9fe0dfbbc152311defdfb96c6068ced4e115943c512889b002e8

- Original candidates: CAND-9b7719f52f9dfc9ba40da744cf266d1f96bd63c391b273188a9cf3b05d84e3ac
- Reason for rejection: The source describes the listed bibliographic\_record fields as a sample of available fields, not as a normative requirement that all listed fields must be included in reportable fields\.
- Related retained requirement: None

Original statement:

Include the listed bibliographic\_record fields in reportable fields \(id, fingerprint, scan\_timestamp, record\_type, edition, language, ISBN, ISSN, UPC, EAN, publisher\_name, publication\_date, place\_of\_publication, physical\_description\)\.

Source: [evergreen\_reference\_2009\.txt](<../data/corpus/evergreen_reference_2009.txt>); document ID: DOC-e6aa9f8c6308ab748459f87b578a0df9df9c865b7911bac3686e865963b7af6f; normalized lines 110–115.

> 3\.3 AVAILABLE FIELDS \(SAMPLE\)
> For bibliographic\_record:
> - id, fingerprint, scan\_timestamp, record\_type,
>   edition, language, ISBN, ISSN, UPC, EAN, publisher\_name,
>   publication\_date, place\_of\_publication, physical\_description
> 

### BL-78815fecb94419832347379cdf26990b687396db596cf8fe48c7716b39f46852

- Original candidates: CAND-42931ba7b4a798cd6e8a0748f0004bbf9fd813a3cf85f4cdd1abd7d85b5ac405
- Reason for rejection: The supplied evidence describes features of an existing report-writer interface rather than establishing a normative requirement that the open-template capability must provide all of those features\.
- Related retained requirement: None

Original statement:

Provide a web-based report writer interface that allows staff to create custom reports with drag-and-drop field selection, basic filtering and sorting, multiple output formats \(CSV, HTML, sometimes Excel\), and the ability to save and reuse report definitions\.

Source: [evergreen\_reference\_2009\.txt](<../data/corpus/evergreen_reference_2009.txt>); document ID: DOC-e6aa9f8c6308ab748459f87b578a0df9df9c865b7911bac3686e865963b7af6f; normalized lines 28–36.

> 2\.1 REPORT WRITER INTERFACE
> Evergreen includes a report writer that allows staff to create custom reports
> using a web-based interface\. Key features:
> 
> - Drag-and-drop field selection
> - Basic filtering and sorting
> - Multiple output formats \(CSV, HTML, sometimes Excel\)
> - Ability to save and reuse report definitions
> 

### BL-8400f7fc1f1a2b9e103fdfe6fcc476ecc36232a3d351620bee3505d35715be56

- Original candidates: CAND-767814106d103b59453a37b0d3c7dc6d5196394decf7f71f3535af4615aa8f77
- Reason for rejection: The source expresses a preference for retaining the main relational database and avoiding denormalized reporting schemas because of synchronization concerns, but does not establish this implementation preference as a mandatory stakeholder requirement\.
- Related retained requirement: None

Original statement:

The reporting system must operate with the main relational database and should not require denormalized reporting schemas that create synchronization issues\.

Source: [interview\_sysadmin\_2009-05-10\.txt](<../data/corpus/interview_sysadmin_2009-05-10.txt>); document ID: DOC-b1738fd7a6de9498f19ede6747ba156ecb29ead86ad1c9a2768b53e862ece1a9; normalized lines 68–72.

> ROBERT: We're using PostgreSQL now, which is a fully relational database\.
> That's good - it means we can write complex joins\. The reporting system needs
> to work with the relational structure, not fight against it\. Some systems try
> to use denormalized reporting schemas, but that creates sync issues\. I'd
> prefer to keep everything in the main relational database\.

### BL-88b0028e607a9ed4212ef37a173114a0dbd56065774fa05ccaccbf495b06faaa

- Original candidates: CAND-102aae98141e1991cf5d52036011d20a3d55c6be8eb9966faa7b795b167ec51f
- Reason for rejection: The evidence presents crowded displays, grouping, filtering, and technical investigation as considerations or possible approaches, not as an adopted mandatory requirement with defined behavior\.
- Related retained requirement: None

Original statement:

Design the interface to handle scalability and technical constraints for displaying a large number of locations \(documented example: 286 locations\); consider grouping and filtering to manage crowded displays\.

Source: [conversations/conv\_pines015\_capacity\_interface\.eml](<../data/corpus/conversations/conv_pines015_capacity_interface.eml>); document ID: DOC-4acf2fdb375b86d49420e5743267e19b3f0af9ebe8bd764c1a88379aa9f5b662; normalized lines 49–51.

> One consideration: with 286 locations, the overview might get crowded\.
> Maybe we should group by system/region? Or allow filtering?
> 

Source: [conversations/conv\_pines015\_capacity\_interface\.eml](<../data/corpus/conversations/conv_pines015_capacity_interface.eml>); document ID: DOC-4acf2fdb375b86d49420e5743267e19b3f0af9ebe8bd764c1a88379aa9f5b662; normalized lines 91–91.

> Robert will look into technical constraints around displaying 286 locations\.

### BL-9dd95e5f91b5856b0b5e116e2b9c59ff20dbb5d5f32f175d1b0d2127d2959ee3

- Original candidates: CAND-714142e9197454f5dc652ded888dc1ab211db92edb8431666c270b23e1dc563f
- Reason for rejection: The source presents read-only reporting replicas as one alternative implementation approach alongside background queuing; it does not establish replicas as a required user or system capability\.
- Related retained requirement: None

Original statement:

The system should support the use of read-only reporting replicas to offload reporting queries from the production database so that reporting does not disrupt other system functions\.

Source: [interview\_sysadmin\_2009-05-10\.txt](<../data/corpus/interview_sysadmin_2009-05-10.txt>); document ID: DOC-b1738fd7a6de9498f19ede6747ba156ecb29ead86ad1c9a2768b53e862ece1a9; normalized lines 41–44.

> need to make sure reports can be queued and processed in the background\. Or we
> need read-only reporting replicas\. The key requirement is that searches and
> reports can be processed during open hours without disrupting other system
> functions\.

### BL-a79a77491bd0a1c62f6945ff57b4182b2ad0dc0f7d9a794d572d7d32eddcc28b

- Original candidates: CAND-068edd78715a677bae6f520dfe6a26790234a6d83be9ac1caeb8ea71729c9e0b
- Reason for rejection: The evidence lists patron fields but does not establish a normative requirement to expose every listed field in reports\.
- Related retained requirement: None

Original statement:

Include the listed patron fields in reportable fields \(id, barcode, opac \(visible fields\), family\_lib \(home library\), usr\_grp \(patron type\), em \(email\), address lines, city, state, zip \(postal code\), birth\_date, create\_date\)\.

Source: [evergreen\_reference\_2009\.txt](<../data/corpus/evergreen_reference_2009.txt>); document ID: DOC-e6aa9f8c6308ab748459f87b578a0df9df9c865b7911bac3686e865963b7af6f; normalized lines 122–126.

> For patron:
> - id, barcode, opac \(visible fields\), family\_lib \(home library\),
>   usr\_grp \(patron type\), em \(email\),
>   address lines, city, state, zip \(postal code\),
>   birth\_date, create\_date

### BL-b0753906a8c56e9549fce2e1145813f32c7a84613f251f06e85c13bf1ecb9022

- Original candidates: CAND-8a2f45578690d2aedb9abbfc7d561848791dcbd1c02031976dadce741579345f, CAND-93532a5895e89f1317557ba03954fafa75bf3440d3574827cfac312ec49d242b
- Reason for rejection: These candidates prescribe a database trigger and specific audit-table fields as implementation details\. The supplied evidence describes them as what would be needed to implement the capability, but does not establish the trigger or fields as mandatory stakeholder requirements\.
- Related retained requirement: None

Original statement:

Implement a database trigger that logs deletions to an audit table\.<br><br>The audit table must include fields: record\_type, record\_id, deleted\_by, deleted\_at, and location\.

Source: [conversations/conv\_pines022\_deletions\.eml](<../data/corpus/conversations/conv_pines022_deletions.eml>); document ID: DOC-7b8da7c05931fc99bc80d4a4bb0c8563e690e0c415b57f5ca1ae394462dc26c8; normalized lines 38–41.

> To implement this, we'd need:
> 1\. A trigger in the database that logs deletions to an audit table
> 2\. Fields: record\_type, record\_id, deleted\_by, deleted\_at, location
> 3\. A report interface to query this audit table

Source: [conversations/conv\_pines022\_deletions\.eml](<../data/corpus/conversations/conv_pines022_deletions.eml>); document ID: DOC-7b8da7c05931fc99bc80d4a4bb0c8563e690e0c415b57f5ca1ae394462dc26c8; normalized lines 39–41.

> 1\. A trigger in the database that logs deletions to an audit table
> 2\. Fields: record\_type, record\_id, deleted\_by, deleted\_at, location
> 3\. A report interface to query this audit table

### BL-c5c63137a22c3781fdc29870be0803874d6a720c32ee9a4409505348aa3112ab

- Original candidates: CAND-cde722d821d44c2360fc6a9c760fb44feaf7ebb73ff12a46b460f0830ba5aecf, CAND-d23954eea79d762ce2298ca8cbaa2cb60ea57646033d6b0d0e7b3f76fb8d4304
- Reason for rejection: These statements describe enterprise context and possible reliance on enterprise infrastructure rather than a specific system behavior or mandatory system quality\. The evidence does not establish them as requirements imposed on this system\.
- Related retained requirement: None

Original statement:

Management Processes are part of an enterprise-level Library Automation System\.<br><br>Management Processes are part of an enterprise-level Library Automation System and may rely on enterprise infrastructure such as redundant servers, backup systems, and network connectivity\.

Source: [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>); document ID: DOC-091180de9b2d4ea83267d989411ac89f415d4def3bbf7cd51651fb7fda8d8bf9; normalized lines 201–202.

> AS-1: Management Processes are part of an enterprise-level Library Automation
>       System\.

Source: [meeting\_tech\_subcommittee\_2009-06-30\.txt](<../data/corpus/meeting_tech_subcommittee_2009-06-30.txt>); document ID: DOC-e081aa7bd57bf5e59c75a8a86f592124757b74dff1ee0df4badc10c025092d96; normalized lines 121–125.

> AS-1: Management Processes are part of an enterprise-level Library Automation
> System\.
> 
> Robert: "This means we can rely on the infrastructure - redundant servers,
> backup systems, network connectivity\."

### BL-ccc9bb549882435fe39254a14774e1ee80750cf9d87685e257702179b6a0dac4

- Original candidates: CAND-8cefcc1fac462fb78e75a740a5cf5dd17f999040f9a94353d69faee03957eb24
- Reason for rejection: The cited evidence lists item fields in the context of reportable data structures and does not establish a normative requirement to expose every listed field\. Retaining this candidate as a mandatory requirement would overstate the supplied evidence\.
- Related retained requirement: None

Original statement:

Include the listed item fields in reportable fields \(id, barcode, label, copy\_number, location \(copy\_location\), status \(acq status\), circ\_modifier, call\_number, purchase\_date, purchase\_price, shelving\_location, age\_hold\_protect, reserve\_id\)\.

Source: [evergreen\_reference\_2009\.txt](<../data/corpus/evergreen_reference_2009.txt>); document ID: DOC-e6aa9f8c6308ab748459f87b578a0df9df9c865b7911bac3686e865963b7af6f; normalized lines 116–120.

> For item:
> - id, barcode, label, copy\_number, location \(copy\_location\),
>   status \(acq status\), circ\_modifier, call\_number,
>   purchase\_date, purchase\_price, shelving\_location,
>   age\_hold\_protect, reserve\_id

### BL-d1fcde3b797d70bd2d5087398a864800bc7ad3ab4111847738cdb4a2e046948f

- Original candidates: CAND-526d13257600229e4c02c037eaf29a9bbb3a88c18ace74b9c1616546e22ea7bb
- Reason for rejection: The evidence presents avoiding denormalization as a strong technical recommendation rather than a mandatory stakeholder system behavior or constraint\.
- Related retained requirement: None

Original statement:

The design should avoid denormalization for reporting \(strong recommendation against denormalization\)\.

Source: [meeting\_tech\_subcommittee\_2009-06-30\.txt](<../data/corpus/meeting_tech_subcommittee_2009-06-30.txt>); document ID: DOC-e081aa7bd57bf5e59c75a8a86f592124757b74dff1ee0df4badc10c025092d96; normalized lines 36–39.

> "I strongly recommend against denormalization for reporting," Robert said\.
> "Maintaining sync between a reporting warehouse and the live database creates
> more problems than it solves\. Modern SQL databases can handle complex analytical
> queries if they're written properly\."

## Unresolved issues

### Source ambiguities requiring clarification

#### ISSUE-4a8e7b4bf185ec2a2f43705368de61ba92d7878a06fe0e3155200827c83437b4 (OS7)

Requirements: REQ-019, REQ-328

Candidates: CAND-ce4e56e22d58b576bb17bf7430d70a3130b29a76322c122f5d8b99fcd8c69826, CAND-d79cf16557191fa22451a45abaf6d3d9c8df88ab8b3fa2e4cf6e0177e25b5380

The supplied unresolved conflict remains: the requirements address the same report-delivery address-book capability but differ on whether it is mandatory or optional\. The evidence does not resolve that decision\.

Requested action: Disclose the conflict and obtain stakeholder clarification on whether the address book is required or optional; do not choose a business decision without evidence\.

Source: [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>); document ID: DOC-091180de9b2d4ea83267d989411ac89f415d4def3bbf7cd51651fb7fda8d8bf9; normalized lines 626–627.

> - Ability to enter email addresses for report to be sent to - would be great to
>   have an address book of regularly used addresses

Source: [evergreen\_reference\_2009\.txt](<../data/corpus/evergreen_reference_2009.txt>); document ID: DOC-e6aa9f8c6308ab748459f87b578a0df9df9c865b7911bac3686e865963b7af6f; normalized lines 174–174.

> - No address book for report delivery

#### ISSUE-9643db05464cf6ad97b8c5bfa5cc2e8b208ba04b8862962dc1957c0e2220b661 (OS7)

Requirements: REQ-303, REQ-403

Candidates: CAND-feac7279a16874f96776f98fd95775d52879b3e9b8a203c0736e4895936b3960, CAND-ffc4099894dab9631579d30b9d3be3f70b16ecf621010888bb568c779a723e51

The supplied unresolved conflict remains: the all-branch capacity interface depends on a capacity measure, and the evidence lists competing measures without selecting one\.

Requested action: Disclose the unresolved capacity definition and obtain stakeholder clarification before specifying the measure\. Do not select or imply an alternative without evidence\.

Source: [conversations/conv\_pines015\_capacity\_interface\.eml](<../data/corpus/conversations/conv_pines015_capacity_interface.eml>); document ID: DOC-4acf2fdb375b86d49420e5743267e19b3f0af9ebe8bd764c1a88379aa9f5b662; normalized lines 3–7.

> As a branch manager, I need to see the capacity of all branches in our
> system, not just my own\. When we're deciding where to move items or
> allocate resources, it helps to see the big picture\.
> 
> Is there a way to see an overview of all branches' capacity?

Source: [conversations/conv\_pines015\_capacity\_interface\.eml](<../data/corpus/conversations/conv_pines015_capacity_interface.eml>); document ID: DOC-4acf2fdb375b86d49420e5743267e19b3f0af9ebe8bd764c1a88379aa9f5b662; normalized lines 52–56.

> Also, what specific metrics define "capacity"? Is it:
> - Number of items vs\. shelf space?
> - Number of physical items vs\. a configured limit?
> - Circulation volume vs\. processing capacity?
> 

Source: [conversations/conv\_pines015\_capacity\_interface\.eml](<../data/corpus/conversations/conv_pines015_capacity_interface.eml>); document ID: DOC-4acf2fdb375b86d49420e5743267e19b3f0af9ebe8bd764c1a88379aa9f5b662; normalized lines 57–57.

> Need to nail this down before building the interface\.

### Quality defects remaining after the revision limit

#### ISSUE-02cb6ac8ef1e3b0aaee16f8d0d016960ddcc53731f4d1e40323d7fa5b7561c1c (OS3)

Requirements: REQ-069, REQ-445

Candidates: CAND-164438fbe48accb869f6b3804cb33fad34b8de9e9748cecedcb4c830e3d4716a, CAND-e73112df4c4e1e104d9691ddaf67a7996e0f09e1b85cc72e61c7fed5d276b0de

Both requirements specify historical reporting through a reporting warehouse/data store\. They duplicate the same historical-reporting capability, although other requirements may separately describe date-range behavior\.

Requested action: Consolidate these into one historical reporting requirement, retaining the supported ability to retrieve data for a specified date or date range\.

Source: [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>); document ID: DOC-091180de9b2d4ea83267d989411ac89f415d4def3bbf7cd51651fb7fda8d8bf9; normalized lines 656–657.

> - Ability to have historical reporting - a reporting warehouse such that data
>   can be acquired on a given date or date range

Source: [evergreen\_reference\_2009\.txt](<../data/corpus/evergreen_reference_2009.txt>); document ID: DOC-e6aa9f8c6308ab748459f87b578a0df9df9c865b7911bac3686e865963b7af6f; normalized lines 171–171.

> - No historical reporting warehouse

#### ISSUE-176c634cf7102d7b846122ce2f29790c70f685ccd68c0726fc45571ebe2befba (OS3)

Requirements: REQ-014, REQ-132, REQ-133, REQ-238, REQ-263

Candidates: CAND-014cd73d14dd417db704dbc7e60d78d59534bd8bc38f2e1eda9e9aac965124b9, CAND-202972b16179a87374aa98fe9b4ef5390df65be8f54196a9a71c2e8543426407, CAND-8f79679d7c9152728fa6b7ab88b4930af8d60c41eb21c6363f24b7133fcb58a5, CAND-9232a3279103eae4acab816cf83f390ee00d3e93d8ee9f6d9f86842f468a9db6, CAND-bb5b03e98522452b8d99e3b3e5f1e0ba2b10dc527aea5c9363ff1e5f95e94552

These requirements repeat the shelf-space utilization/comparison report: comparing circulation share, collection share, and shelf-space share by genre and format\. The per-library/per-system scope in REQ-133 is an added detail of the same report, not a separate report capability\. The current set fragments and repeats one feature\.

Requested action: Consolidate the overlapping requirements into one shelf-space report requirement, preserving the genre/format metrics and the supported per-library and per-system scope; keep any genuinely distinct date-filtering or estimation behavior separate\.

Source: [conversations/conv\_pines016\_shelf\_space\.eml](<../data/corpus/conversations/conv_pines016_shelf_space.eml>); document ID: DOC-b507e8abe1ba7c996c1d86d688e90bcf2404694ec00528c8361f26dfc8bd82f1; normalized lines 1–6.

> Question for the group: How do I figure out if I'm using my shelf space
> efficiently? I need something that shows me, for each genre and format:
> - What percentage of total circulations it has
> - What percentage of the collection it is
> - What percentage of total shelf space it occupies
> 

Source: [conversations/conv\_pines016\_shelf\_space\.eml](<../data/corpus/conversations/conv_pines016_shelf_space.eml>); document ID: DOC-b507e8abe1ba7c996c1d86d688e90bcf2404694ec00528c8361f26dfc8bd82f1; normalized lines 98–106.

> Great discussion everyone\. Summarizing the Shelf Space Report requirement:
> 
> The system should provide, for each genre and format of material, the ability
> to compare:
> - The percentage of total circulations
> - The percentage of the collection
> - The percentage of total shelf space
> 
> The report should be available per library and per system\.

Source: [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>); document ID: DOC-091180de9b2d4ea83267d989411ac89f415d4def3bbf7cd51651fb7fda8d8bf9; normalized lines 336–343.

> 10\.3 Shelf Space Report
> For each genre and format of material, ability to compare:
>   - The percentage of total circulations
>   - The percentage of the collection
>   - The percentage of total shelf space
> 
> The report should be able to run per library and per system\.
> 

Source: [interview\_cataloging\_2009-05-08\.txt](<../data/corpus/interview_cataloging_2009-05-08.txt>); document ID: DOC-a79fab45108210e6bce7d92153dfcf055f2ef6b2cdab49a3f6f5717a3e35f29f; normalized lines 100–105.

> 1\. The shelf space report is important for collection management\. For each
>    genre and format, I need to compare:
>    - Percentage of total circulations
>    - Percentage of the collection
>    - Percentage of total shelf space
>    This helps me decide where to allocate resources\.

Source: [meeting\_minutes/meeting\_2009-07-20\_minutes\.txt](<../data/corpus/meeting_minutes/meeting_2009-07-20_minutes.txt>); document ID: DOC-5ab1dd8bc97af3b1ab2e378495f0e0d75fd501fcc19f923c0d8fda831074281b; normalized lines 52–52.

>   - Shelf space utilization reports are important

#### ISSUE-25521240808de23b9992a566a0e120cf3d7eb30c18cde07e7894e74c60d1ddb8 (OS6)

Requirements: REQ-027, REQ-045, REQ-076, REQ-281

Candidates: CAND-2b5558f3fc6e1eb53479f4dec04000a56b2204ca28322c2b925339a8fc2eda8b, CAND-5529179bb446f31d0b366c23743f0decc38ba0eca4383169bfb4591892cdca6e, CAND-ed9641d456143ab968495db7ebff977a362658fbfb083c72630d9a4b0d5182c0, CAND-fae7c1b6bb14749f9bd236a1111e847138a52bacd7925f28671ae4e4e0a3f354

Priority metadata does not consistently follow the supplied scale and original priority markings\. The original specification marks the consortium-scale requirement, web-or-Windows access, and complete data specifications High Priority, which maps to P2\. REQ-045 and REQ-027 assign P1 and mark priority inferred; REQ-281 and REQ-076 mark priority inferred despite explicit source priority evidence\.

Requested action: Set the consortium-scale requirements to P2 with priority\_inferred=false; retain the web-or-Windows requirement at P2 but set priority\_inferred=false; set REQ-076 to P2 with priority\_inferred=false\. Give rationales that cite the original High Priority markings and their mapping to P2\.

Source: [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>); document ID: DOC-091180de9b2d4ea83267d989411ac89f415d4def3bbf7cd51651fb7fda8d8bf9; normalized lines 126–127.

> OE-1: The system must support a library consortium with 286 locations, 17 million
>       annual circulations, and purchasing/processing over 900,000 items per year\.

Source: [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>); document ID: DOC-091180de9b2d4ea83267d989411ac89f415d4def3bbf7cd51651fb7fda8d8bf9; normalized lines 126–130.

> OE-1: The system must support a library consortium with 286 locations, 17 million
>       annual circulations, and purchasing/processing over 900,000 items per year\.
>       It is highly desirable that searches and reports can be processed during
>       open hours without disrupting other system functions\.
>       \[\* High Priority\]

Source: [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>); document ID: DOC-091180de9b2d4ea83267d989411ac89f415d4def3bbf7cd51651fb7fda8d8bf9; normalized lines 135–136.

> OE-3: The system must be accessible through a web browser or a Windows-compatible
>       client\.

Source: [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>); document ID: DOC-091180de9b2d4ea83267d989411ac89f415d4def3bbf7cd51651fb7fda8d8bf9; normalized lines 135–137.

> OE-3: The system must be accessible through a web browser or a Windows-compatible
>       client\.
>       \[\* High Priority\]

Source: [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>); document ID: DOC-091180de9b2d4ea83267d989411ac89f415d4def3bbf7cd51651fb7fda8d8bf9; normalized lines 176–179.

> UD-1: The developer must provide complete data specifications for authority
>       records, bibliographic records, order records, item records, hold/request
>       records, and other records maintained or accessed by the Management
>       Processes\.

Source: [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>); document ID: DOC-091180de9b2d4ea83267d989411ac89f415d4def3bbf7cd51651fb7fda8d8bf9; normalized lines 176–180.

> UD-1: The developer must provide complete data specifications for authority
>       records, bibliographic records, order records, item records, hold/request
>       records, and other records maintained or accessed by the Management
>       Processes\.
>       \[\* High Priority\]

#### ISSUE-33c1f4ed183b1416d63e318f95198a4ac6d9ab6e0180bcec8d304c77f26fe858 (OS3)

Requirements: REQ-012, REQ-139, REQ-422

Candidates: CAND-8817d2fe09b0632e6a2738ff06836dc4ff1ba348ad96a5d67d3588c3864256ce, CAND-89f83065ae1742a1bf1677e89beba3078f3a05a6c9e521b56167ec6f95834de1, CAND-c44959e9d1d15c61674532cb0eff5d5a9621844f7e7f38426a672c65c60d463f

All three requirements state that Management Processes must use a fully relational database backend\. They are semantically duplicate constraints\.

Requested action: Consolidate these into one relational-database requirement and preserve the supported wording about working with the relational structure\.

Source: [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>); document ID: DOC-091180de9b2d4ea83267d989411ac89f415d4def3bbf7cd51651fb7fda8d8bf9; normalized lines 153–153.

> CO-1: The system must use a fully relational database back-end\. \[\* High Priority\]

Source: [meeting\_minutes/meeting\_2009-07-20\_minutes\.txt](<../data/corpus/meeting_minutes/meeting_2009-07-20_minutes.txt>); document ID: DOC-5ab1dd8bc97af3b1ab2e378495f0e0d75fd501fcc19f923c0d8fda831074281b; normalized lines 106–108.

> CO-1: Management Processes shall use a fully relational database back-end\.
>       \[Discussion: Evergreen already uses PostgreSQL\. We need to ensure our
>       reporting layer works properly with the relational structure\.\]

Source: [meeting\_tech\_subcommittee\_2009-06-30\.txt](<../data/corpus/meeting_tech_subcommittee_2009-06-30.txt>); document ID: DOC-e081aa7bd57bf5e59c75a8a86f592124757b74dff1ee0df4badc10c025092d96; normalized lines 31–34.

> Robert confirmed that the system must use a fully relational database back-end\.
> He noted that PostgreSQL is the current choice for PINES and it meets this
> requirement\. The reporting system must work WITH the relational structure,
> not against it\.

#### ISSUE-414500ab82656ab94bf13b3fb20b44c7bb126ad445bdd67874264c8c85376234 (OS7)

Requirements: REQ-249

Candidates: CAND-8a9fcb99b42bc663f32a410c3e22694d275a797a4b95a0992bce133cf02c4037

The requirement adds providing or integrating WorldCat functionality\. The source says the last-copy report helps catalogers update WorldCat entries; it does not require the reporting system to integrate with or provide WorldCat functionality\.

Requested action: Limit the requirement to providing last-copy information that assists catalogers in updating WorldCat, unless a separate source explicitly requires WorldCat integration\.

Source: [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>); document ID: DOC-091180de9b2d4ea83267d989411ac89f415d4def3bbf7cd51651fb7fda8d8bf9; normalized lines 383–385.

> status to another\. The system should provide a last copy report that singles
> out a library system's last copies, to assist catalogers who need to edit
> WorldCat entries\. The system should provide a quick effective method of

Source: [interview\_cataloging\_2009-05-08\.txt](<../data/corpus/interview_cataloging_2009-05-08.txt>); document ID: DOC-a79fab45108210e6bce7d92153dfcf055f2ef6b2cdab49a3f6f5717a3e35f29f; normalized lines 80–83.

> And the last copy report is CRITICAL\. This singles out a library system's last
> copies, to assist catalogers who need to edit WorldCat entries\. Last month, we
> almost deleted our last copy of a rare book before someone remembered to check
> WorldCat\. If we had a report like this, it would save us from that situation\.

Source: [interview\_cataloging\_2009-05-08\.txt](<../data/corpus/interview_cataloging_2009-05-08.txt>); document ID: DOC-a79fab45108210e6bce7d92153dfcf055f2ef6b2cdab49a3f6f5717a3e35f29f; normalized lines 125–125.

> - The last copy report and WorldCat integration are critical

#### ISSUE-4601fd935115b6142a4f53b253f155952e30b8d4e5aeaec121e5e31bc06899d0 (OS3)

Requirements: REQ-218, REQ-262, REQ-365, REQ-415

Candidates: CAND-0eac9bd1b3990e377378abff6a437d8c1a802b4fc006b424f9eab55526732ef5, CAND-20788446eb843450003516c57df8e1e72c9b4d3c086c0e70a31c8fa9338dbd7d, CAND-3d4dd0a7b7ba5877aba682afa820bdc7fb1e32db02e66281ab2256bd353fe16a, CAND-e6357108ed68dbac76984d51c4c380ca77361e00bb400a736fbd7b0a43b24b1c

These requirements overlap on open-template reporting and, in some entries, the three reporting interfaces\. REQ-415 and REQ-365 already cover the open-template capability, while REQ-218 and REQ-262 restate it more generally\.

Requested action: Consolidate the overlapping interface requirements while retaining the distinct supported details for canned, on-demand, and open-template reporting and the open-template filtering/display attributes\.

Source: [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>); document ID: DOC-091180de9b2d4ea83267d989411ac89f415d4def3bbf7cd51651fb7fda8d8bf9; normalized lines 595–603.

> 15\.1 Three Interfaces
> Three interfaces are needed:
>   a\) Canned reports - generic reports set to run by the individual either ASAP
>      or recurring
>   b\) Noncanned or On Demand Reports - preset but have the ability to edit
>      selection criteria and display options
>   c\) Open Template Reporting - all attributes associated with circulation,
>      items, patrons, bills, and bibs to select from for filtering and display
> 

Source: [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>); document ID: DOC-091180de9b2d4ea83267d989411ac89f415d4def3bbf7cd51651fb7fda8d8bf9; normalized lines 615–618.

> 15\.4 Open Template Reporting
> Open template would have all attributes associated with say circulation,
> patrons, items, bills, and bibs to select from for filtering and the same
> attributes for displaying\.

Source: [evergreen\_reference\_2009\.txt](<../data/corpus/evergreen_reference_2009.txt>); document ID: DOC-e6aa9f8c6308ab748459f87b578a0df9df9c865b7911bac3686e865963b7af6f; normalized lines 195–196.

> - Three interfaces \(canned, on-demand, open template\) - only basic canned exists
> - Open Template Reporting - does not exist

Source: [evergreen\_reference\_2009\.txt](<../data/corpus/evergreen_reference_2009.txt>); document ID: DOC-e6aa9f8c6308ab748459f87b578a0df9df9c865b7911bac3686e865963b7af6f; normalized lines 196–196.

> - Open Template Reporting - does not exist

#### ISSUE-48634ce025cbe78018799f171400e0dbb1d05c46cdc01b85787cb951ffc5de8b (OS3)

Requirements: REQ-112, REQ-130, REQ-240, REQ-341, REQ-407, REQ-474

Candidates: CAND-305233fb98b5e408bac226e8caa51a64bf48c6c730f5fb6e23f51a906d108d64, CAND-8859d15565740cee359ee3d053a7581b23fdc5055e744b63ce68a133616ef023, CAND-9fe2d71f0e6f1d6abbaefd186b12757a25042d052b624ad566921b83c366ee2d, CAND-a29f0b67c664ade4075700b7bf2d7bcf3fa8245bc215c07ec4c130619d4848be, CAND-a3ff94c9dd49a977120652f5f0c189848736bb1712930ebddda528a7a9d60945, CAND-e6412b0ca42a6d9f6226689adb8800cb150f5d721ba08bf5b7b5c51702aadd7f

These entries repeat the accessibility obligation for Management Processes and the reporting interface, including assistive-technology support and Section 508 compliance\. The scope differences do not justify maintaining multiple overlapping general accessibility requirements\.

Requested action: Consolidate the overlapping accessibility requirements into a clear system-level requirement that preserves mandatory Section 508 compliance and the explicitly listed assistive-technology support; retain a separate interface-specific requirement only if it adds distinct, supported behavior\.

Source: [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>); document ID: DOC-091180de9b2d4ea83267d989411ac89f415d4def3bbf7cd51651fb7fda8d8bf9; normalized lines 144–146.

> OE-5: The system must be accessible with screen-reading software, screen-
>       magnification software, and other assistive technology programs designed
>       to increase accessibility\.

Source: [evergreen\_reference\_2009\.txt](<../data/corpus/evergreen_reference_2009.txt>); document ID: DOC-e6aa9f8c6308ab748459f87b578a0df9df9c865b7911bac3686e865963b7af6f; normalized lines 188–188.

> - No accessibility support for report interface

Source: [interview\_sysadmin\_2009-05-10\.txt](<../data/corpus/interview_sysadmin_2009-05-10.txt>); document ID: DOC-b1738fd7a6de9498f19ede6747ba156ecb29ead86ad1c9a2768b53e862ece1a9; normalized lines 56–56.

> ROBERTY: This is non-negotiable\. As a public institution, we MUST comply with

Source: [interview\_sysadmin\_2009-05-10\.txt](<../data/corpus/interview_sysadmin_2009-05-10.txt>); document ID: DOC-b1738fd7a6de9498f19ede6747ba156ecb29ead86ad1c9a2768b53e862ece1a9; normalized lines 56–60.

> ROBERTY: This is non-negotiable\. As a public institution, we MUST comply with
> Section 508 accessibility requirements\. The system needs to work with:
>   - Screen readers like JAWS and NVDA
>   - Screen magnification software like ZoomText
>   - Other assistive technology programs

Source: [meeting\_minutes/meeting\_2009-07-20\_minutes\.txt](<../data/corpus/meeting_minutes/meeting_2009-07-20_minutes.txt>); document ID: DOC-5ab1dd8bc97af3b1ab2e378495f0e0d75fd501fcc19f923c0d8fda831074281b; normalized lines 95–100.

> OE-5: Management Processes shall be accessible with screen-reading software,
>       screen-magnification software, and other software programs designed to
>       increase accessibility\.
>       \[Discussion: Susan emphasized this is a legal requirement for public
>       institutions\. We need to support JAWS, NVDA, ZoomText, and other
>       assistive technologies\. Section 508 compliance is mandatory\.\]

#### ISSUE-6f7eed63d88f3855a2ce1f3aeb29b6fb44d13479fca196d748a29dd7714fce74 (OS3)

Requirements: REQ-215, REQ-221, REQ-265

Candidates: CAND-26296051cb9a5061293ad3ff67a1c69578ce0b638a90671b91a4f8309d8cab05, CAND-55ea828708012ebe9e6b43418f4ff583cbb65dc59e307904f51c5ec985bf00ff, CAND-99e6efc589c27a60d93e8f01243ed44004c4377af40e2dc911fa7279d620d5cd

These requirements overlap on standards-compliant HTML for the system's web output\. Their scope differs in wording, but the underlying quality constraint is duplicated across entries\.

Requested action: Consolidate these into one standards-compliant HTML requirement covering the applicable web interface, help, and report output; retain additional accessibility markup only where explicitly supported\.

Source: [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>); document ID: DOC-091180de9b2d4ea83267d989411ac89f415d4def3bbf7cd51651fb7fda8d8bf9; normalized lines 155–156.

> CO-2: The system must produce standards-compliant HTML output for web-based
>       components\.

Source: [meeting\_minutes/meeting\_2009-07-20\_minutes\.txt](<../data/corpus/meeting_minutes/meeting_2009-07-20_minutes.txt>); document ID: DOC-5ab1dd8bc97af3b1ab2e378495f0e0d75fd501fcc19f923c0d8fda831074281b; normalized lines 110–112.

> CO-2: Management Processes shall produce standards-compliant HTML\.
>       \[Discussion: All web output needs to be valid HTML\. This affects report
>       display, help system, and any web-based UI components\.\]

Source: [meeting\_tech\_subcommittee\_2009-06-30\.txt](<../data/corpus/meeting_tech_subcommittee_2009-06-30.txt>); document ID: DOC-e081aa7bd57bf5e59c75a8a86f592124757b74dff1ee0df4badc10c025092d96; normalized lines 41–47.

> 2\.2 HTML COMPLIANCE
> The system must produce standards-compliant HTML\. This was discussed in the
> context of the web-based interface, the help system, and report output\.
> 
> "We need to make sure all HTML output validates against W3C standards,"
> Robert noted\. "This isn't just about looks - it's about compatibility with
> different browsers and assistive technologies\."

#### ISSUE-75152969f0faa45d51d04d5cb76fc6a2bc8a6c68772ef41f19b58ce25cd0b2e3 (OS3)

Requirements: REQ-027, REQ-045

Candidates: CAND-5529179bb446f31d0b366c23743f0decc38ba0eca4383169bfb4591892cdca6e, CAND-fae7c1b6bb14749f9bd236a1111e847138a52bacd7925f28671ae4e4e0a3f354

Both requirements specify the same consortium workload: 286 locations, 17 million annual circulations, and more than 900,000 items purchased or processed annually\.

Requested action: Consolidate the duplicate scale requirements into one capacity requirement, retaining the stated workload figures\.

Source: [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>); document ID: DOC-091180de9b2d4ea83267d989411ac89f415d4def3bbf7cd51651fb7fda8d8bf9; normalized lines 126–127.

> OE-1: The system must support a library consortium with 286 locations, 17 million
>       annual circulations, and purchasing/processing over 900,000 items per year\.

Source: [meeting\_minutes/meeting\_2009-07-20\_minutes\.txt](<../data/corpus/meeting_minutes/meeting_2009-07-20_minutes.txt>); document ID: DOC-5ab1dd8bc97af3b1ab2e378495f0e0d75fd501fcc19f923c0d8fda831074281b; normalized lines 66–69.

> OE-1: Management Processes must support the needs of a large, multiple-system
>       library consortium\. Specifically, the system must support a library
>       consortium with 286 locations, 17 million annual circulations,
>       purchasing and processing over 900,000 items per year\. It is highly

#### ISSUE-7b8ced2f4b9e274827e199f35712726ff9b8c21a0f11150bd606fc077f80feb2 (OS3)

Requirements: REQ-281, REQ-437

Candidates: CAND-2b5558f3fc6e1eb53479f4dec04000a56b2204ca28322c2b925339a8fc2eda8b, CAND-6f5236be44966ed2c699a62259d4144e6748ff7fb65d465edc6536420ef3f150

Both requirements specify access through a web browser or a Windows-compatible client\. The duplicate entries also carry inconsistent priority inference metadata; the original specification explicitly labels this requirement High Priority\.

Requested action: Consolidate the access-mode requirements and use the priority metadata supported by the original specification: P2 with priority inferred set to false\.

Source: [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>); document ID: DOC-091180de9b2d4ea83267d989411ac89f415d4def3bbf7cd51651fb7fda8d8bf9; normalized lines 135–136.

> OE-3: The system must be accessible through a web browser or a Windows-compatible
>       client\.

Source: [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>); document ID: DOC-091180de9b2d4ea83267d989411ac89f415d4def3bbf7cd51651fb7fda8d8bf9; normalized lines 135–137.

> OE-3: The system must be accessible through a web browser or a Windows-compatible
>       client\.
>       \[\* High Priority\]

Source: [meeting\_minutes/meeting\_2009-07-20\_minutes\.txt](<../data/corpus/meeting_minutes/meeting_2009-07-20_minutes.txt>); document ID: DOC-5ab1dd8bc97af3b1ab2e378495f0e0d75fd501fcc19f923c0d8fda831074281b; normalized lines 82–86.

> OE-3: Management Processes shall be accessible through a web-browser or a
>       Windows-compatible client\.
>       \[Discussion: This is critical - some libraries prefer browser-based
>       access \(no client install\), others prefer the dedicated client for
>       better performance\.\]

#### ISSUE-9342e631b51f7556539a204ba39e42093693ddd3cec2191670566d85612eea93 (OS3)

Requirements: REQ-268, REQ-277, REQ-380

Candidates: CAND-46753964acc52b2ba175eee48ab89e67d52b4722a1be8a81019bd22c679332c0, CAND-7d196bae1fe78f8b24ee1f8a999bbbf1b16574b81d8e0faa66ea79b7d1fbc992, CAND-ccda4d5b7132404c27aa255b6e37fcd48185a9dc20b6c6c933d37458c25ed678

These requirements repeat the capability to count and track record deletions\. The location and system scope in two entries is compatible with, and should refine, the broader entry rather than create duplicate requirements\.

Requested action: Consolidate the repeated deletion-count requirements into one requirement that states the supported record types and location/system scopes\.

Source: [conversations/conv\_pines022\_deletions\.eml](<../data/corpus/conversations/conv_pines022_deletions.eml>); document ID: DOC-7b8da7c05931fc99bc80d4a4bb0c8563e690e0c415b57f5ca1ae394462dc26c8; normalized lines 104–106.

> The system should count and track record deletions \(e\.g\., item records,
> patron records\) per location and per system\. Tracking should include:
> - Record type

Source: [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>); document ID: DOC-091180de9b2d4ea83267d989411ac89f415d4def3bbf7cd51651fb7fda8d8bf9; normalized lines 389–391.

> 10\.9 Deletions Tracking
> Ability to count and track record deletions \(e\.g\., item records, patron records\)
> per location and per system\.

Source: [survey\_results\_2009\.txt](<../data/corpus/survey_results_2009.txt>); document ID: DOC-aac7bceef7a883652805583e98ec513b6ae2e7951e2ecfa18722127b1f12a5c4; normalized lines 91–91.

>   - Count and track record deletions: 27%

#### ISSUE-95faa1d752cae1c75c7c393c9ae5542dec22d46af01321325c6c26078818304d (OS3)

Requirements: REQ-189, REQ-390

Candidates: CAND-59c960798b3709e469a8dafc5a451bf9e5193ec69eea2ca93be96efc30ede3e7, CAND-b3cc501f18bdd27a060b221548d9ac3c38dc03bd134d0bf2fcbff54d4556467c

Both requirements state that Management Processes operate on a Linux or Solaris server\. They duplicate the same platform constraint\.

Requested action: Retain one Linux-or-Solaris server requirement and map both candidates to it\.

Source: [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>); document ID: DOC-091180de9b2d4ea83267d989411ac89f415d4def3bbf7cd51651fb7fda8d8bf9; normalized lines 132–133.

> OE-2: The system must operate on a Linux or Solaris server environment\.
>       \[\* High Priority\]

Source: [meeting\_minutes/meeting\_2009-07-20\_minutes\.txt](<../data/corpus/meeting_minutes/meeting_2009-07-20_minutes.txt>); document ID: DOC-5ab1dd8bc97af3b1ab2e378495f0e0d75fd501fcc19f923c0d8fda831074281b; normalized lines 78–81.

> OE-2: Management Processes shall operate on a Linux or Solaris server\.
>       \[Consensus: Both Linux and Solaris are acceptable\. Most PINES
>       installations use Linux, but some larger systems use Solaris\.\]
> 

#### ISSUE-ad9cec1cdf8585be3f6b68efe7fc0e44b54e13cf50765bb3cca44d54cdc8a615 (OS7)

Requirements: REQ-216

Candidates: CAND-9bc83e68a2ac35e88a62b2ea11afa35cb58e25e8664475c70717f96dc03363d1

The requirement mandates Red Hat Enterprise Linux 5 and Solaris 10 on SPARC\. The source requires Linux or Solaris and describes those specific versions as the current server environments; it does not make the exact distribution, version, or hardware mandatory for the reporting system\.

Requested action: State the supported platform requirement at the evidenced level—Linux or Solaris, or both if that is the adopted requirement—and remove the exact version and hardware mandates unless separately confirmed by a normative source\.

Source: [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>); document ID: DOC-091180de9b2d4ea83267d989411ac89f415d4def3bbf7cd51651fb7fda8d8bf9; normalized lines 132–133.

> OE-2: The system must operate on a Linux or Solaris server environment\.
>       \[\* High Priority\]

Source: [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>); document ID: DOC-091180de9b2d4ea83267d989411ac89f415d4def3bbf7cd51651fb7fda8d8bf9; normalized lines 132–133.

> OE-2: The system must operate on a Linux or Solaris server environment\.
>       \[\* High Priority\]

Source: [interview\_sysadmin\_2009-05-10\.txt](<../data/corpus/interview_sysadmin_2009-05-10.txt>); document ID: DOC-b1738fd7a6de9498f19ede6747ba156ecb29ead86ad1c9a2768b53e862ece1a9; normalized lines 31–35.

> ROBERT: Our main server is a Red Hat Enterprise Linux 5 box with dual quad-core
> processors and 32GB of RAM\. It runs PostgreSQL 8\.3 for the database\. We also
> have a secondary site that runs Solaris 10 on SPARC hardware for disaster
> recovery and reporting\. So any reporting system needs to work on both Linux
> and Solaris\.

Source: [interview\_sysadmin\_2009-05-10\.txt](<../data/corpus/interview_sysadmin_2009-05-10.txt>); document ID: DOC-b1738fd7a6de9498f19ede6747ba156ecb29ead86ad1c9a2768b53e862ece1a9; normalized lines 31–35.

> ROBERT: Our main server is a Red Hat Enterprise Linux 5 box with dual quad-core
> processors and 32GB of RAM\. It runs PostgreSQL 8\.3 for the database\. We also
> have a secondary site that runs Solaris 10 on SPARC hardware for disaster
> recovery and reporting\. So any reporting system needs to work on both Linux
> and Solaris\.

#### ISSUE-da91846ce8d7359d59daeccf8c178e18ccdf4aaede0e0f2e70174beb26b912c8 (OS7)

Requirements: REQ-204, REQ-396

Candidates: CAND-0530577eccda48dc14e04a5c2edef3b73ee284be9d5f3435720ee7f6bde583c3, CAND-1c027e89807cec1ef5670ce2cbde759ac8e2d080781acf61afd38ca66ea85c45

REQ-396 describes return-time and renewal-rate statistics as demographic analysis\. The source separates patron behavior/use analysis from demographic statistics, and REQ-204 already covers the behavior-analysis capability\. The categorization overstates the source and duplicates an existing requirement\.

Requested action: Remove the unsupported demographic framing from REQ-396 and consolidate its behavior-analysis content with REQ-204, retaining demographic statistics as a separate capability where supported\.

Source: [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>); document ID: DOC-091180de9b2d4ea83267d989411ac89f415d4def3bbf7cd51651fb7fda8d8bf9; normalized lines 309–315.

> 9\.1 Patron Behavior and Use Analysis
> The system should produce statistics that can be used to understand and predict
> patron behavior and use of materials\. For example:
>   - How quickly is a particular book returned, on average?
>   - How likely is a particular book to be renewed?
>   - What percent of check-outs at a particular branch are renewals?
> 

Source: [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>); document ID: DOC-091180de9b2d4ea83267d989411ac89f415d4def3bbf7cd51651fb7fda8d8bf9; normalized lines 316–319.

> 9\.2 Demographic Statistics
> The system should produce useful demographic statistics, including transactions
> by geographical regions, age ranges, etc\. The data used to produce these
> statistics must be anonymized - information that could be used to identify a

Source: [survey\_results\_2009\.txt](<../data/corpus/survey_results_2009.txt>); document ID: DOC-aac7bceef7a883652805583e98ec513b6ae2e7951e2ecfa18722127b1f12a5c4; normalized lines 51–57.

>   - Transactions by age ranges
>   - Patron behavior analysis \(how quickly books are returned, renewal rates\)
>   - Demographic statistics \(must be anonymized - no personally identifiable info\)
>   - "I use demographic data to plan programming\. Age ranges and zip codes
>     are most useful\."
>   - "We need to predict patron behavior\. How likely is a book to be renewed?
>     What percent of check-outs are renewals?"

#### ISSUE-eae8f7e026851307f5149971ebbd57c993e423a036725bf8819bdf834efa2054 (OS7)

Requirements: REQ-402

Candidates: CAND-0a11d6a6c6777690202274564edb434ab646222968ded51a3c42143500f5a7bd

The requirement says to revert an item when it is checked out at the destination, but the source clarifies that items checked out there should stay; only items that remain unused should come back\. The current requirement contradicts that clarification\.

Requested action: Remove destination checkout as a reversion trigger\. Preserve the stated time-based and status-based examples, and describe destination checkout as a condition for keeping the item at the destination\.

Source: [conversations/conv\_pines018\_item\_transfer\.eml](<../data/corpus/conversations/conv_pines018_item_transfer.eml>); document ID: DOC-a47eb1f11286ff9099687b72a901e4a6ed2455b431087c0742aa78583c5bd80a; normalized lines 75–78.

> I like the auto-revert based on criteria\. For example:
> - Revert after X days \(date-based\)
> - Revert when item status changes to "returned" \(event-based\)
> - Revert when item is checked out at the destination \(event-based\)

Source: [conversations/conv\_pines018\_item\_transfer\.eml](<../data/corpus/conversations/conv_pines018_item_transfer.eml>); document ID: DOC-a47eb1f11286ff9099687b72a901e4a6ed2455b431087c0742aa78583c5bd80a; normalized lines 75–82.

> I like the auto-revert based on criteria\. For example:
> - Revert after X days \(date-based\)
> - Revert when item status changes to "returned" \(event-based\)
> - Revert when item is checked out at the destination \(event-based\)
> 
> The event-based reversion is tricky but very useful\. We send items to
> a mobile library, and when they're checked out there, they should stay\.
> But if they just sit there unused, they come back\.

#### ISSUE-f1c8282f51389782b136edc178b321da11f88367fbc4bdca6b12cf576ab681a4 (OS6)

Requirements: REQ-279, REQ-291, REQ-296, REQ-493

Candidates: CAND-710d77d9020152a42ed48b85c8cce791461d677e82674719081815f65625ee92, CAND-714eff94d1667f6ca43ed80dacbe68f126071db527de4b5cceab3262e6eeb09b, CAND-9ef1edbd32466031d633522508aa503fc2d146708111ba2276e1b4402282d913, CAND-a92484bc9ad4bb23e44e084f856d52f357dbbb8bf856fb373fbfb5c7519a4320

These requirements are assigned P1 based on general importance or inferred reporting accuracy/reconciliation benefits, but the evidence does not establish them as essential to core operation, safety, security, or mandatory compliance under the supplied scale\. Their current rationales do not substantiate P1\.

Requested action: Reassess these priorities against the supplied P1 definition; absent evidence of criticality, use P2 and revise the rationales to distinguish substantial impact from criticality\.

Source: [conversations/conv\_pines023\_patron\_characteristics\.eml](<../data/corpus/conversations/conv_pines023_patron_characteristics.eml>); document ID: DOC-d2b26a6e7678ca4e82bfa7bb06566f329dea692ea22e8987b516fa8bc98c544b; normalized lines 95–98.

> One consideration: if patrons haven't provided optional fields, they'll
> show up as null\. We should include them in the report \(with null values\)
> rather than excluding them, because excluding data silently can lead to
> misleading results\.

Source: [conversations/conv\_pines023\_patron\_characteristics\.eml](<../data/corpus/conversations/conv_pines023_patron_characteristics.eml>); document ID: DOC-d2b26a6e7678ca4e82bfa7bb06566f329dea692ea22e8987b516fa8bc98c544b; normalized lines 121–121.

> - Null values should be included in results

Source: [email\_financial\_reports\.eml](<../data/corpus/email_financial_reports.eml>); document ID: DOC-8b6cfb3cf368b794d82567933f9c85062740814819b1e28b4837f6021cbcbee6; normalized lines 64–66.

> - The financial data is attached to patron records AND item records\. So when
>   we query for financial reports, we need to be able to join these data sources\.
> 

Source: [email\_financial\_reports\.eml](<../data/corpus/email_financial_reports.eml>); document ID: DOC-8b6cfb3cf368b794d82567933f9c85062740814819b1e28b4837f6021cbcbee6; normalized lines 116–119.

> 3\. FINANCIAL DATA \(PATRONS\):
>    Fines, charges, waivers, and ecommerce transactions are attached to patron
>    and item records\. System tracks fines waived and payments made per library\.
>    Financial information can be updated easily\. A staff user can easily query

Source: [email\_report\_features\.eml](<../data/corpus/email_report_features.eml>); document ID: DOC-d9e168e0c03903021bf9e636e1d8e5f56dfcb79cc110d3839e38175a7c54344e; normalized lines 11–13.

> 2\. REPORT TEMPLATES: Admins need to create report templates that are available
>    to staff\. Templates should be runnable as-is or modified\. Changes shouldn't
>    compromise results\. Admins should be able to limit which filters and display

Source: [meeting\_minutes/meeting\_2009-03-15\_minutes\.txt](<../data/corpus/meeting_minutes/meeting_2009-03-15_minutes.txt>); document ID: DOC-defef992db2ae0e10167fd94902eac93f82c59c4c070df030ca2f77811082818; normalized lines 63–64.

>   - Tracking and verifying financial transactions
> 

### Unresolved source conflicts

- batch14/CONFLICT-a2671ca71a91807b8516d031102ba3efeeeea82e5207babb0c7ebaef53e05e34: REQ-019, REQ-328. Both requirements address an address book for report delivery, but the evidence does not resolve whether the capability is mandatory or optional\. The requirements are retained separately pending stakeholder clarification\.

Source: [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>); document ID: DOC-091180de9b2d4ea83267d989411ac89f415d4def3bbf7cd51651fb7fda8d8bf9; normalized lines 626–627.

> - Ability to enter email addresses for report to be sent to - would be great to
>   have an address book of regularly used addresses

Source: [evergreen\_reference\_2009\.txt](<../data/corpus/evergreen_reference_2009.txt>); document ID: DOC-e6aa9f8c6308ab748459f87b578a0df9df9c865b7911bac3686e865963b7af6f; normalized lines 174–174.

> - No address book for report delivery

- batch17/CONFLICT-27fb1ae8ca42a0cc26b8ffae26ebdee453a9bd58fbb3d125bbd297dfd30e4521: REQ-303, REQ-403. The all-branch capacity interface requires a defined capacity measure, but the supplied evidence lists competing measures and does not select one\. Stakeholder clarification is required before specifying the measure\.

Source: [conversations/conv\_pines015\_capacity\_interface\.eml](<../data/corpus/conversations/conv_pines015_capacity_interface.eml>); document ID: DOC-4acf2fdb375b86d49420e5743267e19b3f0af9ebe8bd764c1a88379aa9f5b662; normalized lines 3–7.

> As a branch manager, I need to see the capacity of all branches in our
> system, not just my own\. When we're deciding where to move items or
> allocate resources, it helps to see the big picture\.
> 
> Is there a way to see an overview of all branches' capacity?

Source: [conversations/conv\_pines015\_capacity\_interface\.eml](<../data/corpus/conversations/conv_pines015_capacity_interface.eml>); document ID: DOC-4acf2fdb375b86d49420e5743267e19b3f0af9ebe8bd764c1a88379aa9f5b662; normalized lines 52–56.

> Also, what specific metrics define "capacity"? Is it:
> - Number of items vs\. shelf space?
> - Number of physical items vs\. a configured limit?
> - Circulation volume vs\. processing capacity?
> 

Source: [conversations/conv\_pines015\_capacity\_interface\.eml](<../data/corpus/conversations/conv_pines015_capacity_interface.eml>); document ID: DOC-4acf2fdb375b86d49420e5743267e19b3f0af9ebe8bd764c1a88379aa9f5b662; normalized lines 57–57.

> Need to nail this down before building the interface\.

## Traceability summary

| Requirement | Internal key | Candidates | Sources |
| --- | --- | --- | --- |
| REQ-001 | REQ-001d6b93e9041d3c5c1eba57986561225d75713aa85317ddc4777fb4413e1451 | CAND-4ce1ed994be79d34ee7dff03169a107ac39133bc29b8f1694d0b754166f98354 | [evergreen\_reference\_2009\.txt](<../data/corpus/evergreen_reference_2009.txt>) |
| REQ-002 | REQ-003021ae0a370d08050a95049f055465836ea7c94b3a2da32cdb59f2777222b2 | CAND-7ea2b48e4d5d6940db1111a179137bca63403d398de04459260cfacba9c2b393 | [meeting\_minutes/meeting\_2009-07-20\_minutes\.txt](<../data/corpus/meeting_minutes/meeting_2009-07-20_minutes.txt>) |
| REQ-003 | REQ-006b3492a2b761f611cbbcaa4ccfd246d7d09ec292a7e4fc3f03c091d3e92ea8 | CAND-504307a404fa2b2858176138734414b4308de790d09ae77111b198a21648f85e | [survey\_results\_2009\.txt](<../data/corpus/survey_results_2009.txt>) |
| REQ-004 | REQ-00c33705380271f9f097fd43192a91fa776eeae0826e3a32f0134c438da149b5 | CAND-01d145faf148363b6616aa760e85d5e43147daa16ea7a43f9d758cd1dae8d514 | [conversations/conv\_pines019\_020\_missing\_intransit\.eml](<../data/corpus/conversations/conv_pines019_020_missing_intransit.eml>) |
| REQ-005 | REQ-00c33705380271f9f097fd43192a91fa776eeae0826e3a32f0134c438da149b5-new | CAND-e7f4a40694e4f1b530955d4fd215c15b1c8c4b6a5cf7acfd5488db48de8f91a4 | [interview\_cataloging\_2009-05-08\.txt](<../data/corpus/interview_cataloging_2009-05-08.txt>) |
| REQ-006 | REQ-00cfcd9e274e2beda7b8976f75522b15b9a2e83bbf449b3ca21610dfaf0505e6 | CAND-e7210799b1cf38e6327adf462f30c04ca8bc18be4eeb8e6bef7befe58066c67c | [conversations/conv\_pines023\_patron\_characteristics\.eml](<../data/corpus/conversations/conv_pines023_patron_characteristics.eml>) |
| REQ-007 | REQ-012944e973cc481c9f218b200036126c08c5d6d52b1f23770d88491598165415 | CAND-c532dd68f6aa5bf872b59a635d7c50d39d4129ad78ab912efddd1ef17e47a9fd | [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>) |
| REQ-008 | REQ-0132b810f72302c145e0b929e6f52a3ef093e4029eaf69f01e1b30883ba61f22 | CAND-7027a266c65f9ec37a9dbed0d91aa886cf0a99ad45d6da59fd2cc973c20de579 | [survey\_results\_2009\.txt](<../data/corpus/survey_results_2009.txt>) |
| REQ-009 | REQ-0134f0fed99c1e9a521fb285371cdadf320cd08885cbdb7d9144cb77f5aae13e | CAND-5f14ff99a1c539854a4c289c2e134f09fe3d2988ed15430743e7626683f13ad7 | [conversations/conv\_pines022\_deletions\.eml](<../data/corpus/conversations/conv_pines022_deletions.eml>) |
| REQ-010 | REQ-013c4361595619bea95b9311ed36e61497c8a00ac5bd45e3efd2a71c778b355c | CAND-8df2af985b0865f6c841b7458be78c405e329d54cd07b169e206ff941ceb2c7e | [conversations/conv\_pines018\_item\_transfer\.eml](<../data/corpus/conversations/conv_pines018_item_transfer.eml>) |
| REQ-011 | REQ-0194ede2e2e348ff5c24cbfb604872c53ec777610a44f5d10f7b15d7efbf8be9 | CAND-af2620caa2835352f8c4f10988413f8cd94287039f98f29d7bd9acbd6e9485d5 | [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>) |
| REQ-012 | REQ-019b1d41cf92a548a2780a8efac86580c234ac6b42313092caced1503dea0d40 | CAND-8817d2fe09b0632e6a2738ff06836dc4ff1ba348ad96a5d67d3588c3864256ce, CAND-89f83065ae1742a1bf1677e89beba3078f3a05a6c9e521b56167ec6f95834de1 | [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>), [meeting\_tech\_subcommittee\_2009-06-30\.txt](<../data/corpus/meeting_tech_subcommittee_2009-06-30.txt>) |
| REQ-013 | REQ-024b618d9579d5dab0f0805011eaa804fd2bbe9c076bf2408113263bd866340f | CAND-f0b3763da289ca2f75066fc05cdae98561d4bdf0bc87e103a5d70d6227b32e95 | [email\_financial\_reports\.eml](<../data/corpus/email_financial_reports.eml>) |
| REQ-014 | REQ-041e44cb0ab21fc97625e408d3c290f7fb2d6215567cbed11cf43b296e11ff5a | CAND-8f79679d7c9152728fa6b7ab88b4930af8d60c41eb21c6363f24b7133fcb58a5 | [meeting\_minutes/meeting\_2009-07-20\_minutes\.txt](<../data/corpus/meeting_minutes/meeting_2009-07-20_minutes.txt>) |
| REQ-015 | REQ-04b6c2cc1e3847ea8aec226d7758663c58c059545dd9f0869422a8f15a3c28fe | CAND-7c45d8d40c7c07636307b9d374b6f33502471ca6f48b546e7ec8e438657cbf5d | [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>) |
| REQ-016 | REQ-05cb4e757788e452d3584a452b53cc757d16291bf6ea9a5f44ca511bfc3eb4a9 | CAND-0e506deb9a1e647ba46c6f66c60adee87babf6202235c41162ee1a6ef047a7ec | [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>) |
| REQ-017 | REQ-0631fd069698385e9c3b2f3e4c8d5296606d6c85e891b30749bd4878a49a6ddc | CAND-aee2451b88e390dd75447951414b1e52caed944ff12830dabaf9dc79d2b41aff | [survey\_results\_2009\.txt](<../data/corpus/survey_results_2009.txt>) |
| REQ-018 | REQ-06ae1f2fbdbe44800091725474b0d8aefac31f56f51976ab43bb88ae220dae93 | CAND-dc31594e5bcbf6a30328cb898e8f4ed7896529776ad662c13cae0b0c75bd97af | [evergreen\_reference\_2009\.txt](<../data/corpus/evergreen_reference_2009.txt>) |
| REQ-019 | REQ-06cc288fe67ae0505b0dc4c9c8a62b23e08949626b7622e8651532a9715cd159 | CAND-d79cf16557191fa22451a45abaf6d3d9c8df88ab8b3fa2e4cf6e0177e25b5380 | [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>) |
| REQ-020 | REQ-074d068b280ae3a2b37e9afc518c9ba66dfee641e23891167c0ecc377a82c38c | CAND-4efc0e79a646d5645dbd5d456af0a1680850ed231d2d81ebdf61d8673d07eb8b | [conversations/conv\_pines016\_shelf\_space\.eml](<../data/corpus/conversations/conv_pines016_shelf_space.eml>) |
| REQ-021 | REQ-07c3ee473dadac84817b2277e6cb3656891b88832d1024f4951332ddbb8e2059 | CAND-b0de2230c4d55b6714a05b648933e437a4d20e7d5e9c329bf6c22c9d95584991 | [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>) |
| REQ-022 | REQ-0801480f36cb42d3178d8ca7b553d847b3826ba62e4e1e91738f9646c6674988 | CAND-cd1224310883a1f4707e1175c2590445bc7a6acad0a720f8e316cd4f8f7bb80c | [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>) |
| REQ-023 | REQ-0a5e692f9e97183dabad28474e381b91d2923904c84b752bb58586ded73f718f | CAND-29c4ba01d2f9cf6e200dd59ee871794c2b033f63c1f5b5f11c2bf0fc9dc63dcc | [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>) |
| REQ-024 | REQ-0b0f974518fad561b3186d4d04ecd426b248cf8f333c1b059b441dfda7c795b9 | CAND-d3d04a98c617e7a4f045ae31e00f8360416d7f5a7ba1e9fe9b0cf2526cec6bf4 | [meeting\_minutes/meeting\_2009-03-15\_minutes\.txt](<../data/corpus/meeting_minutes/meeting_2009-03-15_minutes.txt>) |
| REQ-025 | REQ-0b13b445a2eea4822fe4aa71a6fc4706a1cbdb82433a90a6b3593ec1cf27a0bc | CAND-7cd525708cf99590b441535f77c6ae1c06d208270c855478e877dc391d16d19e | [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>) |
| REQ-026 | REQ-0b4f2cddd3f199e2f2faaefc355fc07c824110bec7cc88e02132b9a73e372204 | CAND-aab216802cf265e16e28c51729a8002f33796469b76d259d756e9d0c7db117b2 | [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>) |
| REQ-027 | REQ-0bf369c574dd1446c301fefbc8244c1b9e738fa6e8d93751bb992c2297455f05 | CAND-fae7c1b6bb14749f9bd236a1111e847138a52bacd7925f28671ae4e4e0a3f354 | [meeting\_minutes/meeting\_2009-07-20\_minutes\.txt](<../data/corpus/meeting_minutes/meeting_2009-07-20_minutes.txt>) |
| REQ-028 | REQ-0c113d026df68f16729ac7a566d781131b697eee2df934e938acc760322cec36 | CAND-58e875ceaaa779afc7bcb7d8ad05cc618a66e02c52c68bc772ddf0bbb868b950 | [conversations/conv\_pines018\_item\_transfer\.eml](<../data/corpus/conversations/conv_pines018_item_transfer.eml>) |
| REQ-029 | REQ-0cd60684d308634bc7ff6bb24e1a577c13868ead64ab9f65a38fb0227bac654b | CAND-6f5cec804e36605c002a5e55e8ef7ddc3955f92a0ea7d8d1b5b945a71969313d | [conversations/conv\_pines015\_capacity\_interface\.eml](<../data/corpus/conversations/conv_pines015_capacity_interface.eml>) |
| REQ-030 | REQ-0cd6e2d32e669a0e764e5bbfc47fc544bff20080d82cb787b3a6c1b16f3514dc | CAND-8c652bc3345ea74741eb6655a3f950d14ae7d84725e80a46c4cca63b4fffdc9a, CAND-90765e8428262b81ed25442a788311ec6450ccc4302b3b96c06d09e6c3d517f8 | [conversations/conv\_pines021\_item\_purging\.eml](<../data/corpus/conversations/conv_pines021_item_purging.eml>), [interview\_cataloging\_2009-05-08\.txt](<../data/corpus/interview_cataloging_2009-05-08.txt>) |
| REQ-031 | REQ-0d6669b08c08f44c8cfbfa02c634c6005dcba584ee6a8d0e6dfe7a3d308f16e8 | CAND-5ccf114ce994ef24a37962a6d9d0f4b4cb5accfa420990571cb5e65f3badcd6a | [interview\_cataloging\_2009-05-08\.txt](<../data/corpus/interview_cataloging_2009-05-08.txt>) |
| REQ-032 | REQ-0e6c5261b0a1640d933fe9a3c80151623177b25eb91529c956c4fecd8fb648cf | CAND-c742cd2b1d1d299cb25523530d924d851bc17c0d21b0a8390f2c1985e58974b5 | [conversations/conv\_pines018\_item\_transfer\.eml](<../data/corpus/conversations/conv_pines018_item_transfer.eml>) |
| REQ-033 | REQ-0f1181ddc427c4dbfe0fdd104eec5740906fb43ff085e68c6bfd2b6a897d5b9d | CAND-29dc146fbfab9452c3e062d94c0c4494280e1ebaef4bad6677bff8a9d99d8c70 | [conversations/conv\_pines019\_020\_missing\_intransit\.eml](<../data/corpus/conversations/conv_pines019_020_missing_intransit.eml>) |
| REQ-034 | REQ-0f2df5fec52e41fa3683855f47c8a7bbe69e0b0e6231f03c0594a53e780da514 | CAND-5a8bccc70d8bad6722fecaf52001868994ddff8e762fb963e4733978f3dd48f3 | [conversations/conv\_pines018\_item\_transfer\.eml](<../data/corpus/conversations/conv_pines018_item_transfer.eml>) |
| REQ-035 | REQ-0f7d0c19e19070f9e9cf6b47dbe31b8efcc082a2c9d843ceee779e04f169cb3a | CAND-1b4af7271a734267072ececbc204022f41cb142f17cafaa0aa494d0d7ae41355 | [evergreen\_reference\_2009\.txt](<../data/corpus/evergreen_reference_2009.txt>) |
| REQ-036 | REQ-104449e9d557f36a5702fd2cb149c56e7c2d7b0e2d2f703ba162babef3fc3ddb | CAND-0afeca455dbfc1369bbcf9b9e5f79e64a642060dd5a480acfc44ed24d865ef39, CAND-2ae75acd187869ad6e351b5d95e51b57f8bb0981288135f19c7d3a0eb4ad9220, CAND-3a2f5351b9d878d8624a7eecb4280977e040a1be97398e2f3bf6ce2eb43d182f, CAND-629713e3c077bf3bedf37177ad2da63a8652375ccf9476eac77861123a9a4d63, CAND-af44c77e71c4d09def9032d41935558b89e1699a2fc782938e053a0298542fc3 | [conversations/conv\_pines014\_material\_volume\.eml](<../data/corpus/conversations/conv_pines014_material_volume.eml>), [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>), [interview\_cataloging\_2009-05-08\.txt](<../data/corpus/interview_cataloging_2009-05-08.txt>) |
| REQ-037 | REQ-10a2c5b7e4fb128df54d02b40b9d402527a628d6113f91d50b40b8b4a6a5fe76 | CAND-e884e6ababfe41fe3c05f8b878305dd255452e3b528e52451aca76cfd1760ad7 | [meeting\_minutes/meeting\_2009-07-20\_minutes\.txt](<../data/corpus/meeting_minutes/meeting_2009-07-20_minutes.txt>) |
| REQ-038 | REQ-112bc6169b74f99b74669890aa6112c9a3cde4f1092a37f1183ba8a7bca59929 | CAND-0ffd6b9e640006b755ac309601feb5ceba01b917e171cb7b6f16c7a79a51e3bc | [conversations/conv\_pines019\_020\_missing\_intransit\.eml](<../data/corpus/conversations/conv_pines019_020_missing_intransit.eml>) |
| REQ-039 | REQ-1174f75bc65d73fc20211bb38a545ccba560146803442678a7ee33c8c7712c24 | CAND-8bd6179a138ba10b91aea9abee7c8b881663f85f63e559dbaef7928c0e8ad896 | [interview\_cataloging\_2009-05-08\.txt](<../data/corpus/interview_cataloging_2009-05-08.txt>) |
| REQ-040 | REQ-11be320c3e87894730bd0c6d08942c810e2cf75770097faae1e03d027e821485 | CAND-dc8acbb37eb0428634745aa31b7f901db91bc335085a8d865c8e921eba2f5cbd | [meeting\_minutes/meeting\_2009-03-15\_minutes\.txt](<../data/corpus/meeting_minutes/meeting_2009-03-15_minutes.txt>) |
| REQ-041 | REQ-132114c65eee111425a4573ea3d23198475d2956c7a12a851178775a9096cfff | CAND-42c57e31eea5838c8b279921de7b6512425150bcd8962ff0d8c9b308882ec0ba | [email\_financial\_reports\.eml](<../data/corpus/email_financial_reports.eml>) |
| REQ-042 | REQ-140c8dff3bef72b3bc3db8c25d0bb367fff8760336ab23a3c306c8c6a54d4372 | CAND-44e028a885fd0ceaab543ea135fcd42c9f7a10b089b81588c10e1200f16a12f6 | [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>) |
| REQ-043 | REQ-1542ab7fef252056a50f9108296a50c609ab1c7798ddc69c24d50aacb02ccaca | CAND-ccd7ea4ab293e2721bef79847565cf04bf4655fb6d860e061b8be67f3bdfc49f | [email\_report\_features\.eml](<../data/corpus/email_report_features.eml>) |
| REQ-044 | REQ-1672aa797f51ac49051ee329dbe173d2fb7a4ee576ee1421ded739bb790e1a71 | CAND-76e7503afd5e401e1a131565a66493c42801cc78fe902a9bc5cabbae0181a2bf | [conversations/conv\_pines024\_inactive\_patrons\.eml](<../data/corpus/conversations/conv_pines024_inactive_patrons.eml>) |
| REQ-045 | REQ-16ae6ac8c8645e39f59bb3b5e0ab454b414b354fa1062b27fb64d892e424ae3c | CAND-5529179bb446f31d0b366c23743f0decc38ba0eca4383169bfb4591892cdca6e | [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>) |
| REQ-046 | REQ-1727ffbefccf46e0885013da826069199d8e0e41eedf69f52c48d433ecc98ddf | CAND-13523719220bb248315f5b1c8930e7efa88fc53bf60aea1eccff1896406fe6f0 | [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>) |
| REQ-047 | REQ-1993897f0cc8a87078b872ed55cd076825df08ab489dfd4d052efe3ba6ae0e7a | CAND-31c7966ec2d46c14333f51369be84647d74fbc4988bce381e79465292a352d2f | [evergreen\_reference\_2009\.txt](<../data/corpus/evergreen_reference_2009.txt>) |
| REQ-048 | REQ-1a2eddfe406759457c40f392749961f439007051a7492c01ac3d0b97fb964f6e | CAND-efa36da8c136b37b661a9a364466bfb4cb6c053746405bac285350f7a23f056f | [meeting\_tech\_subcommittee\_2009-06-30\.txt](<../data/corpus/meeting_tech_subcommittee_2009-06-30.txt>) |
| REQ-049 | REQ-1a585170f6200d72a170a9d5ab26b4788941d8a63df21131ccfcb07d6d035754 | CAND-3bdeff3f1151aca3fb45a0106dd29435d2b71b907f7687fd4c507c9b79b3ee77 | [evergreen\_reference\_2009\.txt](<../data/corpus/evergreen_reference_2009.txt>) |
| REQ-050 | REQ-1ab543c0a25babe1fd371782db199fca173a295ba6715d96727b4aa895042f0f | CAND-da02cd5a6ab15e849c36876ebd1b3b7fac8cebc91409999913c95c18209bc998 | [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>) |
| REQ-051 | REQ-1b9c1ad416aef54b2aafdf7381ad663c89d97c803be3ceb2d3f4a385f7094d2c | CAND-5cdf7eff611619932cd7b1e37e71c100a5fc2b261bb374e6bef861b9b3e79458 | [evergreen\_reference\_2009\.txt](<../data/corpus/evergreen_reference_2009.txt>) |
| REQ-052 | REQ-1bb2dc57368dcf2ef1fa46aee853dc91f05efe385ba78341e58d96448bf9b72e | CAND-8365541838de5641c57ab2a1833631d40f67a64f715995902d7862a274f79dce | [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>) |
| REQ-053 | REQ-1bd4de4fce7952b990a84b0ced6483a560f44842c7a50ad1a4cc8ef8184650ee | CAND-4d37e3d4bb54e2d43a3f7417f6520aed696c9eeb12007c263f51bb80e5cb8f74 | [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>) |
| REQ-054 | REQ-1c06a018874f68e74b6bb3d354549d34ccdc7ca19631c46ae69ea925c822b010 | CAND-9139c6ef9d904680f4d9ae9939444cbae16c1cecb88660072540a3d961348d30 | [meeting\_tech\_subcommittee\_2009-06-30\.txt](<../data/corpus/meeting_tech_subcommittee_2009-06-30.txt>) |
| REQ-055 | REQ-1f32e45a08417bb5fa4738861a2718e80c3bb3f2215486380c3f1534f13cc331 | CAND-e86ce8b434d47af8fdd6d4246d3fe39317c438e18675de1ed40c5ec9fe23833e | [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>) |
| REQ-056 | REQ-1fc20f70bb4490befccf8582e07e2f381f07a8f3553e194d079d88d32c95799c | CAND-68ff94d2b19db868ef439a55726c2aced5231bf23cdb9a42ee93b91209fdf19e | [survey\_results\_2009\.txt](<../data/corpus/survey_results_2009.txt>) |
| REQ-057 | REQ-21e2586cf7d27ad176e7b5433dbae3a7879f3f3a5139bc7d3807a7eb0057fdcc | CAND-06a160839031bbc48ca34208ff86cf1025843496af82bbb0a84b7b640071879e | [evergreen\_reference\_2009\.txt](<../data/corpus/evergreen_reference_2009.txt>) |
| REQ-058 | REQ-21eb547e8be2f8c2710dfa12df27614f5242422bc931082d6d5154b093c538d7 | CAND-d3cad322c5d4485132df7b22ca4e3d7ccc175da4072706569d4b33d99efcff2d | [conversations/conv\_pines021\_item\_purging\.eml](<../data/corpus/conversations/conv_pines021_item_purging.eml>) |
| REQ-059 | REQ-226422db6abcad9f3cb4f46f9ef39d15ad2680b11f8021bb63b6bc76675b568e | CAND-2a70be31526eceaaf09300c8cd94ae2121dd968807211542caca1f1e6641545c | [conversations/conv\_pines024\_inactive\_patrons\.eml](<../data/corpus/conversations/conv_pines024_inactive_patrons.eml>) |
| REQ-060 | REQ-22d99f9f29ddea2ba6dc1111c64c1e95ec393f943e42e56f85f9f2590a5a00eb | CAND-9c52f6c79ce2ece8dba0511c945710b48d1f15f20beaab834054706322272f4f | [conversations/conv\_pines022\_deletions\.eml](<../data/corpus/conversations/conv_pines022_deletions.eml>) |
| REQ-061 | REQ-2300bcf8038e7ded85f55e018f5bcb974d53c5e40a931fafaa2e01e3de610d66 | CAND-451e368af09b4f0999863202e1a0dea7ef9a2c2e4dbabfa3617262b7979fecba | [conversations/conv\_pines016\_shelf\_space\.eml](<../data/corpus/conversations/conv_pines016_shelf_space.eml>) |
| REQ-062 | REQ-234b530eab753fc65bb8c02bc4f4a8c83b7df21636af1365b52df906e4376043 | CAND-18940d55b2311d0b4d83cf089c9f6a1303f3964cda14363e3de1b305ed225f3e | [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>) |
| REQ-063 | REQ-24199549b50e10e76152e30aba2abf48577af8ef296fa73d4eeebb29afb56103 | CAND-513284f7c6f23040d68eda7869715544e96a9816ade06e8e077338be94d5f995 | [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>) |
| REQ-064 | REQ-24a38bf6f293220c6fdbfd62cedc381f5a594a32a919c1048fff680b2bd1d328 | CAND-bb0ea6a9f1a403fe1ec786606e3b6a4737ab5527e3e6d59315ba74205d8af4bd | [interview\_cataloging\_2009-05-08\.txt](<../data/corpus/interview_cataloging_2009-05-08.txt>) |
| REQ-065 | REQ-2575b458130a875a2f3aa3f2903d078f6ab5eb22cb1de3680189b30ac50c8d85 | CAND-a6a32ad9dad04495906a314aaf805acd9790c236fb16c3994bd292736d145560 | [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>) |
| REQ-066 | REQ-258be826194ebfa112611c657f7ba15df59c1774ba05a615d240a909c94e7783 | CAND-ddef7bf56f650d087d2268ab1f42bbda89ba7c00dc85fe49396ba349230aff20 | [meeting\_tech\_subcommittee\_2009-06-30\.txt](<../data/corpus/meeting_tech_subcommittee_2009-06-30.txt>) |
| REQ-067 | REQ-26177571770f5142eedbee22e4bec89acff23a275da9ac3f082d3c22575179f4 | CAND-5ce0d1e400764d5bf7de9beb9ed6999ed95bb5cd963c2dc304c1a72fc794eeda | [email\_financial\_reports\.eml](<../data/corpus/email_financial_reports.eml>) |
| REQ-068 | REQ-262943d09c57181db20a03519ae9c661cf2ca6604fff253c417fbe263b0613b3 | CAND-253c14c36bffcbcaa58457ef151f9cb0351293fb57a1707cf846bdc855e0301a | [survey\_results\_2009\.txt](<../data/corpus/survey_results_2009.txt>) |
| REQ-069 | REQ-262e4ae00b36db862a9ee8753879427865a3c136fafed0fe4c2691637dca76ab | CAND-e73112df4c4e1e104d9691ddaf67a7996e0f09e1b85cc72e61c7fed5d276b0de | [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>) |
| REQ-070 | REQ-26c40fa365956e4272fc695a8371aae04ca3584ef6f957602cfb7061ae2d30bb | CAND-c6141814d98fe5b0a8f0ba46201ae3cb8b8711b5346ffd046fcb2479d1301195 | [meeting\_tech\_subcommittee\_2009-06-30\.txt](<../data/corpus/meeting_tech_subcommittee_2009-06-30.txt>) |
| REQ-071 | REQ-26e9b5d56720d9ade801e5aff799b889cd990d00147524e131e7aacbbf7bc817 | CAND-b80c7a667f93d247ba5f74eea78e6986f4b2331bbc8241a0937f3c9dfb06590c | [conversations/conv\_pines024\_inactive\_patrons\.eml](<../data/corpus/conversations/conv_pines024_inactive_patrons.eml>) |
| REQ-072 | REQ-26ec0f186e788c756d098aa0a72bf088cb9b9e08c9a8b73d3e1e19de8b9eef88 | CAND-71fd9dc7bf25f15245653567b30a00349a3e085c4188a4c2665ceee72f27ebbb | [meeting\_tech\_subcommittee\_2009-06-30\.txt](<../data/corpus/meeting_tech_subcommittee_2009-06-30.txt>) |
| REQ-073 | REQ-2718971e8588d933e255e76ac2d68a8c5bc0cca599cf883e8f9e95af52156d82 | CAND-8d42b838447f80ffe8cc776bca106392a12014ef06a61e58c2c906efd9b8ae42 | [conversations/conv\_pines024\_inactive\_patrons\.eml](<../data/corpus/conversations/conv_pines024_inactive_patrons.eml>) |
| REQ-074 | REQ-279724ab69bc0d638d84fc9089b9a9ca3a21a9c871565f6e55936a2e5a953c58 | CAND-60dadb8062c1e2de076b05f5433c60e27baf7d8f133d0a9daeb1a437e6c9be95 | [meeting\_minutes/meeting\_2009-03-15\_minutes\.txt](<../data/corpus/meeting_minutes/meeting_2009-03-15_minutes.txt>) |
| REQ-075 | REQ-27cc9512436bfa663fc1b96d788ece69cc7d845f2e852c2eadf1e0aa42859291 | CAND-d69e39e1039b4090a0f926bcead7974b5ebd2827f174d281313bf5a8b47bc9fe | [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>) |
| REQ-076 | REQ-27d474f2bac7a0762149523421b16972fc4b40b653ea9758dc128184eb3da09f | CAND-ed9641d456143ab968495db7ebff977a362658fbfb083c72630d9a4b0d5182c0 | [meeting\_tech\_subcommittee\_2009-06-30\.txt](<../data/corpus/meeting_tech_subcommittee_2009-06-30.txt>) |
| REQ-077 | REQ-286c5a869b7870b652c4fa583d39628483ffaab45f98cf74f310c163143f7f45 | CAND-d31bf409015246295898c44e0976f4ae015f0928934685591e6f00cdd3bcf030 | [conversations/conv\_pines023\_patron\_characteristics\.eml](<../data/corpus/conversations/conv_pines023_patron_characteristics.eml>) |
| REQ-078 | REQ-29c4b814561f3df4373983fae140f570aa3ac86f726e88ac56bcf8c72c750702 | CAND-7e450a7847586de3f40f3f805e7d1bf61eab75d0008424b16872024b182e1e85 | [conversations/conv\_pines023\_patron\_characteristics\.eml](<../data/corpus/conversations/conv_pines023_patron_characteristics.eml>) |
| REQ-079 | REQ-29e2133460b5f10eb2fc01616feb60b47b529b3a23e45564406967e3cf848384 | CAND-e2fb31d228e8ece8e3a7e46c0d8553337222b4c7e9181b9b8209560325e5e146 | [email\_staff\_login\.eml](<../data/corpus/email_staff_login.eml>) |
| REQ-080 | REQ-29e59c70f4114d2d61a2625aa91cff01d28a4d1fb10ed048842b07b922af32f0 | CAND-3e8af1e576bd07fa9a6c08a56b861662f98bca9aafef437000d8ee817dab9a5e | [meeting\_tech\_subcommittee\_2009-06-30\.txt](<../data/corpus/meeting_tech_subcommittee_2009-06-30.txt>) |
| REQ-081 | REQ-2a34a6ca032b3f61e6310bf246589b4aaae1403d54a7c9f4d1cd903d1176acac | CAND-ec7dd567916e089c22a612cbecef7342ca89343549fc3e24a7670de7b36e14dc | [interview\_sysadmin\_2009-05-10\.txt](<../data/corpus/interview_sysadmin_2009-05-10.txt>) |
| REQ-082 | REQ-2abde3d3fc149f3792ee098af3876d9a6f6ddf7dcad59c12b745af4715467273 | CAND-694dd7331a22c4a9248dcea707d3fad37b520aa29f54055e88832fdf9298c0aa | [interview\_sysadmin\_2009-05-10\.txt](<../data/corpus/interview_sysadmin_2009-05-10.txt>) |
| REQ-083 | REQ-2b20da6ffe2e5d2f5ac0d476581e05654ddab0be0c7819c933c133557ec2c095 | CAND-f0404cbb13127656a1cf20e19e54cd6d0cb0176996f9bfaabb5afe358b6d74ad, CAND-fb67462b82ce634ccb46ff2a4be799937873bd3257803d9c0527b319b13e2b84 | [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>), [meeting\_minutes/meeting\_2009-07-20\_minutes\.txt](<../data/corpus/meeting_minutes/meeting_2009-07-20_minutes.txt>) |
| REQ-084 | REQ-2b59c53f90acb3288b70f7f08af14dac9ce88284fc392695bf5a211e6267a09b | CAND-9611f851f8d14d9faab8c48ac0c624980d4ab2848fb112d7f63845c04b735a95 | [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>) |
| REQ-085 | REQ-2c377ae15450567ec55b3d92f63445302a6fa60279f2e1bd7b924f3e0684e7d8 | CAND-1e24e587c59c6661c57067e6ccd780ded1ebc6669917891dadd951cfcc32b8b9 | [interview\_sysadmin\_2009-05-10\.txt](<../data/corpus/interview_sysadmin_2009-05-10.txt>) |
| REQ-086 | REQ-2c734477c16b9da1697067852b5c63069c087a75a0a5c6389f0cb3ac783cb4ea | CAND-9d3ffb182d868c5a797e4d73f942ee6e8cd15de363fa4669d02f0fa63b32cdbf | [interview\_cataloging\_2009-05-08\.txt](<../data/corpus/interview_cataloging_2009-05-08.txt>) |
| REQ-087 | REQ-2d6d7027d970d64ac8b668881cbfdffe97ee8238e57666edd6313965aa981791 | CAND-bb3152cacd82ed2b60616520472f537544339d2e56077b4d1211f25a44f9f82d | [evergreen\_reference\_2009\.txt](<../data/corpus/evergreen_reference_2009.txt>) |
| REQ-088 | REQ-2d7565d050f266ba2d57fbc8de84f46aab2b4515a8744c3d87a07e77532b2778 | CAND-6b8a3978207838c5ae4ae42703c6c421672d3c6d481c1a8e8ef81c23793d933b | [conversations/conv\_pines014\_material\_volume\.eml](<../data/corpus/conversations/conv_pines014_material_volume.eml>) |
| REQ-089 | REQ-2e5b3f3719980a9e0e3981b2727a9c3c0b57b1efe7e39a23ccd5e3ed0ac5507b | CAND-45e6c8a56b7d685969e4e7d566f32c4faf4a433148a29b93ed59c83bebe186ab | [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>) |
| REQ-090 | REQ-2f0b2a4e587a13a0d36c20cc5a8b7d27dc301b4759455c4873f00a8a0da0b1c9 | CAND-0cd068b39f1827d787a7f3d37546305bcbe3d5a6dcb80b25c2375c0c238d77e8 | [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>) |
| REQ-091 | REQ-2f233809631a3784fa8f496f33d69b9e5670375ac95f57e54eb631bca2327fe9 | CAND-8ae508337d91d13e0e2b5e565e1e20dd9a335c2087cf4788ff9bdb8a8f92211b | [meeting\_minutes/meeting\_2009-03-15\_minutes\.txt](<../data/corpus/meeting_minutes/meeting_2009-03-15_minutes.txt>) |
| REQ-092 | REQ-2f9d588489198ee3df69cd29804622656d27de492ddf4ca53b2b3304ed5d47ee | CAND-12f84f0d7c3b77bad76223c56690c0652f94edbd0612d9cc927e047a9e2fdb7a, CAND-5f7f363b71f413c56dd01778e709803ac4fdb5489e2948765109f021f164564b, CAND-6d2d3a69800ac11cb523b8b50d3d183cc4e5272c6987aaf059fbf29d7411bdb8, CAND-8ecc856417c12f521731dfb71943884d8e92e580a2921a44499eec767f7c1c19, CAND-93788a162aa928e99d3f586f49037960838a578c3b127910a6401f57cecc4b95 | [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>), [evergreen\_reference\_2009\.txt](<../data/corpus/evergreen_reference_2009.txt>), [interview\_sysadmin\_2009-05-10\.txt](<../data/corpus/interview_sysadmin_2009-05-10.txt>), [meeting\_minutes/meeting\_2009-07-20\_minutes\.txt](<../data/corpus/meeting_minutes/meeting_2009-07-20_minutes.txt>), [meeting\_tech\_subcommittee\_2009-06-30\.txt](<../data/corpus/meeting_tech_subcommittee_2009-06-30.txt>) |
| REQ-093 | REQ-2fa5c45c1afcb2d8ef921cd1868fc04a1c1a7aa4b18908f1be005bce3debfc56 | CAND-2a25edb11d5b427c5c90666e206bb433c459facee8f85ea23156761b154b23de | [survey\_results\_2009\.txt](<../data/corpus/survey_results_2009.txt>) |
| REQ-094 | REQ-30ef99ab0e984fab20b5d47a4dd43b43319cf24f0746ee4910c420df76b99c92 | CAND-9f018efc5c88627cbc3659dcc9e04f9f9380795405eb72c2f48cda3bfa32d7ad | [email\_financial\_reports\.eml](<../data/corpus/email_financial_reports.eml>) |
| REQ-095 | REQ-32c1a6f5a798d7817741962e04e0fd75676bba88896506bb9f53699659445f3e | CAND-1eb2be6e31853b5d2690b1d4440db9098424b99c11c54b6233099aabbeee403f | [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>) |
| REQ-096 | REQ-333a244430151ec3ce30f53536237448bfacc5b35b20b31c71ab9482c30f6b79 | CAND-06a2fbeb406f29ddb0592cd5d0b6e33368dc54f0ff91c110c6770b2fc5b8986d | [meeting\_tech\_subcommittee\_2009-06-30\.txt](<../data/corpus/meeting_tech_subcommittee_2009-06-30.txt>) |
| REQ-097 | REQ-342f3a69f00fab04f26b49133990668495d3564788200c918993798de90fe495 | CAND-49907d16099c747de7c369ac72a2d06e02104762b0f9bbbac5bd4b5ab1480362, CAND-54c5e09b3c32679ee73dbbc10673c654f92416e11f5b16d9daed8ade76966dbf | [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>), [meeting\_tech\_subcommittee\_2009-06-30\.txt](<../data/corpus/meeting_tech_subcommittee_2009-06-30.txt>) |
| REQ-098 | REQ-34659944a82365513d0dd1846a4afdd53bc62048c1c0f107bd731c46aee40e28 | CAND-a83bf47f7f6aa94e2c174ae11a8639be1e6735baa3d1767abf2f06d2b068c796 | [meeting\_minutes/meeting\_2009-03-15\_minutes\.txt](<../data/corpus/meeting_minutes/meeting_2009-03-15_minutes.txt>) |
| REQ-099 | REQ-34a1eaa1900a594cac5cddf13c714446576eeb94b38765a0355143c101731d7b | CAND-ea1b01fdd99d1e6192c5ad85e8695295da619a1d79c905196004279917ef9048 | [conversations/conv\_pines019\_020\_missing\_intransit\.eml](<../data/corpus/conversations/conv_pines019_020_missing_intransit.eml>) |
| REQ-100 | REQ-35aa884d8e4aff3cc0adfc00c502811576ad4bf68543ab9b73bbe9185ec5267f | CAND-e024e581f97344a28220dcff0c702142f6ab5e180624d98eee19c50d0ee4a4a4 | [survey\_results\_2009\.txt](<../data/corpus/survey_results_2009.txt>) |
| REQ-101 | REQ-366acd8de9991f7b1b902f62eb16b4c7d116a95773340ac451aa82a39b46c40f | CAND-e7dc48f1f7486b08729be4d9c9a963cd75edda81fcc0d6154b90e05a132072bb, CAND-f8a00a933039e350d051618f0403572471fa3724798adb494f5251c15d3248ee | [conversations/conv\_pines018\_item\_transfer\.eml](<../data/corpus/conversations/conv_pines018_item_transfer.eml>), [interview\_cataloging\_2009-05-08\.txt](<../data/corpus/interview_cataloging_2009-05-08.txt>) |
| REQ-102 | REQ-37103089c88f5232dfc39c363dcc36f2c1ab1a2c3bedba0d86e04074836cf84f | CAND-7b96dba9e8b242de1165edea5425b8f3237fd2c85d722793a4a5c50eb86f0d8a | [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>) |
| REQ-103 | REQ-372718b91bcf891c549cb877aba944e6ef70f32a059e3c0d8fd66c601e415e1e | CAND-1e6aaedd25c5edf80c44de4d95c4e3be16db0017f209f2d85e06ef29bf08a167 | [conversations/conv\_pines018\_item\_transfer\.eml](<../data/corpus/conversations/conv_pines018_item_transfer.eml>) |
| REQ-104 | REQ-3753a58491e0435248647e735e6d290759afdc222f5e161c2933d3ee858d361a | CAND-bf07a55a9de5edf14234f3021361bf7b3a2c572f0796cd0501188b41e6df1e0e | [evergreen\_reference\_2009\.txt](<../data/corpus/evergreen_reference_2009.txt>) |
| REQ-105 | REQ-38689a78b31d9ea480f209d34eac46a9d829d49cf401506d743febe76495c08b | CAND-9f0783ad949c6c6c534033bcc04bee2656d09541c1117cadd924da59d80708db | [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>) |
| REQ-106 | REQ-38715fba26491d543d05df19e4e068aa17ccbd3e5c5bc8e613d6c7499b109837 | CAND-7ff3df2cd1ab48d85ed5b2a87f45e8eafe978f2ba1f32b447d82753c98350297 | [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>) |
| REQ-107 | REQ-38908c17dbfe657f8bcc17896465ebd62dff56e741e92d669b089771cbc12276 | CAND-0d0505711a88919d8fc649aeba575aabb9fcb9f3fe1216ae6bbee236ca33088f | [email\_financial\_reports\.eml](<../data/corpus/email_financial_reports.eml>) |
| REQ-108 | REQ-38ed7b3651926eddb0e7b728a5b9324d4d18b6fd3823c964976f89a492dff1db | CAND-23684841540a2b28d39121747c26d1422265fef96bd82c1e9f9fe6f85ce7b73b, CAND-2c1ac17b11772eddc760b9316d81562b5df03409400e8a1635777bfa806c20fa | [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>) |
| REQ-109 | REQ-393e43f8baabd53a0bc1d6dc59a76eb92b0c45fbf20a7cb81a1f9f440398697e | CAND-caee8ea06096c3f103509ea080a24b00f9c565a4dd4a604061c42e326b4350c8 | [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>) |
| REQ-110 | REQ-395bac6a71d09fb251fbc5caaddd5f405e0d0b540f69db7f83843f375075fe70 | CAND-e39c0ae6b96bf38e1f06af791143eacd0741bb6a021ad5470e26e0156d1b9a91 | [survey\_results\_2009\.txt](<../data/corpus/survey_results_2009.txt>) |
| REQ-111 | REQ-39642b8eda3fee136e34f247e078cc9156e505ad21d38aff7ff1fe0879455753 | CAND-695c1810eb76dff409ae00f571f17bcb0ab32a686c2f786412fc7fd293e629a9 | [email\_financial\_reports\.eml](<../data/corpus/email_financial_reports.eml>) |
| REQ-112 | REQ-39774cae3d3ee660f182703d232d92e9ad3976734feb6db96f39414355d3ecfa | CAND-305233fb98b5e408bac226e8caa51a64bf48c6c730f5fb6e23f51a906d108d64 | [interview\_sysadmin\_2009-05-10\.txt](<../data/corpus/interview_sysadmin_2009-05-10.txt>) |
| REQ-113 | REQ-397b067f8434592807aa035f151791afca49fdc9b8050386071fc66a710586c4 | CAND-06a0e9425321185a882fbcf9f10b62169d11fb29380e8ab0e91cdef9cc588f2c | [email\_staff\_login\.eml](<../data/corpus/email_staff_login.eml>) |
| REQ-114 | REQ-399a1800f44501f2eb83c88c74b40ec0a04d5a4dc209b28add9a9a84aabb65e8 | CAND-467101f54bbe6e3325f4f1fd83d695fd7f75eab5fec60fd15085f8104fc6d64a | [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>) |
| REQ-115 | REQ-3a89f0685c9ca2a243f211a3513ee0cbb0535b7b746e75f7b813d74be6697bf8 | CAND-a8a4c3002bf5ed0f128f43d803a29357986105d50dcb22b33156b7fa279318c5 | [meeting\_tech\_subcommittee\_2009-06-30\.txt](<../data/corpus/meeting_tech_subcommittee_2009-06-30.txt>) |
| REQ-116 | REQ-3af0b484058c2db4bac3c37131ff0b9a9211d8cb2030d11cf68dd7ca16736bf7 | CAND-0f71d6ae4a2f21a35cbc3fb37df177e7ee2ac6faf5d6329d991875f2dab95ae1, CAND-200915cb8e62a43b75ba68dbce47aa9ee2a0d143d0c8119ea3601874f9658605, CAND-40de2f446078e78eeb0d93ac9779a18b5b498031a49e0ebd19f37b04c758e5f9, CAND-8460e580561c835a4376c2b7475b737a8d19e4cedf0997859fda03965df1b8ad, CAND-a182d27c59420b2d39c368b1da24b3dc42c24d0a707de73064803d3abdc38573, CAND-c1640a340428f3c1ae9f0cbf3a802f3b709d235645676901be42d8e7de484e7b, CAND-ee4c2da9030b1c4d91bd3a6cea039204e6fcb4df7ee122dde1831e0828ff6ba3, CAND-f08e64a9bc1879f0e10d659ac465d9abec5a4b65eadbd32708bc79ed2662f381 | [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>), [email\_report\_features\.eml](<../data/corpus/email_report_features.eml>), [evergreen\_reference\_2009\.txt](<../data/corpus/evergreen_reference_2009.txt>), [meeting\_minutes/meeting\_2009-07-20\_minutes\.txt](<../data/corpus/meeting_minutes/meeting_2009-07-20_minutes.txt>), [survey\_results\_2009\.txt](<../data/corpus/survey_results_2009.txt>) |
| REQ-117 | REQ-3b213e28192a44128ced93d988e8d0b9d968dfab5d71699f10f9d912a049fbc2 | CAND-0d9c44a06081f598aac73c876b5af8787a3bc509b100190099b746341dad8838 | [meeting\_minutes/meeting\_2009-07-20\_minutes\.txt](<../data/corpus/meeting_minutes/meeting_2009-07-20_minutes.txt>) |
| REQ-118 | REQ-3bf07cb0143e38bb1d75c52bd48bae63c9b707541478f3f7d77086352a6ca180 | CAND-b3cc501f18bdd27a060b221548d9ac3c38dc03bd134d0bf2fcbff54d4556467c | [meeting\_minutes/meeting\_2009-07-20\_minutes\.txt](<../data/corpus/meeting_minutes/meeting_2009-07-20_minutes.txt>) |
| REQ-119 | REQ-3d202b858d32bd0ca9658fdf2f6fb50255ff8ec608ac4cc650000085dac6cf4a | CAND-e82deb9bad228f3245534e34cc11e37cf4c7b3ffe8670334309009e7914c6cf7, CAND-e97ab96d3d7908c20e128f7287bb05f4d17905935ab5ab00d8ec1cba750db89b | [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>), [meeting\_minutes/meeting\_2009-07-20\_minutes\.txt](<../data/corpus/meeting_minutes/meeting_2009-07-20_minutes.txt>) |
| REQ-120 | REQ-3dc810ade1a2b2ec3588905fa4fb2b7352152c75c2bc715cdddc74c8f13b382c | CAND-42e202ad68ba22aefd289dde1d471446f2f437b14e4be84d70afc2a38609de3e | [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>) |
| REQ-121 | REQ-3de91974e63c5e566c18239444e0cea7bdf96e8eaf6e7fddc7fb785dcf37db7d | CAND-4980a6242cca693c0a0cdd0670902b125d612a318bbfc24e00f168213b3d0556 | [conversations/conv\_pines022\_deletions\.eml](<../data/corpus/conversations/conv_pines022_deletions.eml>) |
| REQ-122 | REQ-3e49c8b537afa6ce741017e6e9c21a6b9c39c90187db38f7044260b40ef113ba | CAND-08e04c8a9f19b91aeb06b44abf6183ca7a64bf13e951c5b371deef86385d5c86 | [conversations/conv\_pines018\_item\_transfer\.eml](<../data/corpus/conversations/conv_pines018_item_transfer.eml>) |
| REQ-123 | REQ-3f2e043f9b40b51c37127bb669d26c2ba6aed07bfc48ce7c8e113a1b8fdcd815 | CAND-3d32dc0af13b53200ebab059507c3d08e6e523ee85804d09da15c1b723bfd643 | [conversations/conv\_pines022\_deletions\.eml](<../data/corpus/conversations/conv_pines022_deletions.eml>) |
| REQ-124 | REQ-3f713a839858bba3c17eb2601f1e9bc2e829bc7746d169628bba5576ab5bc651 | CAND-c6b17d5e787a0ca9b49073d30959b0f0558e5e16f10878bbdd3af0332fd33c3d | [conversations/conv\_pines018\_item\_transfer\.eml](<../data/corpus/conversations/conv_pines018_item_transfer.eml>) |
| REQ-125 | REQ-3fd9b55e518abf077ca655659d2be48c202adab908f3cb71f3ae730ca0fa7425 | CAND-a942896713be0071e1f2784394f893f3a1f420ed0c9023e1ed37544ca36a8565 | [meeting\_minutes/meeting\_2009-07-20\_minutes\.txt](<../data/corpus/meeting_minutes/meeting_2009-07-20_minutes.txt>) |
| REQ-126 | REQ-40626f32b12f2d6e58dd91a375db01bedf6ad72564a1408881a54547119f2442 | CAND-d73d76a7a303eb099f5778ba95feebc9eb4231f0a6016b80af1abb9e7f71ff06 | [conversations/conv\_pines022\_deletions\.eml](<../data/corpus/conversations/conv_pines022_deletions.eml>) |
| REQ-127 | REQ-41c168e28bc9f42f2118a88855ca61268ae666b1b0c8a66e3ab8cd2a8a266125 | CAND-b9de88da4a2a6a1449fad30414db6f69f115d002bd852fdb9af0ee10cfea38cb | [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>) |
| REQ-128 | REQ-4253b851b4ccc8507247fc35654eb718832f15a36063f840ef3780cb3fa766d5 | CAND-6487a6e31bce657f5f66ab93908852be7812aa44794b01cf882b3771ea654c5f | [conversations/conv\_pines015\_capacity\_interface\.eml](<../data/corpus/conversations/conv_pines015_capacity_interface.eml>) |
| REQ-129 | REQ-42618db7e795451bf5d8659b55422ce247db23533c3d2ee50cae20d55409245f | CAND-4b791422a65411fbcb36535fce939b380327eb66c475a5777568292a75c9d3d8 | [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>) |
| REQ-130 | REQ-43e5e92e2408a724dbbdb56548f4f3ce38d4f6cbf35c13249c060347cbb35b03 | CAND-e6412b0ca42a6d9f6226689adb8800cb150f5d721ba08bf5b7b5c51702aadd7f | [meeting\_minutes/meeting\_2009-07-20\_minutes\.txt](<../data/corpus/meeting_minutes/meeting_2009-07-20_minutes.txt>) |
| REQ-131 | REQ-451641be1b31209b34c27ab707627d3a3836b414f57ebcdda48f39bc3c1e18ae | CAND-fd57729a1d264b5f4314ca99ec831188df4fc12727598d04794a6410f72d2b5a | [email\_financial\_reports\.eml](<../data/corpus/email_financial_reports.eml>) |
| REQ-132 | REQ-45a97b4d662a97503be8b357d9c5233c25e2b5e8576f1cd8442e020f1e9c0ef5 | CAND-014cd73d14dd417db704dbc7e60d78d59534bd8bc38f2e1eda9e9aac965124b9 | [interview\_cataloging\_2009-05-08\.txt](<../data/corpus/interview_cataloging_2009-05-08.txt>) |
| REQ-133 | REQ-45a97b4d662a97503be8b357d9c5233c25e2b5e8576f1cd8442e020f1e9c0ef5-new | CAND-9232a3279103eae4acab816cf83f390ee00d3e93d8ee9f6d9f86842f468a9db6 | [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>) |
| REQ-134 | REQ-467092eba9ef2159fc541702b382c93613fe45f99e6bd71651d544d415fc549b | CAND-4676a15703b2d8a116563ec9a3c675df8bd97451900302089ed9a04afc7655d8 | [evergreen\_reference\_2009\.txt](<../data/corpus/evergreen_reference_2009.txt>) |
| REQ-135 | REQ-4672df0613679a6e6ae21e10378f8f08f66c2939bc25297d916c438a95a601f2 | CAND-c115b03dfb31ef8d832cd9bfd9a14ce7be41f2832fcb9af2bbbca26443c35bc1 | [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>) |
| REQ-136 | REQ-46af57c3953900c8cfab95b4427e28dfac06e75e994179cc886823776e20ccec | CAND-4597dfcaba5a030e50a217574d5d5f569d561513a2a2d841057068b8f660705a | [meeting\_minutes/meeting\_2009-03-15\_minutes\.txt](<../data/corpus/meeting_minutes/meeting_2009-03-15_minutes.txt>) |
| REQ-137 | REQ-4712dfa1344a1e1fa9a93331144bbf799cdd2de086893902540cf4d2aab1925e | CAND-a8c4505902f52cdc9f24b45cc550f77ac08c2e0bd4849733de19ba5df3b79dcd | [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>) |
| REQ-138 | REQ-4749a037a3a6cf57659fe8fdbda89ccac8129bd823ddb037542dafbf79d73867 | CAND-7cb4d4b570f0c55a2909409c584dac5f16ed16b19d1c09fbee8ba04ee368876c, CAND-84b7320cea15e0202dbd7921f79d0e207b0a6d0dabdc1df822988a784610517a | [evergreen\_reference\_2009\.txt](<../data/corpus/evergreen_reference_2009.txt>), [survey\_results\_2009\.txt](<../data/corpus/survey_results_2009.txt>) |
| REQ-139 | REQ-4782640a579b647a510ccf0f1afeaa9afc451704838df6cfda1a04d04addd510 | CAND-c44959e9d1d15c61674532cb0eff5d5a9621844f7e7f38426a672c65c60d463f | [meeting\_minutes/meeting\_2009-07-20\_minutes\.txt](<../data/corpus/meeting_minutes/meeting_2009-07-20_minutes.txt>) |
| REQ-140 | REQ-47ac0149ece1a6c6de30f063c8b6b59a9db8bb87af3d9341b1658b731649d4c6 | CAND-8f89b91dbe18063602db77c1b389247140ac3021c1d4464e7c7ed695fae76ecf | [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>) |
| REQ-141 | REQ-47efd0163702e0d88a82d2b1029efa9a04bbd49afd57a9b5d1249baa8da524c0 | CAND-650fc6e0aa0a4fcd0b185e822132eec9c32f12a0d60614eac4a044bc6ddcee68 | [conversations/conv\_pines014\_material\_volume\.eml](<../data/corpus/conversations/conv_pines014_material_volume.eml>) |
| REQ-142 | REQ-487c3d1860dba77b192c6005f68f8be44fd4b47b9039e06c7f2d2fae6c0dcec9 | CAND-cecc24ea5db477cc5885d210bf68b60376538c540d2fc56994077685f5c0e86a | [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>) |
| REQ-143 | REQ-4a201812ab33b8e7bf1154550db6de5777a453599df09cb6c7c4859cecda9310 | CAND-5fe27c79a2cd4b0ee6ee91782de7c1880dc7a63426751a6bc42016661d38f6e5 | [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>) |
| REQ-144 | REQ-4a32a3b56eead0606939e075d5ad8d6d97c1ac5872512068c555dc81bd8d4e47 | CAND-ca37c9c8877e4d9bd5ffac768ed2bb4aedc5611a24174efec8dfaf867d4389cd | [interview\_sysadmin\_2009-05-10\.txt](<../data/corpus/interview_sysadmin_2009-05-10.txt>) |
| REQ-145 | REQ-4ae4b0f852a72bb24649b10215b3c932066084b34a91af5d5260738fdcd92c04 | CAND-16470d484872ca45a239e593eba521e3c52ff83981e3ed3f107e7becef78ed92 | [conversations/conv\_pines014\_material\_volume\.eml](<../data/corpus/conversations/conv_pines014_material_volume.eml>) |
| REQ-146 | REQ-4d1615e1c31c931c9b0acc9439f3400654b06b41649b4d34dcd36c139f1555e2 | CAND-4729a2de940a964bcf1dad9811be4a392ca7a93a7035dd081a51c4b0e06f343e | [conversations/conv\_pines016\_shelf\_space\.eml](<../data/corpus/conversations/conv_pines016_shelf_space.eml>) |
| REQ-147 | REQ-4d442a204e10ac10ff40e537dac866b57793698dc709a714969227923af74261 | CAND-4b6f691f03cd44214373992be9b5a649fc877ca3c211996efbc0fb9e1559b3a3 | [meeting\_minutes/meeting\_2009-03-15\_minutes\.txt](<../data/corpus/meeting_minutes/meeting_2009-03-15_minutes.txt>) |
| REQ-148 | REQ-4d5162677abd8705447c4346c74a78a1755a8b15432b40710864dcd71f8d4c2f | CAND-c444007ee0eb5c3772b93b78b76a23920a2f6f3442315248a231257b70b1742b | [interview\_cataloging\_2009-05-08\.txt](<../data/corpus/interview_cataloging_2009-05-08.txt>) |
| REQ-149 | REQ-4d66266bac966e927bd99ee1b9c2da38b27a50bf7a59d6c2140484bf2b555000 | CAND-df037f635a0dc9f1d9d540a6282238148a93bda09a04d53c0780e6e3a4a3a60a | [survey\_results\_2009\.txt](<../data/corpus/survey_results_2009.txt>) |
| REQ-150 | REQ-4dfd9d4432362235ee82b22831ea18f3f62b5462a85968600faf8c9a5cc2a58c | CAND-1d880959b4ded45670c438208f21d25a894a3dea2d487d6e548224e70dbb2ebc | [conversations/conv\_pines024\_inactive\_patrons\.eml](<../data/corpus/conversations/conv_pines024_inactive_patrons.eml>) |
| REQ-151 | REQ-4ea945a733673579c14dd2101929cf1c09dac67aa67c424a051b9d9c64836ba4 | CAND-15e2a1c9042548124ec97802868fdbbc4561f092805ed8495e0ca15f71da1da0 | [conversations/conv\_pines018\_item\_transfer\.eml](<../data/corpus/conversations/conv_pines018_item_transfer.eml>) |
| REQ-152 | REQ-5005d3553e353a093d96fbd291dac28e4b3f2a1703167335862dbf279ca05911 | CAND-ed0d5044a14f8ebf45544607c5c5db86f113de212f72f4135483bc669135e7a2 | [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>) |
| REQ-153 | REQ-50a19f69485d02c73221e3f754991f962044f0aa3213e2261542547bcf79f406 | CAND-f09593ec4afc503d109b89a44ef7bb3bd3ffa28032ebfe5e94d87ec6c8bd4397 | [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>) |
| REQ-154 | REQ-51ee1fa512e19ee9aa32ae5d74990db91ec16540cf05fe7789ef8eda83c1a13a | CAND-2b12907af86263458da5cbceba1e5127770b7838992433af7b3bc956c8a3961d | [meeting\_minutes/meeting\_2009-03-15\_minutes\.txt](<../data/corpus/meeting_minutes/meeting_2009-03-15_minutes.txt>) |
| REQ-155 | REQ-5274ec341a1fdb292ddf486244336728d149dd475eba593b83292ec7e8c22e59 | CAND-42dcb2d75232af264ab8bddc6ccad907def82aac7834b46850b081e3f596b7f4 | [evergreen\_reference\_2009\.txt](<../data/corpus/evergreen_reference_2009.txt>) |
| REQ-156 | REQ-5360d814680e583f014a2a33513053acba6117d665018cd970055dad81907929 | CAND-5582fe9c6ce9fd087858406d395f764c51f7cc91d2aa0e0db3419dc635b6bb68 | [interview\_sysadmin\_2009-05-10\.txt](<../data/corpus/interview_sysadmin_2009-05-10.txt>) |
| REQ-157 | REQ-5360d814680e583f014a2a33513053acba6117d665018cd970055dad81907929-new | CAND-5761e6541b0fee1705673a252c4526af721fbba5503ba12feec1e69d0f905607 | [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>) |
| REQ-158 | REQ-53edbd5b459ca92389a3b9d794048866d005987a0f34750ae8df494f41026176 | CAND-d2e01e95a4df9cee9e20c98278922ec90e8fb93c7a1fe4183a4709b80389e417 | [evergreen\_reference\_2009\.txt](<../data/corpus/evergreen_reference_2009.txt>) |
| REQ-159 | REQ-5435212810ea77283733034c7e6330d76bdb493cddd6bccfe8b815806aaab96e | CAND-bc6cb2227ee9499878ac5afd81ff8503bb90feba527454f6b03d7d4c7a4cd3e1 | [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>) |
| REQ-160 | REQ-543cc4a79be0d916e2dc6465f1093e49e4d766be10bd73fffbbc291b6b71de5c | CAND-58949b6fa23f8b4aff26acb554063793d18f55f519bd9c371c7221921fc41617 | [conversations/conv\_pines019\_020\_missing\_intransit\.eml](<../data/corpus/conversations/conv_pines019_020_missing_intransit.eml>) |
| REQ-161 | REQ-5478728780de0be7580bad7342657c17f6ca590b026cada458a95097ba8b0344 | CAND-2c397cfa61fb4cb35f7f73277ca660df6ab76658283022e032e32261e2c4471c | [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>) |
| REQ-162 | REQ-54dc5165886bad36793b9ce63cc2c0de9e7a6429988feffbe9a4db3aa9497e1c | CAND-13a693039b11df8ad619da643f0625430a9375b6c70529cb4fa7f6d21aae9798 | [meeting\_minutes/meeting\_2009-07-20\_minutes\.txt](<../data/corpus/meeting_minutes/meeting_2009-07-20_minutes.txt>) |
| REQ-163 | REQ-54e07fdc15db837cfe321435c5f67da2f756b02cbe3c2760bed2587876f6fe52 | CAND-d9d951bff6c0e48140b438229837669bcc49faa60157b69760dfbc272e608b81 | [conversations/conv\_pines022\_deletions\.eml](<../data/corpus/conversations/conv_pines022_deletions.eml>) |
| REQ-164 | REQ-569cf887e9de0b9ee88dd40739ab7ff4d4928123f85df8a63b3b7c14b10e78ef | CAND-8d7b692a9d051a2f77d1e15f7fae75aa5453ced07013ccf2512fcdbb741ec17b | [conversations/conv\_pines018\_item\_transfer\.eml](<../data/corpus/conversations/conv_pines018_item_transfer.eml>) |
| REQ-165 | REQ-5761a15d2357c158faad812c8ea64f1b66230647e0b8b67415e97554e92c2199 | CAND-800696766ba618c2c9136a4fb09023b2b63d145ac05900376918042ff99751ac | [evergreen\_reference\_2009\.txt](<../data/corpus/evergreen_reference_2009.txt>) |
| REQ-166 | REQ-57d4471cbfbb6a1e9bb81db9db1d22628d2eef73c0571b9a984287b69aa4a311 | CAND-87f6537aa97ea78cb30dfedef331ba005416a81ba2c263775aea047f08fdee01 | [meeting\_minutes/meeting\_2009-07-20\_minutes\.txt](<../data/corpus/meeting_minutes/meeting_2009-07-20_minutes.txt>) |
| REQ-167 | REQ-57d547fd6ff212c9aec7fd87134baa5066d84fc33e8040212bf6d41b12ded96f | CAND-e5115ecaf6920136b1dfe042bfd2f53f8cae050f03c89f45f59a98c8924a2fc1 | [meeting\_tech\_subcommittee\_2009-06-30\.txt](<../data/corpus/meeting_tech_subcommittee_2009-06-30.txt>) |
| REQ-168 | REQ-57fb8a54977b6db12b57e20498ac9064868dc8aee8dcd74d0926e9ced8ba31cb | CAND-369c6c290940ad6a6db39f2a442d83c2509ddad3633f54eec6232091900923f9 | [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>) |
| REQ-169 | REQ-589c3576aebfacb7b5807625c034e0a61c7f3f01de66ed30aeb47cd59177c767 | CAND-bbb60c3bd1e345099f66d8da87f953cd8cd5582b8aaf9a348e83c816b0219409 | [conversations/conv\_pines021\_item\_purging\.eml](<../data/corpus/conversations/conv_pines021_item_purging.eml>) |
| REQ-170 | REQ-591bc8ca11ea6dc208fde918b44c2e8ad2095be7c77dca7f8454b9fd5e63cd04 | CAND-9edfcf7595c2da9e90872e6648b71b664e9c63f27fb0ca1c71576927cdf47ecc | [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>) |
| REQ-171 | REQ-599ef7ad7e23b8152747ea9b240ba344c70cf6771ee0ef8a59ab08bb411a8964 | CAND-aa81220e81bfbcc08b052a4c6d30a8014be4c1806c478255a4bb64550c0aaab5 | [meeting\_minutes/meeting\_2009-07-20\_minutes\.txt](<../data/corpus/meeting_minutes/meeting_2009-07-20_minutes.txt>) |
| REQ-172 | REQ-5a284fdd2acf85ac2a5fa309add5563ac5ee71025a228f5a93d5f91f421666de | CAND-86364bc65fe5795bab9b2afd62dc3b563b55ce8de564914f84eaaf3d3552b8be | [interview\_sysadmin\_2009-05-10\.txt](<../data/corpus/interview_sysadmin_2009-05-10.txt>) |
| REQ-173 | REQ-5a93004d416ccf73bd950141c08247c1c6dd0b9d8bdf01558a37b7535151fd1a | CAND-3d7d1adf6265c0cb70ba8626dc95e7c75b73d00c51300a117c73b6c6797c39de | [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>) |
| REQ-174 | REQ-5afd585d9b2f57d52413965c311f679cd5c7c541f4e9323fe937e5f9ec888cd6 | CAND-8a6f0b6380454602a1b0b0e0996bd5d1dd0c612bc792d19725dc88d5dc279636 | [evergreen\_reference\_2009\.txt](<../data/corpus/evergreen_reference_2009.txt>) |
| REQ-175 | REQ-5b48a59183426f580c57b6ce999aa91e6114d0ef935332cbe18886261347266b | CAND-28ec7e2e9f62873d7c2eaa7a5ce673f1c0b31b87d45039e66ab156f2af41bd4a | [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>) |
| REQ-176 | REQ-5b7f75eb32b7d2d3111fda99ebbaaaeb015a65c79aeaf381f972db998f97d783 | CAND-e2d8a90f1125d0274258568a115d6b073ce5208aa5d4e655569a8c7b6fa7af05 | [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>) |
| REQ-177 | REQ-5b89e4b3283430f8a9ee73a302b4203724a9941d38441c9049a46d9f90b513cd | CAND-5b1ba79e438750abc733e3c32807040cae32803724b67c1bb9181197eb98eb74 | [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>) |
| REQ-178 | REQ-5bd98881a310ed27591aae26e24bbb8768c56675bd8037422ee1590ab9baaa97 | CAND-b868676e9882ab79898743955e3ddf5a37a71a52fefe5be5d8b541420cbe0b1e | [interview\_cataloging\_2009-05-08\.txt](<../data/corpus/interview_cataloging_2009-05-08.txt>) |
| REQ-179 | REQ-5bf8de1177bd44fdf466b4b93bd0a78b33e82d5d075efbf515767989daa898db | CAND-0894ac3888f6c691fab1653bd623b85a5aefe94711183328344e9834c14dee82 | [conversations/conv\_pines018\_item\_transfer\.eml](<../data/corpus/conversations/conv_pines018_item_transfer.eml>) |
| REQ-180 | REQ-5c605d382a1dcee3081b02e18075da93386a3e9c410539a8d71481a41b218f97 | CAND-a5eca48fbf62dfb6cb539b330c1c9679bc5108bae97c0a7d35bbfa1d5076f69f | [evergreen\_reference\_2009\.txt](<../data/corpus/evergreen_reference_2009.txt>) |
| REQ-181 | REQ-5cfb0dc5742fa3cb607c8f6c2d7c664361e0f4fca4dc083389d678255e4d20e0 | CAND-8f4ab5a0f27bcce171b64e4a7989b6f7b263efd87d7050b53102302c3b1ab5a9 | [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>) |
| REQ-182 | REQ-5d12a8386e04e1bccd898a6b601866da3df48a462fdf976ea9d6d3b07bdb4443 | CAND-5a3fdea2897edeeabf8d04af154117b990ec6f7b83fca597595119b419656fe2 | [conversations/conv\_pines024\_inactive\_patrons\.eml](<../data/corpus/conversations/conv_pines024_inactive_patrons.eml>) |
| REQ-183 | REQ-5d200b5f411347a1ae724837856c65f114262a04b6ffb7e6acb4c4bb35703dba | CAND-30db376939b250eefe320bddad610e9b173cae36564c9184f20354e1b5b1c2c9 | [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>) |
| REQ-184 | REQ-5dae62739cb9193fac81f21e9bb5fc95e6b8caac397300a4d5794d8b89aa54ce | CAND-017827c3eed0eb15eaa895056eae71c2ab1f8c8dd16c835a5c0e1f9dd93e24e5 | [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>) |
| REQ-185 | REQ-5dd637df0254d190379e13a7e74eefa49af71d9370ff0809362ab7b723e5595a | CAND-b5cdcb15e82fc847019ec7a3597a3162084372734de669d37189d989e7a5b4ee | [conversations/conv\_pines018\_item\_transfer\.eml](<../data/corpus/conversations/conv_pines018_item_transfer.eml>) |
| REQ-186 | REQ-5e771e50870e3506a919dd6d073f0b9d48ad3c56cb48f7f09dc9f6ad53ece2e7 | CAND-5d4c3e49c526478bc803fed1e0a75b2117ee9b3fdcb32ef3c5fddfd2177cde81 | [meeting\_minutes/meeting\_2009-03-15\_minutes\.txt](<../data/corpus/meeting_minutes/meeting_2009-03-15_minutes.txt>) |
| REQ-187 | REQ-5f2c8ff886717769aeec82cd97b19e3f52e62c21b4eb706da27aa226082dae96 | CAND-0a9f1160133ccb14eb9bcd025b8f46d252373ed0a30cc5acd6e5906250064d64 | [conversations/conv\_pines018\_item\_transfer\.eml](<../data/corpus/conversations/conv_pines018_item_transfer.eml>) |
| REQ-188 | REQ-5fd6fea533086daf9cb437b66554dd8907feda280ecdeef6a63b923718f61001 | CAND-f52704325b6492235058eae00ee3cfba0e22b93397bca5e607a55bab9ae53a52 | [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>) |
| REQ-189 | REQ-602064e99e776378e6114c0a1a455ed14b5949d8f1ffae03f8458ffaf1672422 | CAND-59c960798b3709e469a8dafc5a451bf9e5193ec69eea2ca93be96efc30ede3e7 | [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>) |
| REQ-190 | REQ-60428b53a0ec5a3f58130ad395cc7444396eebf5af4fdc967546abea6d5b8d59 | CAND-616e5417ae8350a7d2a5c3067d853a74b04b6ff914caac37a25163d9764a6ea7 | [evergreen\_reference\_2009\.txt](<../data/corpus/evergreen_reference_2009.txt>) |
| REQ-191 | REQ-612f860863b073151afb50afc992153a1eac4c946e867a507a1d3da79697f1c0 | CAND-fb5c37891da74cb7d7bed2c72a7e15e7278b5c71ad4ad30ba252a58a575de963 | [evergreen\_reference\_2009\.txt](<../data/corpus/evergreen_reference_2009.txt>) |
| REQ-192 | REQ-6179da66c87f0417bd0cadc989f3fcefd1be1eea044bd602b99b69765d2df261 | CAND-6696fecd6573f7f647894da5f27c46ff2f2b484d1b8b0f761af83c0c5ab51a43 | [conversations/conv\_pines019\_020\_missing\_intransit\.eml](<../data/corpus/conversations/conv_pines019_020_missing_intransit.eml>) |
| REQ-193 | REQ-621c7b4b493f852210632e3630560b41111338716b7188a5414e5ac363130401 | CAND-0d9b4b8af2d1d040cf7f2526e403c8d1e67217a3a248ade4106438fc2cd0ab03 | [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>) |
| REQ-194 | REQ-6293a5e0dd8f1acbfbff85ef30ca8878cf8d661121ddd3167f6a7217aecba717 | CAND-da968ff4766f186ea30fc73e2596c1298415198e067063b8dd1a066f5a812ace | [meeting\_minutes/meeting\_2009-07-20\_minutes\.txt](<../data/corpus/meeting_minutes/meeting_2009-07-20_minutes.txt>) |
| REQ-195 | REQ-62beac27fe28410d78c0303986a176d451292baed407e42c4f0420ff1f3ec915 | CAND-d47876d538df701a226c072d724c60792ae217900399576a28e03064dc718087 | [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>) |
| REQ-196 | REQ-639b75f2232b422699bae6fbfbcc0b33927c9d407c66d670db9a927932483f89 | CAND-fd80fac8d5e6102026d39da2dfa5206bff790fb9d9ca940117e4f201e4a1c3c3 | [meeting\_minutes/meeting\_2009-03-15\_minutes\.txt](<../data/corpus/meeting_minutes/meeting_2009-03-15_minutes.txt>) |
| REQ-197 | REQ-64adc45b62a0adeee8872a8ce2ec779342e6c0bd68bd45bc15314bc308c86458 | CAND-e462dabc37f958dcbf7672c9138236edf7582ebba84ff06c420a75165f77ad0e | [meeting\_minutes/meeting\_2009-03-15\_minutes\.txt](<../data/corpus/meeting_minutes/meeting_2009-03-15_minutes.txt>) |
| REQ-198 | REQ-65badf429e7052b0df4fa26d58eed3317e69ff5948598c6e323300b5d343dd62 | CAND-b7b00d863ed78b634f3e33820989792b2e3b8e53b323b074e41bb47a942dd548 | [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>) |
| REQ-199 | REQ-66259eeb658e0ea5b8f23220f67db490ea0fc5fc54446cc5ebb6134458b6823b | CAND-8f1c19d45b9073470c0da42f89684e4ab23018ef9076d075f88ae6a349770dab | [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>) |
| REQ-200 | REQ-66e6a5d7fd0934baf00c674101170b84d28bf0dad8a44657a32166eca1238745 | CAND-d506611962290660a9487a07c28c927e422444f70018992b80c7aec89aba5a98 | [meeting\_minutes/meeting\_2009-03-15\_minutes\.txt](<../data/corpus/meeting_minutes/meeting_2009-03-15_minutes.txt>) |
| REQ-201 | REQ-6727386b1b5f3b1aad9757665f43a8e1c49fc0d5e484cc5dc4468425f88f7eca | CAND-c36378b0868747bcdc9f5ecc8e701daf4854d626694dc9ae1f7a9b5e562cd73e | [conversations/conv\_pines014\_material\_volume\.eml](<../data/corpus/conversations/conv_pines014_material_volume.eml>) |
| REQ-202 | REQ-68c19a7a8f1c5f6d44675a054553560d4772f4867db99fd4799dee01b53a323e | CAND-677a4b1257a222cc56e8f4c8c3f24ea4728da6b12ba02d1a16f2a0ee89e8cc18 | [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>) |
| REQ-203 | REQ-68d84947254ab8d744707e5dc721c2db41e8ae7424e4465632eb5a7b903165a6 | CAND-64fcf15e64cf998b31773d0a516776771d9ad69c3b8075caad278de0eb85ea0e | [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>) |
| REQ-204 | REQ-69f74f64cabdcadefe6388276b5592e03cb9fbb35c6eba3a39cb0a254c14bc39 | CAND-1c027e89807cec1ef5670ce2cbde759ac8e2d080781acf61afd38ca66ea85c45 | [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>) |
| REQ-205 | REQ-6a1dbfd822fabd0295f7513c5723a9769f530a76696a84f1f1a639cb0a1979fc | CAND-775b519373198af56fa52273a4ebaafe582d46785615ae3fc014867e0bb1dcdb | [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>) |
| REQ-206 | REQ-6b402aa5f7e63c1bf5ab9d3d5421196826aabd03c888d564b85824bfd3f760ab | CAND-bfd13fba1a8e144a998546ce2999f68855df2c92e5c242b493475cd4a412b3d2 | [conversations/conv\_pines014\_material\_volume\.eml](<../data/corpus/conversations/conv_pines014_material_volume.eml>) |
| REQ-207 | REQ-6b4ac7c91043bef6198e290d39c4af05732d1ef2a6550572638314ad791e9a76 | CAND-c6c02c59a7e9eb7b5bafe756835a8478b5dce48ad7d6e3884e6f4634e22d83b8 | [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>) |
| REQ-208 | REQ-6b51df2613c7d1c37d5481b1f579482239dd0d76e1125d39c737e0af2b8bccae | CAND-4f6985c368ec8194fbadb8ea2a141725bc150b4f0e8127c9a1adb3988d0b2219 | [evergreen\_reference\_2009\.txt](<../data/corpus/evergreen_reference_2009.txt>) |
| REQ-209 | REQ-6c060665182d4ef51a6fb5a33e09fedd5d78f55944731f5f54d48168b4395ca9 | CAND-1dda307ca69a73196365fb0a88fffde3900af53bf77324997fb3db47b0305879 | [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>) |
| REQ-210 | REQ-6c95f6fdb3caa54ba215292496ef4b0f9c1559a345faf708fc3fa212ae6981f2 | CAND-3cdeaada135c9a0bcc8b849407b54ee0742e9283779463dd5c31a8318defba7f | [interview\_sysadmin\_2009-05-10\.txt](<../data/corpus/interview_sysadmin_2009-05-10.txt>) |
| REQ-211 | REQ-6cbfb8b74be736536146daba8b31706978ba34d43ba390fc90eff2cfa95fb461 | CAND-d8be353b42119d356e43ef9018d1642704f8702353d40e30b25ecf5fa2e720a6 | [conversations/conv\_pines016\_shelf\_space\.eml](<../data/corpus/conversations/conv_pines016_shelf_space.eml>) |
| REQ-212 | REQ-6cde243ede2410058103383d28345877d78037653b2f5674e57ab9e349d993be | CAND-e3f98bc05372108041f9475ee997e2346230d8b95fb43ad1992b0c45a1f5289f | [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>) |
| REQ-213 | REQ-6d646c6cee6e4425ad99cd1b86247521c86f3f318d6a3dc2d3cd31fe5d9f5e95 | CAND-863a43fb822dbf32bec12103ca27b01b6b574eb9894bb3e9ea37efc203c03ca5 | [conversations/conv\_pines014\_material\_volume\.eml](<../data/corpus/conversations/conv_pines014_material_volume.eml>) |
| REQ-214 | REQ-6edec70821e73c8037c2cce8852e7af21a4b4d886c296a36b0c98f93dfe77cf9 | CAND-034fecf821b645588e68748637bffd60073f797d5ef00e8ea0a60737710ee722 | [evergreen\_reference\_2009\.txt](<../data/corpus/evergreen_reference_2009.txt>) |
| REQ-215 | REQ-6f4f8f81f9f39ea5a6f385afb79b3904d261f9867fd88d2568bdea51d1a8b276 | CAND-55ea828708012ebe9e6b43418f4ff583cbb65dc59e307904f51c5ec985bf00ff | [interview\_sysadmin\_2009-05-10\.txt](<../data/corpus/interview_sysadmin_2009-05-10.txt>) |
| REQ-216 | REQ-70059418f0b496a80ec44d5d62fed2f4e62916e07835d6a738b8911d18f03d82 | CAND-9bc83e68a2ac35e88a62b2ea11afa35cb58e25e8664475c70717f96dc03363d1 | [interview\_sysadmin\_2009-05-10\.txt](<../data/corpus/interview_sysadmin_2009-05-10.txt>) |
| REQ-217 | REQ-7030a0338f7d50d821b63e99163ff738eefe84b95bfa84ecd72b3b6ae13962eb | CAND-e4ac68a71049583f93a1b53405330a03486fa061dc63427db0c39f302316ef9a | [conversations/conv\_pines014\_material\_volume\.eml](<../data/corpus/conversations/conv_pines014_material_volume.eml>) |
| REQ-218 | REQ-7053459f4b8c9eec6a72d786f8898e8a44a63dca4a4707dbd90b059b5c00c08b | CAND-3d4dd0a7b7ba5877aba682afa820bdc7fb1e32db02e66281ab2256bd353fe16a | [evergreen\_reference\_2009\.txt](<../data/corpus/evergreen_reference_2009.txt>) |
| REQ-219 | REQ-7077e56b2fa35fae9851b043b8e89e48b5f3693ffc9fdde55e90733427fd3e9a | CAND-1579494ea61bfcbdf1e30b269955d9aa236c97995e6467824e0ee37b61876e88 | [evergreen\_reference\_2009\.txt](<../data/corpus/evergreen_reference_2009.txt>) |
| REQ-220 | REQ-71767e4a8974877aadfa45f23c8c696e073eb556e9109a031ec756199df6bb2b | CAND-a0e8b761f088e244420adc211f725a53a6d1fa056e421e0171e97f5728491795, CAND-a2dbdbdeff31fe58e57ad98855fad7ebd6fd9ff396eb7610eff87f18092eb208 | [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>), [email\_report\_features\.eml](<../data/corpus/email_report_features.eml>) |
| REQ-221 | REQ-71c09d3debbebd25f9b68d843e3e1898a822f74fe5a8b07376e19d8206e10bb2 | CAND-26296051cb9a5061293ad3ff67a1c69578ce0b638a90671b91a4f8309d8cab05 | [meeting\_tech\_subcommittee\_2009-06-30\.txt](<../data/corpus/meeting_tech_subcommittee_2009-06-30.txt>) |
| REQ-222 | REQ-71f581aa1a0bea45a7ce0aa0a3405615a81bf5fe15926091a7d3ee30d8705ca1 | CAND-05b609dfc646cb62f50469db7ec52be926c9da3765d5a861603d491344651570 | [email\_financial\_reports\.eml](<../data/corpus/email_financial_reports.eml>) |
| REQ-223 | REQ-72517b21017ecc724f617421ec665319e4099c979b03605d11db84e254798f17 | CAND-ca15eabcb970b4bf25099cfbc88624bb85b93034616b37921506e81974dc1984 | [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>) |
| REQ-224 | REQ-7269ca0721d9a1bdff9833b93628b75d3383dff8b9b3e9de6208d7c40cdd9670 | CAND-0e2e731ddaee00e55c766fabc7d2a367dfb5b49b02df439c5b7d2b4ea7319787 | [evergreen\_reference\_2009\.txt](<../data/corpus/evergreen_reference_2009.txt>) |
| REQ-225 | REQ-72ae8d0b837aabd6f61f69bd648de8eb13f588365a12e8b20675e5d8f3becc55 | CAND-f60304d962427437cad08cede1fa274f32e442a854a1f026eb4c445808124222 | [interview\_cataloging\_2009-05-08\.txt](<../data/corpus/interview_cataloging_2009-05-08.txt>) |
| REQ-226 | REQ-731e6eec00d9c797e092d41b469d337b790174437f9cdcc4641c345307ab2c5d | CAND-e8143608858e361e828b71c80680fb73f6ad26848ed192453f560c94dd0e8345 | [survey\_results\_2009\.txt](<../data/corpus/survey_results_2009.txt>) |
| REQ-227 | REQ-7320b94faf743c76e2039394f63fddfa2571379becc82d7a437f0ac71a6471c6 | CAND-a8263f024ea52f917468a7739817e59e5f17e73a892c7990c14ddf9e724adbd3 | [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>) |
| REQ-228 | REQ-739373cca6671fc6a6a4dc36883788f53f65cc1432941b852f3ebc76231bb05d | CAND-3dedd3ef9065b0f3c2f4bbf294c62626bdc19a926a29a3c07d8a397446451e74 | [conversations/conv\_pines023\_patron\_characteristics\.eml](<../data/corpus/conversations/conv_pines023_patron_characteristics.eml>) |
| REQ-229 | REQ-73bf767d54af7baceafac0b609b0ed37fe205bd7d086b35f70af7fd246150264 | CAND-773f1da3bb2b506e15ae827523e1e3ae5df320e297fa60cf7786ebb5aa9e26ef | [conversations/conv\_pines021\_item\_purging\.eml](<../data/corpus/conversations/conv_pines021_item_purging.eml>) |
| REQ-230 | REQ-73d2b19304fc933ff7c98c219e28c25aa0810bda1c3df3f24321e0c783982316 | CAND-a1f1b024fd672328a748a87a845eff93e3c3c4b496b0a3a31273fcf3087a391b | [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>) |
| REQ-231 | REQ-73eff4f7560788fe0eb7b2d6b0d16af9462694379777ef825955425c67909099 | CAND-49254efda41b2f8287bd83538ba6e849a3d7b19deb0fa64728a439ceb1d3d723 | [email\_report\_features\.eml](<../data/corpus/email_report_features.eml>) |
| REQ-232 | REQ-741a4838019c01825fab688164a6cc554e84f4c18e4cba3253934eef40d6a5b5 | CAND-c0f0e7b1393c1e80fb5c05e38d8471d30dbdf2556cbbcc7a4b274f0b9a15e608 | [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>) |
| REQ-233 | REQ-743a70079470d57806063469d0a5fa5a023ea9261b34f5d28e19290a7c884b55 | CAND-9cc145c97ab22903f3a2f4b2f57a95679b764ffd05f5c53e07d490cdd7432559 | [evergreen\_reference\_2009\.txt](<../data/corpus/evergreen_reference_2009.txt>) |
| REQ-234 | REQ-750ef8573b46428e52db5fb6cbe7d0fc213003cd99795fbedfafdc66c239d7a3 | CAND-40f9a764146577eb5765bc1f9379141e3d624206d5c92a06583c00efdf6254c5 | [conversations/conv\_pines021\_item\_purging\.eml](<../data/corpus/conversations/conv_pines021_item_purging.eml>) |
| REQ-235 | REQ-75384725abe9bc284f0fa8b864d7ed17139f30169f70b2abb0c7ea380b9a8941 | CAND-085d50782057940ca78d26cc2c6c0e69687947fc2415e3e859bd7654d34df246 | [email\_staff\_login\.eml](<../data/corpus/email_staff_login.eml>) |
| REQ-236 | REQ-75f761336ce9f46285d9f31c43db12cd04397af3260d6f2d9ff7eb10412eea41 | CAND-909bbd607262588d8cc515f8b82288b63b6572aa737fe3472ab0859556f7b9b7, CAND-92351b7749fec0a153571a8cdc3144d5c24cf8e5cdca67ab31b836f2fbf314dc | [meeting\_minutes/meeting\_2009-07-20\_minutes\.txt](<../data/corpus/meeting_minutes/meeting_2009-07-20_minutes.txt>), [meeting\_tech\_subcommittee\_2009-06-30\.txt](<../data/corpus/meeting_tech_subcommittee_2009-06-30.txt>) |
| REQ-237 | REQ-760403193d0d6284117bafb23d34c4cf9a09e3523e703967f7b020940637289d | CAND-d21c470e20ce9f1b73208ae42bc86a04aa6023ce390ee7ce40c1cb4a6d299b2e | [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>) |
| REQ-238 | REQ-764024ba7436bda4e187c159793ac0cf657eda897ab873c97ea1ef4d58bfd219 | CAND-202972b16179a87374aa98fe9b4ef5390df65be8f54196a9a71c2e8543426407 | [conversations/conv\_pines016\_shelf\_space\.eml](<../data/corpus/conversations/conv_pines016_shelf_space.eml>) |
| REQ-239 | REQ-76944e40208876dcc27b57b460d000c3922dd90f49ae198e9e7725fecd2b9368 | CAND-24a24c4117e586597171b350401c9b7be9ae6780852f85be2851daa83a377b5c, CAND-2bac5a70d2574e5b4fc5e0b9a1edf031e25874c56c5a8981ed3e9007f4c62e9c | [meeting\_minutes/meeting\_2009-03-15\_minutes\.txt](<../data/corpus/meeting_minutes/meeting_2009-03-15_minutes.txt>), [meeting\_tech\_subcommittee\_2009-06-30\.txt](<../data/corpus/meeting_tech_subcommittee_2009-06-30.txt>) |
| REQ-240 | REQ-77cdbbcd3678512ff8c2d374f74207fc584d021748c3379ecb41db69c9ca42b4 | CAND-a3ff94c9dd49a977120652f5f0c189848736bb1712930ebddda528a7a9d60945 | [evergreen\_reference\_2009\.txt](<../data/corpus/evergreen_reference_2009.txt>) |
| REQ-241 | REQ-781c58730544f482396b4b16059b63f9ae6bd2d0aaff7c0f49ed753eaec8268b | CAND-f2f2e1111f9493da96f82e3d591b5b6584aff73e8e23d1055883e8e390391fca | [meeting\_tech\_subcommittee\_2009-06-30\.txt](<../data/corpus/meeting_tech_subcommittee_2009-06-30.txt>) |
| REQ-242 | REQ-7873382b18e91570bd8197281a6f001e9df3c93b3140c02c99059080d039bf9b | CAND-b7305b8c16e82236b048dfc26e8b6a08e3e7875fe6b36a3bc3013a4e489bd2b8 | [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>) |
| REQ-243 | REQ-7a0c8973cb8ed518f9abf82bb7bbff333e848201b464a8d1576ab72a81411d5a | CAND-4d491824820ae6a1f29329bbfe0925a24ac55d907b7bba81ca9e0dc18831e9b1 | [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>) |
| REQ-244 | REQ-7af1cc46a49ccf5f4c4b2bd851449c1696f3fee3522d06d42a3ff9338a0f7b0c | CAND-178571d7af05d72fa2f60629463807ef029ded441ef482cb71b5986fa7d6d660 | [evergreen\_reference\_2009\.txt](<../data/corpus/evergreen_reference_2009.txt>) |
| REQ-245 | REQ-7b6c7fa4f29a5a82f0b392224a571cacdf11a6c369e557bbcb9abaa45e292c24 | CAND-d8ce075db4025d4b21ff176b9a8f7441c43582d38b3e3e2ee5ff05173bb3ca8b | [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>) |
| REQ-246 | REQ-7bfaf83f69efe7ebbcf159a165debedbb8b9fc85ca3c45349ea3362e73aa008e | CAND-af05cdfd98fe37bdde26517512297869a3cb74dedf25280eb893150842c08c70 | [meeting\_minutes/meeting\_2009-03-15\_minutes\.txt](<../data/corpus/meeting_minutes/meeting_2009-03-15_minutes.txt>) |
| REQ-247 | REQ-7c16046ba6cf4f3099300c95c29b171590021cf3f9a0981e5e289f4bf02b6713 | CAND-62dd49230766d1ec3c627dc1a8d44d25179910b28708a2a4005c61edb66ec248 | [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>) |
| REQ-248 | REQ-7cbe18a43bc004e93ecf8282a23407c7a5358217e0432522a3741056777c0437 | CAND-1bc7def882a047e862f987f1504b9dd7c9b7bf604ae540469ef1466fd697b540 | [survey\_results\_2009\.txt](<../data/corpus/survey_results_2009.txt>) |
| REQ-249 | REQ-7dab36d987513bce4cb4615bba05f66aace93596a21b6af917732c1341df4ad2 | CAND-8a9fcb99b42bc663f32a410c3e22694d275a797a4b95a0992bce133cf02c4037 | [interview\_cataloging\_2009-05-08\.txt](<../data/corpus/interview_cataloging_2009-05-08.txt>) |
| REQ-250 | REQ-7e074f3c3d835ca452ae3c48e422ec1fb3e3eaf364a70205c06313f97cbcd39a | CAND-9ad3b8929a72aa2ef6c42c3c53ab60d52ff8ee72746b73253f3dd57b2f913a62 | [survey\_results\_2009\.txt](<../data/corpus/survey_results_2009.txt>) |
| REQ-251 | REQ-7ecfec537f372907a56dd312a0a6962119a8217ac76bf50cd1a766fb9d1f2c3a | CAND-36a38745a975aa7cc77dabcfe50d08aa0f564c9e5432afd16d2250a0764ed45b | [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>) |
| REQ-252 | REQ-7efb5012d383718b9284f50d1a00abbc19577086935bfb4354e5df78c359bb13 | CAND-27817c8c3b15ff4dd8628fce4194ec4b5354ca1cd8c9e7e36557d742af715430 | [meeting\_minutes/meeting\_2009-07-20\_minutes\.txt](<../data/corpus/meeting_minutes/meeting_2009-07-20_minutes.txt>) |
| REQ-253 | REQ-7f0e00541153d76c0eb37e842dda667430954bb3ae468044ec341c41933c7b43 | CAND-75be9cb43f93d8b89c6ee0ef6d30a3ecf96678b8052c8f466c4e8e214275d47e | [email\_staff\_login\.eml](<../data/corpus/email_staff_login.eml>) |
| REQ-254 | REQ-7f1a8945403765968d103e08e01a58d54f2b22d479076453a054b57043001735 | CAND-8d346afecd1e6fca9e58195a62e10416ccbfa3d340df66ad694714e318975370 | [interview\_cataloging\_2009-05-08\.txt](<../data/corpus/interview_cataloging_2009-05-08.txt>) |
| REQ-255 | REQ-7fe20f2f414d0b6bb2a5fbb727f85c0e025ab09a5e7a3ab230564b2c404d8920 | CAND-1a3811c0a213ac2be35bea074bea127e75d003925d98fe25bb57878953be4911, CAND-1a96ef3f6e53faff772618b35a3b663759518c0ae10b0de428882cc6783b2208 | [meeting\_tech\_subcommittee\_2009-06-30\.txt](<../data/corpus/meeting_tech_subcommittee_2009-06-30.txt>), [survey\_results\_2009\.txt](<../data/corpus/survey_results_2009.txt>) |
| REQ-256 | REQ-8039ff9491ba06c264a939614123435e1c5c9753c536dac27a6919356224d7a5 | CAND-3b905d1f2f12567b87b0769be444523daf3037cf4c0fa345e22c334644ae9eb3 | [conversations/conv\_pines021\_item\_purging\.eml](<../data/corpus/conversations/conv_pines021_item_purging.eml>) |
| REQ-257 | REQ-815ab976eb1fb48c310acaae0250bd25aa1f280735d89a870ee1860c5446b0eb | CAND-efd8161d2574a6d047d206d43becedf3cf02c9dcbd7391c80358f2d47521d20f | [meeting\_minutes/meeting\_2009-07-20\_minutes\.txt](<../data/corpus/meeting_minutes/meeting_2009-07-20_minutes.txt>) |
| REQ-258 | REQ-81f81b8cbd8488bb7bdc3fabe462101ffb91eebdbd111d794ade10c632b1d34c | CAND-4348024e4fc3569842e0421dd59682230968237168a06dc27d93983925ea3fd9 | [meeting\_minutes/meeting\_2009-03-15\_minutes\.txt](<../data/corpus/meeting_minutes/meeting_2009-03-15_minutes.txt>) |
| REQ-259 | REQ-8239e0a8a6025c47becf4d159f74ea17fd7f9338cd1e27ddee866970d1c85438 | CAND-a6688ed9bf7aeeb6a83cdda3157b6e8e4ba3c7aafca383edaa6c77cbdd7f22e5 | [email\_report\_features\.eml](<../data/corpus/email_report_features.eml>) |
| REQ-260 | REQ-82a9433355bfd9211ad7c71140e59ac886e17446f6338635a08f20eb76f2f334 | CAND-e04a626fb77338ba833377637031307dd80ff7d12f65c7cd20aaac5e8c4382d0 | [email\_staff\_login\.eml](<../data/corpus/email_staff_login.eml>) |
| REQ-261 | REQ-831ab059e0df7aa832e04fbdefd18e1394023cbd41c003b50e79910ba5628237 | CAND-24efd64b595fc9935b6fd3c48aaaf8e87c43ef009d57cbf3503a27abe88b31f8 | [conversations/conv\_pines018\_item\_transfer\.eml](<../data/corpus/conversations/conv_pines018_item_transfer.eml>) |
| REQ-262 | REQ-83305b684e7e93c6ed6b812a002241c272ca271d92b69b56a2b6a444d498db08 | CAND-e6357108ed68dbac76984d51c4c380ca77361e00bb400a736fbd7b0a43b24b1c | [evergreen\_reference\_2009\.txt](<../data/corpus/evergreen_reference_2009.txt>) |
| REQ-263 | REQ-8415aa47b68eeaa3d7c651ef75a378079208c853df5ac7d4005814a7fd898085 | CAND-bb5b03e98522452b8d99e3b3e5f1e0ba2b10dc527aea5c9363ff1e5f95e94552 | [conversations/conv\_pines016\_shelf\_space\.eml](<../data/corpus/conversations/conv_pines016_shelf_space.eml>) |
| REQ-264 | REQ-846c11ac1bf6e94d7a1e70ede1591ee52cb12cf92cb1b5a982e86218f507c7fa | CAND-5206d91138d9a8251b5e9bd1d7bf79e6b2f0bc73a40d422d8a42e2fee106c544 | [meeting\_tech\_subcommittee\_2009-06-30\.txt](<../data/corpus/meeting_tech_subcommittee_2009-06-30.txt>) |
| REQ-265 | REQ-868b0352fbd6dfa0f86d941f7b6b971bb3ec2630959efaf8d42a43bd87e0fe21 | CAND-99e6efc589c27a60d93e8f01243ed44004c4377af40e2dc911fa7279d620d5cd | [meeting\_minutes/meeting\_2009-07-20\_minutes\.txt](<../data/corpus/meeting_minutes/meeting_2009-07-20_minutes.txt>) |
| REQ-266 | REQ-86982ec1ffb99ec98051b741fa992d7e213ffc9e75d21d19bdf3d0de91b35205 | CAND-1769be726f97ae8abb3e561ead88bcf5c0ae22a30cd9b7b7b929a5c81669f536 | [conversations/conv\_pines023\_patron\_characteristics\.eml](<../data/corpus/conversations/conv_pines023_patron_characteristics.eml>) |
| REQ-267 | REQ-86a49ed1b58b112c2faa97c310e907661195ae388f2eb5eaea33dc4a62485df2 | CAND-bd7d935d839397e3c7f2400a4c9f87d8aae202b1ec90370e29a439fc4258eca1 | [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>) |
| REQ-268 | REQ-876194ec737cc7f823e0518315eacdfb0314ec0a91eb5cc53a90b54a781d3e8e | CAND-7d196bae1fe78f8b24ee1f8a999bbbf1b16574b81d8e0faa66ea79b7d1fbc992 | [survey\_results\_2009\.txt](<../data/corpus/survey_results_2009.txt>) |
| REQ-269 | REQ-88615aec00d43be9da5d586cb117eb6dab96e6733f67acb441b5ef63d3ed4bff | CAND-63815786889337e0b615ef60a7b3255f73a310aaf3b4d29436a809e00c670c8a | [email\_report\_features\.eml](<../data/corpus/email_report_features.eml>) |
| REQ-270 | REQ-89b1e0cc81a36fd7830ac5be11d27779694335c4419e02415109db84c48530e2 | CAND-78b6df61fa356e5a45fbf1b8c45d260b4b6369ab64c77a0e46c79b2194b209fd | [conversations/conv\_pines023\_patron\_characteristics\.eml](<../data/corpus/conversations/conv_pines023_patron_characteristics.eml>) |
| REQ-271 | REQ-89b31722a4d93b63b47802265aca41760b53ada131836b24055723a2c441b94d | CAND-b3e81d2e296785ea12efd286cf634e4caea369aaf231c49076077009f228b279 | [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>) |
| REQ-272 | REQ-8ac3195f7cf4e11a3d982c3fcfefa208d25c5108e9f473af03ee9e2feb702a45 | CAND-44c830a5190f065767306d7caa36a95c35236b27f94c80260538f379e4b8f5e7 | [meeting\_tech\_subcommittee\_2009-06-30\.txt](<../data/corpus/meeting_tech_subcommittee_2009-06-30.txt>) |
| REQ-273 | REQ-8b25402a1a0e0da35e86fe4b1d9a88283c13600adcc7dba6a5665cf264bb8ed8 | CAND-3d456d58d8ae127d235f5e8e1f6ee8a0045b74343969bbb1b82172ebe759e9f5 | [evergreen\_reference\_2009\.txt](<../data/corpus/evergreen_reference_2009.txt>) |
| REQ-274 | REQ-8b3162c6b2ee1cfa3434cc55bee249edf64ec3695993dba1227540dd34f1903a | CAND-2c4fd558dbcd126d5fb2f8e3dbe922654aa8924d8eac9255457fdd774f956923 | [conversations/conv\_pines021\_item\_purging\.eml](<../data/corpus/conversations/conv_pines021_item_purging.eml>) |
| REQ-275 | REQ-8b40b51e287eb2319ac729b20fa6b31ae2ebe9ed9c7058db83ec7a5438870b57 | CAND-dbb6c889ee7b708a3288eef0e22e4c3d64ac4fa010fcb363e64202021c258914 | [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>) |
| REQ-276 | REQ-8b4585499327ee31292d05065bd2dc33c6c3f94a3c5a5780257da2f04498126d | CAND-f10479aeb481beded51c02d24ee74a0dfd57e939477120b5ed9121e5228ce516 | [conversations/conv\_pines016\_shelf\_space\.eml](<../data/corpus/conversations/conv_pines016_shelf_space.eml>) |
| REQ-277 | REQ-8b50cc7a2add902799915c02a6da09069c78e2035161fb874f51b0958cca34a6 | CAND-ccda4d5b7132404c27aa255b6e37fcd48185a9dc20b6c6c933d37458c25ed678 | [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>) |
| REQ-278 | REQ-8b6de1fd47daed1f9f96459ff01c5e08dea509ea26a831aa26f0c2d9b30cba32 | CAND-6525261a628a0a11521f32a5790398b9ca97cf97e0d15b97620c3ce2cc6a5c35, CAND-6ff3ce681657abb9346ab5aeeffe36fec45748654c96855c7486bed40ecd5fba | [conversations/conv\_pines024\_inactive\_patrons\.eml](<../data/corpus/conversations/conv_pines024_inactive_patrons.eml>) |
| REQ-279 | REQ-8c5bc8cb0f5e65072154696039e05ee9fd567987e95cee2516a8c5e2a4b3e582 | CAND-a92484bc9ad4bb23e44e084f856d52f357dbbb8bf856fb373fbfb5c7519a4320 | [email\_report\_features\.eml](<../data/corpus/email_report_features.eml>) |
| REQ-280 | REQ-8c6f37fe34933f404144236016e0ae8d0ea9cf21b7ab931304732fb9f3720761 | CAND-c15389e241d81f1cd2aa6c6416a77de3683539064f6965942259a674c99e6a43 | [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>) |
| REQ-281 | REQ-8c9cf6d105b79b0da461665b1032fbe49f6b1298888fc62d473bb746c32fee41 | CAND-2b5558f3fc6e1eb53479f4dec04000a56b2204ca28322c2b925339a8fc2eda8b | [meeting\_minutes/meeting\_2009-07-20\_minutes\.txt](<../data/corpus/meeting_minutes/meeting_2009-07-20_minutes.txt>) |
| REQ-282 | REQ-8d7bbbf2cf6bad036b7a0558c0f18a69c5aa7cdd2275cb289db4e26f8c8760e0 | CAND-338906b17783c1e7a062385f6d2f651f722cb88917910451888cbe6c1da192b6 | [conversations/conv\_pines024\_inactive\_patrons\.eml](<../data/corpus/conversations/conv_pines024_inactive_patrons.eml>) |
| REQ-283 | REQ-8e6224a751d8131f6bb8e55a2b3f3476c8a5a02b106014ef80d80863ee2e8aac | CAND-9db5584ae85dac5b6ed40f6f61553749e5825a2aa0e2845f29c9e2baae13bea2 | [meeting\_minutes/meeting\_2009-07-20\_minutes\.txt](<../data/corpus/meeting_minutes/meeting_2009-07-20_minutes.txt>) |
| REQ-284 | REQ-8e6d56b291cb5b74a95397bc1ffdb3386f0b867820c998d2300b5702688943f7 | CAND-4eeb11030f1b22afa583cb6df81b09fc54e4ed1c3724b9f1b8b123703804eb12 | [survey\_results\_2009\.txt](<../data/corpus/survey_results_2009.txt>) |
| REQ-285 | REQ-8ea032b7c4ecfb681eec7b23aaa46bfd1e15b3094e13fedc3832a7e19ccfccff | CAND-d7941b4db384ba47bd026dad79bad2e252ef0b18d01c5d34dadca424b1fc4c8e | [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>) |
| REQ-286 | REQ-901cf3a8a5cbe9cefb77128edcf0929c6abc5ded0f8393b350b6cacf317b11e6 | CAND-972bd6fb98361cf24737267dddd887376654510d19c82143e32e84d2c82db41c | [survey\_results\_2009\.txt](<../data/corpus/survey_results_2009.txt>) |
| REQ-287 | REQ-9080886072a096004bc8d03bb4aa40635fa547530d19deeefd7a53594fef15dc | CAND-89f23663d56f1a10d52ea2882c947d1caf288f7f2540dd325cf9f905973ffddf | [meeting\_tech\_subcommittee\_2009-06-30\.txt](<../data/corpus/meeting_tech_subcommittee_2009-06-30.txt>) |
| REQ-288 | REQ-9134e1fed77978c60fb2413ae36402b8b14a44f8163f3d7e9e65743731662c19 | CAND-b9e93d46ca2cb5f59659a364cb1f94bcc9f3c11008a3b7eb8cb41a71d1a392ce, CAND-c70e64fe2b184be0202659711f54d06217522bb993a6643757739291f02055b3 | [conversations/conv\_pines021\_item\_purging\.eml](<../data/corpus/conversations/conv_pines021_item_purging.eml>), [evergreen\_reference\_2009\.txt](<../data/corpus/evergreen_reference_2009.txt>) |
| REQ-289 | REQ-91f40e4f994a661fbd58a544bc85c0f7d57b247aee518094ca62f72dc34ecc66 | CAND-d0b9a48e96307475db583e46bb29db395074117652a39ef119f20ef0657091b2 | [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>) |
| REQ-290 | REQ-92690e7229e8e98217908fd4b252b561e24c36d8008f455021f96c3b5461cd3a | CAND-528b742017846017eda4a28de291243864d008e8f6b8105d5553b9c33f7e4985 | [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>) |
| REQ-291 | REQ-92bb4dd94489df26ced5202fc9574a69e5656f3613a6d0f251ac4bbe89352d83 | CAND-710d77d9020152a42ed48b85c8cce791461d677e82674719081815f65625ee92 | [meeting\_minutes/meeting\_2009-03-15\_minutes\.txt](<../data/corpus/meeting_minutes/meeting_2009-03-15_minutes.txt>) |
| REQ-292 | REQ-9315fc23c9498813e0135ab7ec19eccd2821ddf3c9ceb8f1c1a7a9bcfc38ab07 | CAND-6bdfdcb8f5ea58189e87b8a6dca662af7f1a00f8d924aabfb037b1dcd10666d2 | [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>) |
| REQ-293 | REQ-93ff13e5f1b1dd8612c680769837792c2a0f9e80d66939fb6e5636dbf851bacd | CAND-247e727333db03eb1ef134d8765073dd09c3f89803389eb0ca2dca942efeb1e6 | [interview\_cataloging\_2009-05-08\.txt](<../data/corpus/interview_cataloging_2009-05-08.txt>) |
| REQ-294 | REQ-9489f0f1a9476e68442675d818e19ae6035f739d1489e5beb4b8f9443cbe5768 | CAND-39cc7f882373c242a21e240c969f085209db9abb60c99b7ab701467786648ef8 | [email\_financial\_reports\.eml](<../data/corpus/email_financial_reports.eml>) |
| REQ-295 | REQ-9550e74f4358e59fdb834160cd6c82d5af698ef9eeee8e5ba97342819fb0cab6 | CAND-dd32d3617e73dbf9e57c6aa210f3463a3e38222538fcf3a9c1341e18db193e4a | [interview\_cataloging\_2009-05-08\.txt](<../data/corpus/interview_cataloging_2009-05-08.txt>) |
| REQ-296 | REQ-95ba89b96696c858a6c40748d55622b8824772ceeec1abf0c72d1c924ec94932 | CAND-714eff94d1667f6ca43ed80dacbe68f126071db527de4b5cceab3262e6eeb09b | [email\_financial\_reports\.eml](<../data/corpus/email_financial_reports.eml>) |
| REQ-297 | REQ-96002f3d3db7fd77af98c48a3a4bef6e9c43c8548bf96dde6253e733125cec7f | CAND-d42a11233c968c6812c3ce3d870cbfac439a900be355d454e90c091991c1b2a4 | [evergreen\_reference\_2009\.txt](<../data/corpus/evergreen_reference_2009.txt>) |
| REQ-298 | REQ-968ed81502d16790f38794f66aab29f219af762f09c89cf8d77e5a84160e83fe | CAND-189c8a495d293566e6b2d2d067404c64c7b639cbd8dec37d339235eea812113b | [survey\_results\_2009\.txt](<../data/corpus/survey_results_2009.txt>) |
| REQ-299 | REQ-96a0a661a772b9eacf94509db1b9c2107f58d40e42191d3bf63b50343c24e142 | CAND-53428a2ff442116121eb96a63cefc9f0b3de86e51ba12432c486e6a7f63dade7 | [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>) |
| REQ-300 | REQ-96ad5648aad0d60583508a1dc21bdb329cce2ea34f44177f1d4efda7d27f37f7 | CAND-330af25d6aa5626df4d41791bd9a725af9fc4dabcb87980223ba0336d89262d1 | [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>) |
| REQ-301 | REQ-97fa935a0d52bfa813c0a18133690ba835253bfb6236d1efd3d7305ffd26d8d1 | CAND-46458ab91f305f2be1d041a5393d6c08a14ddd03e330576ec232e64dd04d5648 | [conversations/conv\_pines018\_item\_transfer\.eml](<../data/corpus/conversations/conv_pines018_item_transfer.eml>) |
| REQ-302 | REQ-97fda17c62526fbd57a9cd61ccd4eac31076728d1286dbc3693b61b9e881461b | CAND-57b68f1f07814ebe8636037a9fe8037294884431e0b1285289defb48414a9ee1 | [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>) |
| REQ-303 | REQ-983e2944d476bd25ab51211437e775c1f4d53221c0318bdfc06bd833671f2542 | CAND-ffc4099894dab9631579d30b9d3be3f70b16ecf621010888bb568c779a723e51 | [conversations/conv\_pines015\_capacity\_interface\.eml](<../data/corpus/conversations/conv_pines015_capacity_interface.eml>) |
| REQ-304 | REQ-987cc70e7e6b615dd653632904fce88c54622f895dbba9bf474c07c437d814dd | CAND-7dc1f716197a0c43209cf2c7342cf0cbe5d6e4e5e9d799b2d95990797a7dff44 | [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>) |
| REQ-305 | REQ-994cdfd99eeed77986033145b1b7d8b9a9fd8b5fb4415a4390477b0d424563b3 | CAND-64dd892986d23319d8fe445b4f292b9d0a93176635bfbed52cb16196762261c1 | [conversations/conv\_pines015\_capacity\_interface\.eml](<../data/corpus/conversations/conv_pines015_capacity_interface.eml>) |
| REQ-306 | REQ-99ee3fb2cebef41e79d5c214c94a23f682ee6ff752a8a5fc9113220a678c7b83 | CAND-2ea79939686c908ea6ca417f2bcb5a927839f5aad8b5e3a6aeef8864ef55146c | [evergreen\_reference\_2009\.txt](<../data/corpus/evergreen_reference_2009.txt>) |
| REQ-307 | REQ-9a62d854296eab1382d7396fb8748a06178ae56447fc095afe6b7a81cf1f26c4 | CAND-483f228e8b04032feccfa6743d636fe3767982bc3f0bc4a665bd5f7f796ffe52, CAND-49f2468c9084efdcc077175f4ee0bc1032ac9dda61c4f4feb645d64174bbda76 | [evergreen\_reference\_2009\.txt](<../data/corpus/evergreen_reference_2009.txt>), [meeting\_minutes/meeting\_2009-07-20\_minutes\.txt](<../data/corpus/meeting_minutes/meeting_2009-07-20_minutes.txt>) |
| REQ-308 | REQ-9abc4859ea4f78e036e40092e1b053c532d09862cf20c8bac4f31ff817b9ac48 | CAND-3943d017bbe9155bc4d8c9581687c9b6b483b81991e327be1101f977c7cdd366, CAND-3a0b2fd351b8a6606350f8226579eeb12c5cdc5dcb7091f4c78be7761cf21cf4 | [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>), [evergreen\_reference\_2009\.txt](<../data/corpus/evergreen_reference_2009.txt>) |
| REQ-309 | REQ-9af7d80d0eb3bab6a034404290bc83407b77174a4d06dcb2a1591f58e30f591f | CAND-b5b8877697ddd79a308e865825b9671203a11955fe8dfdf7a7abac66e8bbc453 | [email\_financial\_reports\.eml](<../data/corpus/email_financial_reports.eml>) |
| REQ-310 | REQ-9b6a0e7273fde31be149bb6ef5d19ba13ecf50061cbb4b9a7bff50a616c82fa1 | CAND-9aac6402d5da958aeb67c2418c3c056426f513bf6410d31e3332bc6f42df9f47 | [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>) |
| REQ-311 | REQ-9bed4e5fa63e162aad9174dfab25d412e43f8e4b9584b685a54fe73cebc718bd | CAND-c874d30522c1e3c37e24fc1bd1bf92d3a084fbe8f9c1f8ebdd210469d4feca0f | [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>) |
| REQ-312 | REQ-9cae740e23764f4586af93809cd3c99de5668733752bfcc9e95d35865c34bccc | CAND-59b2b5a9dbc557ef0af7c9154f071fc2d4cb34c8aa75aae6e231aa5ca7ef63f9 | [meeting\_minutes/meeting\_2009-07-20\_minutes\.txt](<../data/corpus/meeting_minutes/meeting_2009-07-20_minutes.txt>) |
| REQ-313 | REQ-9df10e7759c5f2c8ec63077923cea5c298616a4e8907431da10b02b38862a26c | CAND-bb9937f47c2f0fa6dbfd70b206f3c74cfc87e41c1024ab58643d228f500fe25d | [survey\_results\_2009\.txt](<../data/corpus/survey_results_2009.txt>) |
| REQ-314 | REQ-9e7f49fdddb3eee3c42f36a7e472c91a4918daf3b5e08c36b24a2486de377fe2 | CAND-424dff222e8481322d23bb9321119b0961b3b486b10dc377a34b7472c7fdd201 | [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>) |
| REQ-315 | REQ-9f3aa7e6a95ffe19b1d3e7f6799a7a93e8ece53b74eef326ef1425bf6b228388 | CAND-5f97ee0a781e0bd8e84f48fdfe563700c395e660218cd6d244e4209c806f7411 | [conversations/conv\_pines022\_deletions\.eml](<../data/corpus/conversations/conv_pines022_deletions.eml>) |
| REQ-316 | REQ-a089b86d6ade163bc3a5fc8250e8bf76d8cace1d40f96544cb31c6d60283b1c7 | CAND-77044be17fd85b79b4783b7e4101855bba06292905b6059bc880c7b9a8f467a3 | [conversations/conv\_pines024\_inactive\_patrons\.eml](<../data/corpus/conversations/conv_pines024_inactive_patrons.eml>) |
| REQ-317 | REQ-a08f6429a3f24e2739cba78f7be907fdadf698ad67e94db216d67ed10c4129e8 | CAND-9753eb313538f11c366970b91f785c1f3dcb05cf80c7c2e7501e2e23685a412b | [conversations/conv\_pines021\_item\_purging\.eml](<../data/corpus/conversations/conv_pines021_item_purging.eml>) |
| REQ-318 | REQ-a0939a4781f15141395b2db72bbfd3ada0f5e5279f36b6fcdc769fabb4cdf11a | CAND-c091b48a8b02e8704a2b7c20041bad484598c24807fc1be08be52e99f4e376cb | [email\_staff\_login\.eml](<../data/corpus/email_staff_login.eml>) |
| REQ-319 | REQ-a2a9aec8b2692fd22012ceacd6189d18558e0b71b08f2754d60f363eab41f67d | CAND-3ee99cd63b9925250a0ac535d498632ffd5437791657f7b1f79ea7109e4f8625 | [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>) |
| REQ-320 | REQ-a3c572278b7e31abc04e9bee9b9ca18cb8323813cf331d635985a15b21b48aab | CAND-abf295f393ae9df51dd44f8201dacfacba1ae2a088885ce2c5e4848dedaf43b1 | [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>) |
| REQ-321 | REQ-a3da459550d75b60d6a16322a829d9a85c7efbfa7548a1f90ebca0dcd66e2962 | CAND-76e30c9d0a1e875e80be4518fd391a3d1aef0c59e71a558008c0a9d5ad4121f8 | [evergreen\_reference\_2009\.txt](<../data/corpus/evergreen_reference_2009.txt>) |
| REQ-322 | REQ-a40d1eaa1adb0459cfec99c490ebd0c3dfa4af30d9e45d4ded325f5f36d5160e | CAND-d5ed7024da0ab982c0a88d261f5b52207d5c1b4de080ce148178e46966991d4d | [conversations/conv\_pines015\_capacity\_interface\.eml](<../data/corpus/conversations/conv_pines015_capacity_interface.eml>) |
| REQ-323 | REQ-a420ca09e1918b6c76cd11134754200494c9ac8d60581632cd72c6b1b166dab1 | CAND-66432579ce33b1655d319e2bb5370fb361673755135f2b0ba8fc575a81747760 | [conversations/conv\_pines018\_item\_transfer\.eml](<../data/corpus/conversations/conv_pines018_item_transfer.eml>) |
| REQ-324 | REQ-a46a4e6b208a43c6201b22de73aeee5cd384639afdce9333481e5673f95e9a34 | CAND-7f42590c9c8fd44883d12c427caada8ce5f09cf9eaa8e3e32f67baf0071efaae | [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>) |
| REQ-325 | REQ-a48922cf4522fc9f2316b57f0815863c27af6b5b89983b902fa10c1aeea7431c | CAND-ad9a5c256eff099f5bb0fdbd5acddcd86b88396e097b400461f3d556c4becbd1 | [survey\_results\_2009\.txt](<../data/corpus/survey_results_2009.txt>) |
| REQ-326 | REQ-a5ea3b71c1fba37231c3b844008a58f35e0bcdaa31cbac7c459d9c7eab0ae620 | CAND-ae275e9acb8701c1a5e815d2eb5d47272661d31ed137b8f603c0b356fad76cdf | [survey\_results\_2009\.txt](<../data/corpus/survey_results_2009.txt>) |
| REQ-327 | REQ-a66ea459d93e9e8eced27d07b449db5f20246b2e91fec4e36b6740dc210113d4 | CAND-a6d80f950131aa716a2cd14dcdd4c514d461de244d3e582280dfeb8bb5106f88 | [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>) |
| REQ-328 | REQ-a6970cad392e9fff0c23ce83719f7ca4ae431f5885cd72a75fa8c3ad4f2a9e7f | CAND-ce4e56e22d58b576bb17bf7430d70a3130b29a76322c122f5d8b99fcd8c69826 | [evergreen\_reference\_2009\.txt](<../data/corpus/evergreen_reference_2009.txt>) |
| REQ-329 | REQ-a69f5fc255e3d252b61bdef16f7663e97ad5528674095cde7175afdb578eee49 | CAND-4ba8842b2402edd9ed4ecc2556dd7e5f6b55243a506cbef63e99b6b8a1217984 | [meeting\_minutes/meeting\_2009-07-20\_minutes\.txt](<../data/corpus/meeting_minutes/meeting_2009-07-20_minutes.txt>) |
| REQ-330 | REQ-a6b71cbb1d302592ff479c6bf037bb43d558a686c0ae16aa4de0d17a7cff542b | CAND-b5f21738c7a985c7da8d784217590291f79bc66d23a5bc94bd32539e86931d8e | [conversations/conv\_pines023\_patron\_characteristics\.eml](<../data/corpus/conversations/conv_pines023_patron_characteristics.eml>) |
| REQ-331 | REQ-a7bfa6f58351cd5eedfb27e9c7ae4dde13b26bcdc7fa7328244a01ef7406a9fa | CAND-2f79953a96cb13e7fbbbbce06eaee523589620b12b6d59e802f99dc5c564a65a | [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>) |
| REQ-332 | REQ-a7d3944ec28bbf71a050e3802a91aeeeee5702e7fea2557b60f39d6a087f26e8 | CAND-602f67ebb6be5e2e20c6ce0b264ca4a6e60301368c5362ac3f75c7603ccdc22e | [conversations/conv\_pines018\_item\_transfer\.eml](<../data/corpus/conversations/conv_pines018_item_transfer.eml>) |
| REQ-333 | REQ-a87e8fe76a954e6206b6914182ccbf509f98dc4c002e5b35d197e9495e54fa12 | CAND-d7e90cfc3e7cf14f18a5b6abd55d535fad5dfe7edea53b916745d20bc82e8b3a | [survey\_results\_2009\.txt](<../data/corpus/survey_results_2009.txt>) |
| REQ-334 | REQ-a8852f951fadacede135ecbf61945a89b15145d04e092194f44aea737705749f | CAND-800d56b22ec0b0bf78deefc4bb3d32ed789abc16f7ba9d2bc35e383760d12c11 | [meeting\_minutes/meeting\_2009-07-20\_minutes\.txt](<../data/corpus/meeting_minutes/meeting_2009-07-20_minutes.txt>) |
| REQ-335 | REQ-a8b07d5110c25ca4fd5f2802911d36e77e2d07c40e090f0636878b0288d42624 | CAND-85b248a3e52b310f531ac1901f26940c4fe781d0562ee089d2e7d02a8fddf7cc | [conversations/conv\_pines021\_item\_purging\.eml](<../data/corpus/conversations/conv_pines021_item_purging.eml>) |
| REQ-336 | REQ-a9c1fe56eb21a58649812d9fa0c4d2e024f35375b70cafecb70daac4b69b3d24 | CAND-be22ff819c69459c7e3a0d374d369bfdb953b4aa23d80952ab42a23810a41573 | [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>) |
| REQ-337 | REQ-a9e0da65c8b5d1610ec1f08f178585b5cc8973875a6a8d88c69a856c79dd424a | CAND-4fb7a4be2983fec72fc8f401274ce684bc93002ee58fb6ab10f0ba74c2e9964c | [evergreen\_reference\_2009\.txt](<../data/corpus/evergreen_reference_2009.txt>) |
| REQ-338 | REQ-abca8b3fc46f890b197fbc849ca15f2fef7b1e43dd54251818127eeee6bf23f5 | CAND-fed7ae4fce588f342fd72ea30bdd289dbe6945e3ef9dbbde7eeef75c735f9a39 | [meeting\_minutes/meeting\_2009-07-20\_minutes\.txt](<../data/corpus/meeting_minutes/meeting_2009-07-20_minutes.txt>) |
| REQ-339 | REQ-ac10eab4f27dc09e759b285bc5d2f42f124eb2333c861406552a9263f795c311 | CAND-9683aedbb525c3a513746d370af45bd0a4f91c5e101e60ec466304e307d462c5 | [conversations/conv\_pines015\_capacity\_interface\.eml](<../data/corpus/conversations/conv_pines015_capacity_interface.eml>) |
| REQ-340 | REQ-ac7888ed04614e37914c1510256f4e83ebe9593cf8e7602d10ef3946dd2c76e3 | CAND-0bcb2f73ef5fe367b5456085c4ddde37ee7fa97c668e116f6cc55185ff281fe0 | [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>) |
| REQ-341 | REQ-ad09182361450643289287a1e11fc87e208ea4307205e1e406997dcab4b8daea | CAND-9fe2d71f0e6f1d6abbaefd186b12757a25042d052b624ad566921b83c366ee2d | [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>) |
| REQ-342 | REQ-ad6c3a1b1223a8a9bd142d0defc24a1a4501af501e069422f6d15f0090fe495d | CAND-796309b89945d06faaf2cfa9eedc1069d771880aeb7443058d2e4ab3f6b41cd9 | [interview\_cataloging\_2009-05-08\.txt](<../data/corpus/interview_cataloging_2009-05-08.txt>) |
| REQ-343 | REQ-ae32d7f02c17e0f882540ab000301ce472b37856a6d7d994b45c6240a804508c | CAND-ee2df40e218ee6ce2f69e5c374f7ddf26465f664207b705c5f4d905f6be5cf2a | [email\_financial\_reports\.eml](<../data/corpus/email_financial_reports.eml>) |
| REQ-344 | REQ-ae64f14e017ccb885104ea8e6761064f76fa2852ebeec1746fb06109a1c3656b | CAND-8c6a5631b7ac10b221ae1c014e3e5b176b1e8f687e5c75a7f4415f8295b6d204 | [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>) |
| REQ-345 | REQ-af341348a59519bb122bb99bc94d6fbbcc095dadc7a43036d46e250ba3ce63fd | CAND-8bde7e66d6d9fc1eea4a4ae3ddd889eb37975d961dfee15212833c7591e1545c | [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>) |
| REQ-346 | REQ-af4d86fd077e78af1b0bc2f09218ac63b117de3bb73a9ccf71951d3e9010aeee | CAND-7f792351645a4e8833f72681e892d38ef94208a7489f22c574c17425d73823f2 | [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>) |
| REQ-347 | REQ-afca43f28caaee09141a99a7c4b58160ebcd6f48552525a2809060f6ada50b40 | CAND-11d9417c85f393fb70bf73137ff3d2cfc673b87e0ccc22df2071c639f9016d9d | [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>) |
| REQ-348 | REQ-afd32b7d2ad8dd28a557b8cfb8b5ead5b57aa3ce024078afa320effe9f3e32a6 | CAND-114e2eeface91605a4b66c8814c1fef72a24a8a2ffbb97aece7e5bfdc6fc8012 | [survey\_results\_2009\.txt](<../data/corpus/survey_results_2009.txt>) |
| REQ-349 | REQ-afeecc228381066d15e3eb43f6868b883ad2c4bf2d5b7ca99d916193dd808bf2 | CAND-f9d16451de6c45d7e5f0db5ddb40baad236ed434e076bb0e4806555b7cc159de | [survey\_results\_2009\.txt](<../data/corpus/survey_results_2009.txt>) |
| REQ-350 | REQ-b00a32939a08725b82df7d62298a3af285e2d4ea29d9142f04fbaf2fdd9aa427 | CAND-c07b36a66760097dd28fdfdeddbc8d945e9eaa117a0e6c2341359f690d9a1787 | [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>) |
| REQ-351 | REQ-b0a5e6dfed37fa79b7bc78414f1a54585b709c114477c95df571819ce96fa2ae | CAND-f70f44e72dc93569af2c299e88a59a23a3dac1696fe0d722bd005dbc70436d08 | [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>) |
| REQ-352 | REQ-b0ae4fb264b052e1ae7956d4bea1854eee4fccd2a49b08a56e3a736340e19fbd | CAND-79ce1c2996009aed76fd9815eafed8df91d85a511073cf47bd0a5ff4e77d036e | [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>) |
| REQ-353 | REQ-b0d60abaae7398ad32b123e1a9b2889e84ec2c8332fe4bcb56c0cfc75258f3c4 | CAND-3f8acaf3f9e550a313971437559d2b40c11e6d8ce41ba7b35db5952c5f0010d8 | [survey\_results\_2009\.txt](<../data/corpus/survey_results_2009.txt>) |
| REQ-354 | REQ-b10023f80640b3b5643b1f8efcd43db35d40e40c225c8410ae6b2c5b24fe4382 | CAND-5d69492cb020d5badc1d0492b8300a1c6ec7178260576abd148b787a9d8768cd | [evergreen\_reference\_2009\.txt](<../data/corpus/evergreen_reference_2009.txt>) |
| REQ-355 | REQ-b17846e8aa9640e29bff60834df4af0793761e57020867832a8628402509f783 | CAND-b2df79f1f799c3170d02a5434f7185ce7ec6cd9638a6fb80f5fc763d5c1e546a | [evergreen\_reference\_2009\.txt](<../data/corpus/evergreen_reference_2009.txt>) |
| REQ-356 | REQ-b1acc564dd39d20ad26851a72484f666fa67ef00cf52463df15499c3febfa292 | CAND-6749805eefe2dec31d7436c9b391995ed74634fef104179e3958d7067ee2de82 | [evergreen\_reference\_2009\.txt](<../data/corpus/evergreen_reference_2009.txt>) |
| REQ-357 | REQ-b2995f84e38e2b92fa0d37c901b064f30fc9439c1d83c32b8b24e6473cedc3f5 | CAND-8d99926ff7571a9550c86da97a707194c02656248b258fdf13e070f6ebc9eec9 | [survey\_results\_2009\.txt](<../data/corpus/survey_results_2009.txt>) |
| REQ-358 | REQ-b39df83f47073c709add8d25e258fbd7db3ba1aff3466bee050d6cdde498c567 | CAND-dd84aec4ea69298917dae1455e70a8b51cd46976d6b0e09c2dd758593c4e3a70 | [email\_report\_features\.eml](<../data/corpus/email_report_features.eml>) |
| REQ-359 | REQ-b3aac13b23d77b7e6051d02c63e4db409611bf798ac601692873f240a109ea8b | CAND-18f92cc633ca4280eb067974d6777d4723e2a816dfb0490d86777eb6ffd95117 | [conversations/conv\_pines018\_item\_transfer\.eml](<../data/corpus/conversations/conv_pines018_item_transfer.eml>) |
| REQ-360 | REQ-b4e87e83411a5dea31f12805a443db52e7d3873ffcce3ed2e1150339494894e8 | CAND-afca3180097b44cb79dacede455476a8c7f1712fd97b52e88e8d53adc32c8688 | [evergreen\_reference\_2009\.txt](<../data/corpus/evergreen_reference_2009.txt>) |
| REQ-361 | REQ-b541c5e21367401e0e5fb76dbb63fba32fc4a6caf9bccd85614c1c5d6e09d2d9 | CAND-c174918e4ea8ea57394de28cc3d453279847ee6815eb8e7e504b9230531d8401 | [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>) |
| REQ-362 | REQ-b5532db78ede5824c50d8f6b701cb4109b322b216253e30bf898a61dee208fdf | CAND-5267255ded67334c52e7cc4b18133bc68e9e1c1d75f67f89829b2afad7c58837 | [survey\_results\_2009\.txt](<../data/corpus/survey_results_2009.txt>) |
| REQ-363 | REQ-b5db3ca2db4d921edb169ca79ae7bc2e7a92ec90e866f8a9e7b1243248fcab92 | CAND-5c943301a02ad13f1854f93a28854a5138041110a9928032cf282b0b54fdc936 | [conversations/conv\_pines021\_item\_purging\.eml](<../data/corpus/conversations/conv_pines021_item_purging.eml>) |
| REQ-364 | REQ-b63c4b011377afd50fa29a840314ecaa823a0e27b680067772f00c93b2b638e6 | CAND-abb42577e6289b4e5fb64f696130dd64f78bc24546be96ede7e46378586c3efe | [survey\_results\_2009\.txt](<../data/corpus/survey_results_2009.txt>) |
| REQ-365 | REQ-b65a935072e139b3418526b987074f2c02d0b7eefcf18b23a40268705df980cd | CAND-20788446eb843450003516c57df8e1e72c9b4d3c086c0e70a31c8fa9338dbd7d | [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>) |
| REQ-366 | REQ-b6e16a43d1fdb11716fe9a42d6c7625c2be712ce84e03b17597fd1a0a482ff02 | CAND-e77c7d63f80e4776ab2e964dbe538170728976e1c3589709731d887cfd4187a5 | [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>) |
| REQ-367 | REQ-b74d4e8fd2c04d794ceea2095028af424d32a85eeea9c89921bd51eef238d3b9 | CAND-2d1cb052d090dce2083f4efedd5b94f5307b4b12e2a1b628c56eec9bb1995e2e | [meeting\_tech\_subcommittee\_2009-06-30\.txt](<../data/corpus/meeting_tech_subcommittee_2009-06-30.txt>) |
| REQ-368 | REQ-b79c7e93b49bba321aa4077b9e5777464fb6254bbbe8f721141be67505d2000f | CAND-fccbce87e5e68cf0cf6f04365aa8a3e08d727590d17bbfd55970230d0012d139 | [evergreen\_reference\_2009\.txt](<../data/corpus/evergreen_reference_2009.txt>) |
| REQ-369 | REQ-b7dfe7f29d3af0ea09356a370c0cad4196982b536fb02d92a483a41566444541 | CAND-ad9b24e74895dd5629a573b99dc88b041d51bbaaae8cea1c72c609234f9c081b | [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>) |
| REQ-370 | REQ-b83f243dd4caff5a2982cfd1fff3f9ac1854a2719d08f527ea803a1ac06b64c6 | CAND-d1b29571923af634aaf2b2333f5b92cc163bb629d8be8f769012bccb12904b4d | [evergreen\_reference\_2009\.txt](<../data/corpus/evergreen_reference_2009.txt>) |
| REQ-371 | REQ-b86723d8da0e0daf49c3760e357f7eb818738e2bd2e9b8702d6839588b91deaa | CAND-3ea7c0ada82784adeedcad6f8209cf12e494bfe279bae7c435be6e9ee06387f2 | [conversations/conv\_pines015\_capacity\_interface\.eml](<../data/corpus/conversations/conv_pines015_capacity_interface.eml>) |
| REQ-372 | REQ-b9fcd55343f17bd51b0347c0e321f4ac23425e66cac9310541b1573bc9104c6f | CAND-8ed52d5f9bd9975008a4eb1a682b4f01ec1ad6dde125117d065556b26e1721f5 | [survey\_results\_2009\.txt](<../data/corpus/survey_results_2009.txt>) |
| REQ-373 | REQ-ba53da7b466cfb8817b3052a5c7ab8476e04df2e307523024641b9bc0074b549 | CAND-8ad6b8ce568e7c3aef1e4e9b2d01665f72b703d8483f4830d47a276c5f86757c | [evergreen\_reference\_2009\.txt](<../data/corpus/evergreen_reference_2009.txt>) |
| REQ-374 | REQ-bbf5ddc24bfa77581600764a41060bf5809b743c27ba85945e10a17586a176ec | CAND-5a602fc5e67480500dab31a57deeec413d7d00e4b2a59ffc6eb784226d774e33, CAND-5c4ec9e6d30a58ce848d6a54a209c90a5b78d9aa948fc50ad8cbb2615706646b | [conversations/conv\_pines018\_item\_transfer\.eml](<../data/corpus/conversations/conv_pines018_item_transfer.eml>), [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>) |
| REQ-375 | REQ-bc6eb82bede0efa6ce10b1f3b98c1f6ab44253e02b292a31212ee57130c1929c | CAND-e19910163f256a30185b9d3ec9b1d0c289defb7335370fb91d451aead4841035 | [interview\_cataloging\_2009-05-08\.txt](<../data/corpus/interview_cataloging_2009-05-08.txt>) |
| REQ-376 | REQ-bc8036ee36d5b4f86da1391523d862267ef6cad4a254882af196ed994a1b5cec | CAND-664a736c7fe1a44b5420ab0b2df667aa06e176510f09e1f8a881401ee417a1b6 | [conversations/conv\_pines018\_item\_transfer\.eml](<../data/corpus/conversations/conv_pines018_item_transfer.eml>) |
| REQ-377 | REQ-bd08cc5baa7105633ffeaa962f1b9519114f33e4a96cd0f15e1b3de0fa9e55a1 | CAND-961f2c34759c754b880424202ee391f1dcf0aaeaf2650d8681ae2d5b119c0640 | [conversations/conv\_pines019\_020\_missing\_intransit\.eml](<../data/corpus/conversations/conv_pines019_020_missing_intransit.eml>) |
| REQ-378 | REQ-bd3ec11e234a90583bd4292ad74181033b162aa711b58109abb045c077e96162 | CAND-efbc4ad832f42f8da24820e05b075f750304c8a33329ba5eb79c38e4621074c5 | [email\_report\_features\.eml](<../data/corpus/email_report_features.eml>) |
| REQ-379 | REQ-be47529142a5ada1c4c3aa738a9b845d051ab53636bc881ca67513364346b5ed | CAND-d09c0175bfd6b7c30ed57e4e077a067f3a7ff37472ff68095df4c9be372d319c | [meeting\_minutes/meeting\_2009-03-15\_minutes\.txt](<../data/corpus/meeting_minutes/meeting_2009-03-15_minutes.txt>) |
| REQ-380 | REQ-be94c3919ab5d0714c081af3874bcc70f9daad8d1c7bf97a199089263a35167d | CAND-46753964acc52b2ba175eee48ab89e67d52b4722a1be8a81019bd22c679332c0 | [conversations/conv\_pines022\_deletions\.eml](<../data/corpus/conversations/conv_pines022_deletions.eml>) |
| REQ-381 | REQ-bf3e61bd179254985f4f8aa789bc1e3302d88e90e92651744dfe30610f9958d9 | CAND-8ca2ed80dc991870ad8dffcd80c78d7f427b1c7dccec8d11a24f9fd0a4b728b6 | [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>) |
| REQ-382 | REQ-bf8512a398e32dcf007140a734b7981d514c6b573e5b3f3ce270486bf72b37bb | CAND-9845760de35b6b3a202f175e5dc71d7409d2b90091411d89d378faf86b87a77e | [meeting\_minutes/meeting\_2009-07-20\_minutes\.txt](<../data/corpus/meeting_minutes/meeting_2009-07-20_minutes.txt>) |
| REQ-383 | REQ-c01fe7ab443cd0227e385540dd185804ba4172c292d7b8cd4e350553177e9f00 | CAND-9e77d31e02b4993148b6e1d25dff30b0391b51fb0b71eea07d10202cfc5f0373 | [conversations/conv\_pines015\_capacity\_interface\.eml](<../data/corpus/conversations/conv_pines015_capacity_interface.eml>) |
| REQ-384 | REQ-c0640d8210c3aea90a16e5105f2ae15748c2f98282dd9046a90d055bc2aecc54 | CAND-7bc8a57a40eb7785860f45bb4214b0f836f0903b3fe2218c3c830f44c1bb5e58 | [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>) |
| REQ-385 | REQ-c21071092848505eebbd6bdeda465cfb14fbfa18f362247f23ce5c1524f1881f | CAND-4bdbb953689aac51560b9bb50f0906670fed75f9a4b2f8914f9d313bb9beaaee | [conversations/conv\_pines022\_deletions\.eml](<../data/corpus/conversations/conv_pines022_deletions.eml>) |
| REQ-386 | REQ-c2bebfaa1cf67be2e28a51f27b91850c6b592f5c2ef371a7258aef65f2f1aab1 | CAND-9ecf0c4a0018aa776bf6901ae5f0cd91e8e71013f3189aa1805f10f6e90b0f1f | [survey\_results\_2009\.txt](<../data/corpus/survey_results_2009.txt>) |
| REQ-387 | REQ-c3db002a14dfedfd3da9401aacc815e33685211e2d6acbce3fd703f9fbd25a9a | CAND-f8c692d46fb6948abfef92f2690ea13ea96f65e1cd01c72a16fb9a4b393120ed | [meeting\_minutes/meeting\_2009-03-15\_minutes\.txt](<../data/corpus/meeting_minutes/meeting_2009-03-15_minutes.txt>) |
| REQ-388 | REQ-c42c8dcbcbcb4357a68a3eb72c553896f2bff1d4b4b7848cbc49ebc5efd58dcc | CAND-72171ec470b8383e0311d21373bcadb03c55794bd97bb4b9806af66675ccbe77 | [evergreen\_reference\_2009\.txt](<../data/corpus/evergreen_reference_2009.txt>) |
| REQ-389 | REQ-c4d72b9a148ccfffb525d21b1217f5b8e5d8d74c42bc74b985ef81413cc57116 | CAND-a86a2363b8b0dcdcb802561d3634ba57ccf22e0dfa65a87446dabfebc976b97f | [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>) |
| REQ-390 | REQ-c556932e61ebe1eb1f18ecab1adda4a88e5b6ba8783dad44f339001c821a2d3c | CAND-15e2e0a1aa9d84721ff93cb0e7cce7699ec1cfd8591c5efd818517d0f7f80146 | [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>) |
| REQ-391 | REQ-c63ab9695a805fffc87a7e5c4c76fed55cc9b72be34838cabd083f12285fbb89 | CAND-dd61040f25203f497c75947db22c18a802e7943d9a5723aa8988aecb04fef16d | [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>) |
| REQ-392 | REQ-c64b467dbd6b73129990452767485644aa7c902352ac4e7c99ea42d2de4d967d | CAND-a8d5d50225b80bfd4b548945a13318e04bc07ea1d356cff22e9a3a1ca0f26c6c | [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>) |
| REQ-393 | REQ-c6630d70e8b3ce1a7155818aaff2e9a28ff3284a8c61290ada11e063ee3b1093 | CAND-cfa0ef0f5d7099abf8bda7d1b7d45db93eaef8b483314b9c1c194d9d24f8f7b0 | [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>) |
| REQ-394 | REQ-c97ef62d268adf8c393bbbd0fe1eceef277aa3447fcaf0652c22b2a5253140ef | CAND-66c37bfd6aafebf9eb2f2d535c0f045fa410d484fc9eb80e190b03ee8b6feca1 | [interview\_cataloging\_2009-05-08\.txt](<../data/corpus/interview_cataloging_2009-05-08.txt>) |
| REQ-395 | REQ-c9d0f819d4ed7c5f9decf4e72e1929fa63a3305550ac5a7a8ab7af2eb8999e3e | CAND-130d2d443ad1cbcd94f138c9ba35450163220236f546b7ee0e40708b58cd893e | [email\_report\_features\.eml](<../data/corpus/email_report_features.eml>) |
| REQ-396 | REQ-ca268ed9556dcf203eacc910492da68481df2879d0b235013be232affc25c437 | CAND-0530577eccda48dc14e04a5c2edef3b73ee284be9d5f3435720ee7f6bde583c3 | [survey\_results\_2009\.txt](<../data/corpus/survey_results_2009.txt>) |
| REQ-397 | REQ-cafc0446d75c014b8e37727e28ebeaacabbefef252b93df2f9c79a32ccce3414 | CAND-484458b773afde4efa6f89874866fa9be9ebfcca62bf9fc60a0fe68f8a20d142 | [evergreen\_reference\_2009\.txt](<../data/corpus/evergreen_reference_2009.txt>) |
| REQ-398 | REQ-cb082c2aeeccd4d279e1435a58b3adbcc98a7a71af12a38d83c687c98ef32dc5 | CAND-83b500323341e44e76d6e129dbca0f794420db375942babc4d8fca470ecd27c1 | [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>) |
| REQ-399 | REQ-cc850a0e8bb1a2805fcb12628f43ffdfbd5e1c95e4ffe6020c321e1dd012c3a1 | CAND-d3f6712c08e7d44922f0fe04ed990f57212c3c8f77e30fa30b96554da045dc53 | [conversations/conv\_pines019\_020\_missing\_intransit\.eml](<../data/corpus/conversations/conv_pines019_020_missing_intransit.eml>) |
| REQ-400 | REQ-ccb00f03f4fa4c2a14f847a285293594b7530a66dfe327b56f1c20bff98a1e38 | CAND-74b20e98c3ed05986504b5bef67276866e937041a8ab9283f5756c12b0b8bbde | [survey\_results\_2009\.txt](<../data/corpus/survey_results_2009.txt>) |
| REQ-401 | REQ-ccfe3165ec823a23895831671c993789ea0b0653d751c602fb5717b131d9f1b2 | CAND-18081af877f991a802132babbe7136612d56084c49dd17470790bfefaa6495ac | [evergreen\_reference\_2009\.txt](<../data/corpus/evergreen_reference_2009.txt>) |
| REQ-402 | REQ-cd28ed99f62a1eaa2f8cb4f361dd5d9b9eee3e861a9470cfb53e60e5cac20237 | CAND-0a11d6a6c6777690202274564edb434ab646222968ded51a3c42143500f5a7bd | [conversations/conv\_pines018\_item\_transfer\.eml](<../data/corpus/conversations/conv_pines018_item_transfer.eml>) |
| REQ-403 | REQ-cdd500fe7e1bcb73b2c251da24a83a7ca3c1601a2f86194692bbb259840b70d4 | CAND-feac7279a16874f96776f98fd95775d52879b3e9b8a203c0736e4895936b3960 | [conversations/conv\_pines015\_capacity\_interface\.eml](<../data/corpus/conversations/conv_pines015_capacity_interface.eml>) |
| REQ-404 | REQ-cdf419cb18f8111c0ab93700605c3b9bb9608628eb71c153f8fdd435e8650f3e | CAND-25b0fe1c717bb18f40e06944be576f442ab4260b37b32f33ce93f6a7d1faf437 | [email\_report\_features\.eml](<../data/corpus/email_report_features.eml>) |
| REQ-405 | REQ-d12923023339df94bed4aa799fb0a18a5ab900c1d89b7ecce30f6658a6a19a67 | CAND-2d12b9a22022ba2d37420c93054e36acb67ab428385feacce108e28c2e959038 | [survey\_results\_2009\.txt](<../data/corpus/survey_results_2009.txt>) |
| REQ-406 | REQ-d1604f4690e341661d46c22b2d89e58f20ae8082ce4ffc6f86d218d15626612f | CAND-7c685f0cc4bc21f8ac76d7ffb7361d3556e6e3605c829629088695dccd06a53d | [conversations/conv\_pines023\_patron\_characteristics\.eml](<../data/corpus/conversations/conv_pines023_patron_characteristics.eml>) |
| REQ-407 | REQ-d18c52b5fbda674dc0f503fffd358372243cf96b23b55f8da9ecfb023dfb2511 | CAND-8859d15565740cee359ee3d053a7581b23fdc5055e744b63ce68a133616ef023 | [interview\_sysadmin\_2009-05-10\.txt](<../data/corpus/interview_sysadmin_2009-05-10.txt>) |
| REQ-408 | REQ-d1b647653268590579a6efe10ccbaf189feb43c07ca1786bc50905db6a9c6ee3 | CAND-ac29e918f53aeec17db31951a5de7cab32991a9346e84c938a2939e2769b04d5 | [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>) |
| REQ-409 | REQ-d23411927c5705fb0c113d7e4397dcaa6491d9f0d8e1656e92f1b42cf4039b65 | CAND-d4d736e3d0384a555e15ac95c1d4b632a75a9ce51740052a84143f158deb18e8 | [survey\_results\_2009\.txt](<../data/corpus/survey_results_2009.txt>) |
| REQ-410 | REQ-d2696c041209b3af3e5a7f8e5f87651bb1960b00d180d868dc6b1bb1ceec382f | CAND-c581fd4f45eaf4540fbd52ec18e1e3ff13679b0bca0cdc2b1540a47883fb69a1 | [interview\_cataloging\_2009-05-08\.txt](<../data/corpus/interview_cataloging_2009-05-08.txt>) |
| REQ-411 | REQ-d28f68b20f43ad6d365884634938ad247dce3e9ef6ea3461934efef991fe0c60 | CAND-47e24ba0fc59bca7f7679ce23baab7b1340d0c2b7fdb1238cc6eeec843bb8162 | [interview\_sysadmin\_2009-05-10\.txt](<../data/corpus/interview_sysadmin_2009-05-10.txt>) |
| REQ-412 | REQ-d29d0f486142c33bb4c83b82d8a6c815a213413432aeb25c117b21d902ddc423 | CAND-51c2839ac1c5c390bd5211c03c7947213fad8a6e18343168a3dd991e4afdcf9e | [evergreen\_reference\_2009\.txt](<../data/corpus/evergreen_reference_2009.txt>) |
| REQ-413 | REQ-d3b1aec41f48d0399de3eeb823e8fbfb84723fa669e2826cd1f4b61a2ac35e6d | CAND-8605bb41f899a282e44b60c17009adb4f4c9196d0c3fb71fd417ded3491590c7 | [meeting\_tech\_subcommittee\_2009-06-30\.txt](<../data/corpus/meeting_tech_subcommittee_2009-06-30.txt>) |
| REQ-414 | REQ-d3e96b7a6e5b39fbffd47beebd2633fda0d21b94226a25556b0fcfb870f63fbb | CAND-6b207c4fc26b18a238340c717d7bc5f081933d4c29c03cb9865138c3d279dac0 | [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>) |
| REQ-415 | REQ-d43b435d85005b904ebee7be3f3cd9894dfd5641df5d4206ec0c4fe11de0edfd | CAND-0eac9bd1b3990e377378abff6a437d8c1a802b4fc006b424f9eab55526732ef5 | [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>) |
| REQ-416 | REQ-d473b44f695f3eae8cf58829ac3f81ab5dd1eef738c287cc8ec984815efed028 | CAND-aa11c7137274f313cd691dfdebf80c43e28280fe321cd6c81fe47291bbd7183e | [conversations/conv\_pines022\_deletions\.eml](<../data/corpus/conversations/conv_pines022_deletions.eml>) |
| REQ-417 | REQ-d4d3a796d19421135bcf413b6e3a5b677cc98471ad9d1c6a350e17d7e67d7527 | CAND-3667b7f07ca36c5ad267494f8549580978de8578176517783797a1a6548e69e1 | [evergreen\_reference\_2009\.txt](<../data/corpus/evergreen_reference_2009.txt>) |
| REQ-418 | REQ-d51ad6fcb102275e5fa971142968e1fa6051a21b5e00031c4ad0e3c2e2dfa509 | CAND-df016350837281f634cb397b3d1d31c88211e938f4701339cd9b54cb40188ff4 | [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>) |
| REQ-419 | REQ-d57d5296e629b8980c231ff304e333628dee47017c28850693b93312c33f5425 | CAND-46cf96a343e04929d1ccef7c3f9f84fdcf02294a5e8de9723d936fa074eebbb9, CAND-486756b6cedb8d4ab9e4e0b56f5b19654991e40e0c1f557a5efcf2343a71c26f | [evergreen\_reference\_2009\.txt](<../data/corpus/evergreen_reference_2009.txt>), [survey\_results\_2009\.txt](<../data/corpus/survey_results_2009.txt>) |
| REQ-420 | REQ-d5fd2cdf349e1983bec192b4eb768ae65ed45d13911604cb596f3f640c5dee59 | CAND-9509453ac6e0b28ed5f03b75e51425c97fa270d882bc854211d4da781c6edb98 | [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>) |
| REQ-421 | REQ-d6788da5598c6cea601bd5ee6c8f91d48bf76514b190467aacd1e73ae90d4332 | CAND-cc52dd7278fcf306a9bc29a24ad8bdcb140c19832924ba3b73843e3d2dd01032 | [evergreen\_reference\_2009\.txt](<../data/corpus/evergreen_reference_2009.txt>) |
| REQ-422 | REQ-d859a0ba10e78959c7c0d7ba2b4e9332f78e5f6ebfd0bbd0d45d7f07fbeda938 | CAND-0003949c2d2ce1f2fe45c76e382d2c4c6ff6a3e881aa87224837a4b327aa5731 | [evergreen\_reference\_2009\.txt](<../data/corpus/evergreen_reference_2009.txt>) |
| REQ-423 | REQ-d90e07518a4dcac124e6c0529ede02d1bf245da9661ccf721941c46ebd7167a2 | CAND-505b347f91609a09079a50d102633715a472959275690e9c907e4daa96ad8715 | [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>) |
| REQ-424 | REQ-da5b82ffef316e3d9074e055fe0dd4ecb19fdce1ca08e6f1bbd17a83299b5f32 | CAND-9d3462625b7e63c50d1e35d15d0af6a7edb5a70aed396ea4fc1542cfa71577e5 | [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>) |
| REQ-425 | REQ-da7a4b4bedd8da13c1273bcc6a5832c2493ea4777aab55605d574a6ef269e7ce | CAND-aa5410337ef1b7439bd5a1058ff24d95d7f9d1ba845d79c210f8ef716e145849 | [evergreen\_reference\_2009\.txt](<../data/corpus/evergreen_reference_2009.txt>) |
| REQ-426 | REQ-daba49d0be7838dfae3529944f71dad32c939b30e275edd1c65205f02817b8a8 | CAND-1f9af3d8cfafc1a79b14ad82a43a7ccc259d8e4992ec3489c83d57eebf387189 | [meeting\_minutes/meeting\_2009-03-15\_minutes\.txt](<../data/corpus/meeting_minutes/meeting_2009-03-15_minutes.txt>) |
| REQ-427 | REQ-db35fce9a845b58a4873b121735c4bf5cc443172401968ac0f0633d03e1c939c | CAND-ba4fcc948dccffc971be6171e69d11c7b35420c4c1ca0f38f2ad8ad9e5ca2785 | [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>) |
| REQ-428 | REQ-db975f9e2b8eb2bd106cef17674bd91e6e005e90b976e2fc5a3dc096779f382e | CAND-eaf45ec50a8f86836a0cdb9abac7f25c886e5ab364647207f4b9b799a1dc241e | [meeting\_minutes/meeting\_2009-07-20\_minutes\.txt](<../data/corpus/meeting_minutes/meeting_2009-07-20_minutes.txt>) |
| REQ-429 | REQ-dba1573e94e93bcbb636662d0569f4c75f556b400afa80de184a788372ea820f | CAND-df28e114db86cde167ee8c617846543d59cabe26d69a6d069eeddd0e48a94edf | [conversations/conv\_pines023\_patron\_characteristics\.eml](<../data/corpus/conversations/conv_pines023_patron_characteristics.eml>) |
| REQ-430 | REQ-dbdeecc38b3a0d1140bd17181b88eef0f06a8dad6885d377c9f48bda0c9db257 | CAND-ca960eb5a90f3ea2b379e68a5e90ab77b9cd3005bae369b733d274273059a07b | [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>) |
| REQ-431 | REQ-dbf327c03cf29ea9551b738993c8c3775c4ad1a460e18229fe09a6665a03e2b8 | CAND-67cdd29e03ee6b04f5050e938bbda03b78a72eef7f2d1690350bd532965105b4 | [email\_financial\_reports\.eml](<../data/corpus/email_financial_reports.eml>) |
| REQ-432 | REQ-dc8673fa44b4a60ae680f42eafc76986598f270c996ead53aa067a78ac633007 | CAND-c6ca6db558320760100809a27201bb3d8908951adc676e457071b0040593270a | [evergreen\_reference\_2009\.txt](<../data/corpus/evergreen_reference_2009.txt>) |
| REQ-433 | REQ-dc8bf974feab6a41ea64c95956f6a2157bc7d7f1e622c25709b16017a6cad4ab | CAND-a87f0fb4d2226b1365e3b636f939e3d5f75901e610c1fffc763098c1313384f3 | [evergreen\_reference\_2009\.txt](<../data/corpus/evergreen_reference_2009.txt>) |
| REQ-434 | REQ-dd339030fc9431951c3c9bd8643de814c2e61efed7cb83d39832cf4e10f99963 | CAND-21a5d65bfd2cc8d54ddfc0b454248cec0f82e2c7aabb3d118c6a9ebf4ab706ba | [survey\_results\_2009\.txt](<../data/corpus/survey_results_2009.txt>) |
| REQ-435 | REQ-dd39afb13a3d552adde49376cfce9baa9b23299e94197f6472a8f4173d9456d3 | CAND-f4d7b321c9a56869fcbfd4418432072925db090b2fbe0581675fbdcbc4d178c0 | [evergreen\_reference\_2009\.txt](<../data/corpus/evergreen_reference_2009.txt>) |
| REQ-436 | REQ-dd5e4aab34ad1f30eed68d71ed9f66c1e1be398ab1a18fb6b92da7d460366846 | CAND-256c8209b11df7aa149ad954bcd18bbe20f6e344ffdf1e8aef8aac79c5dcabb8 | [evergreen\_reference\_2009\.txt](<../data/corpus/evergreen_reference_2009.txt>) |
| REQ-437 | REQ-de70dda33ee3be7e7ed90b39ce8fa8fc27f384bca6ab288f52fbe9dfe0d6597e | CAND-6f5236be44966ed2c699a62259d4144e6748ff7fb65d465edc6536420ef3f150 | [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>) |
| REQ-438 | REQ-df7d84a99e4c5d334f09662aab74f7aeb94c7223846fea2de072f152a669cdf6 | CAND-c7203c53d0d60c5c36e711452a21601b682bc60a8c33212a30d68c672ef62f66 | [email\_staff\_login\.eml](<../data/corpus/email_staff_login.eml>) |
| REQ-439 | REQ-e17884bd89d6e507fbba4f4e181ef3f1111c5d82b19faa3163a9c87629ad9e36 | CAND-6dae8ec2820d2d9e062e45b2d94cdb80d15819b65bd1a645a015e1f5b2b53028 | [meeting\_tech\_subcommittee\_2009-06-30\.txt](<../data/corpus/meeting_tech_subcommittee_2009-06-30.txt>) |
| REQ-440 | REQ-e1999db196c744b6763264bcf9683eab9f1904e559fd3f2ede45f99fcb56647d | CAND-628659d7e54565c7142b34c645ad3aacdf376128c95a35f36a963e93a00eff11 | [conversations/conv\_pines018\_item\_transfer\.eml](<../data/corpus/conversations/conv_pines018_item_transfer.eml>) |
| REQ-441 | REQ-e1d92790466974fc198f225f7c73bbf0455ee79e499911a16bb9838689050657 | CAND-7f44ee73048fd67a14b16385384c01c18fd590c7eadf8a36b1a8eab65074103f | [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>) |
| REQ-442 | REQ-e1f083ff6431150ab09c9b0dceafffdafe1bcb791bf007e9409e51e5cca6d71e | CAND-5664e5b7c6b7a93ac02a7f27a0232ff513f282457ae7056ad06ac7a87c3f430f | [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>) |
| REQ-443 | REQ-e2198787a3bf0d0b9cccf0d6a403c423ee5ddf2c442dbee047c6b41f970fe238 | CAND-7aee1d495375912cd5549097c76e182df045d40ca73333de5751b0b4126407e5, CAND-7bb3e03cee1a1e2e3e8186753a4808d455c327b48d71aba2591ff3135482cc85 | [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>), [email\_report\_features\.eml](<../data/corpus/email_report_features.eml>) |
| REQ-444 | REQ-e232db84f6ac3702fbcf9c21b5950240207156619faab648f54686921672b66f | CAND-635ccdd5fb895245a950d18fd6fdb89c74f0797cfa517a043b96112ea4f4464a | [evergreen\_reference\_2009\.txt](<../data/corpus/evergreen_reference_2009.txt>) |
| REQ-445 | REQ-e26676d4799d8384065b88af0e33d7aba467b420e3732dc6a47af1d4a1ea0fbb | CAND-164438fbe48accb869f6b3804cb33fad34b8de9e9748cecedcb4c830e3d4716a | [evergreen\_reference\_2009\.txt](<../data/corpus/evergreen_reference_2009.txt>) |
| REQ-446 | REQ-e2db554d38f3a259cecbe1e6307b6a98451dedeb6b607ba8ac5cf996b5ca3114 | CAND-f57fe321b939800cda35c43a17b8ffe76d6308432deffddc7b22f6b5583ffe1c | [conversations/conv\_pines024\_inactive\_patrons\.eml](<../data/corpus/conversations/conv_pines024_inactive_patrons.eml>) |
| REQ-447 | REQ-e2eff6b1289d96bc472a9d3d168a8051671274c83c616d8b2facc3d0d52c74a4 | CAND-38347359ecd64e6f3b5259ee4662a4064320da13a262c77b8d49d2e7625929c5 | [interview\_cataloging\_2009-05-08\.txt](<../data/corpus/interview_cataloging_2009-05-08.txt>) |
| REQ-448 | REQ-e35ea609977c0d2a3d5fbfbc5159370bc498b31e12b22835dbfac2750e96099f | CAND-1d3d76e10504136345e256da383aa1d63e199b729b65196e3c778ef4ca11c116 | [evergreen\_reference\_2009\.txt](<../data/corpus/evergreen_reference_2009.txt>) |
| REQ-449 | REQ-e3efb036940ae38a74331cd1264012393e1a642ee1aa7f844b5008c6197a2f8d | CAND-9df1892823dbd97242e29618d71d67b7d47c32dac4c7eb78e7e0eb71d12390fa | [meeting\_tech\_subcommittee\_2009-06-30\.txt](<../data/corpus/meeting_tech_subcommittee_2009-06-30.txt>) |
| REQ-450 | REQ-e5e63226521d5090fd23cb5fdfce274284d697110f0f9548135d6d10f80e46bf | CAND-c68129e739b4c92aa50e9bec0220d181d11d2c1a903531983d35e63b4bd3096f | [conversations/conv\_pines018\_item\_transfer\.eml](<../data/corpus/conversations/conv_pines018_item_transfer.eml>) |
| REQ-451 | REQ-e69392fbdb660afaa2585affc41e908523213a9e0695ba6d1de65de2737b5482 | CAND-af93cfc45ae68c01a2efc96d2105648c520ed9611dc88a73ab05ba6e64909f7a | [evergreen\_reference\_2009\.txt](<../data/corpus/evergreen_reference_2009.txt>) |
| REQ-452 | REQ-e786ef7078d004253869bd50b4eb7077b2556dcaceccf0e8b760647dbdf6e9e4 | CAND-1c7e195090fa0c733afe5d72b2fb565ae726c10cf21dbb23261c93c5302dc7c7 | [survey\_results\_2009\.txt](<../data/corpus/survey_results_2009.txt>) |
| REQ-453 | REQ-e7cf89b6ef5a4cba4902252400a32e9ed09d14155896fa0ff4a876cb70aa0962 | CAND-e67f59422fc91d9411abb85fd19bb5ad9b6ac282aa2a98c8c943419c178853b7 | [email\_report\_features\.eml](<../data/corpus/email_report_features.eml>) |
| REQ-454 | REQ-e9ac467f7f798d1631dbbb0204c9c5d667add6f82e74d92fc43ced47aa0acaf4 | CAND-de58b8c437164bc93b4b4578e2fc3665089ebde96a731d654248585baf38870a | [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>) |
| REQ-455 | REQ-ea65a8ab239b0ed71a98a0d42b1e321f26841f296eba30e41151ece29387858a | CAND-357ef74055519c78e712f94b4a81eefdd6064a2c32e52de493a45ccd12a8c4fa | [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>) |
| REQ-456 | REQ-eaa5bc41986bdf9bf15d2098f529a34b840e38a20c8b02df9f56e9f5e6d4ff18 | CAND-c0b92045823be672ebe7726a1cd36d62fa756e7aa5ae70eb1a2bd58ba8cc131d | [meeting\_minutes/meeting\_2009-07-20\_minutes\.txt](<../data/corpus/meeting_minutes/meeting_2009-07-20_minutes.txt>) |
| REQ-457 | REQ-ec44a7ab77b20bde2aed2489d80e4f2d79779ec99ebaf3bfbf4494852dc775e4 | CAND-fd23fe468d01937a1a67ba67ed2e1b6b899d4bee995cc7e44fa16cdab110c4f9 | [interview\_sysadmin\_2009-05-10\.txt](<../data/corpus/interview_sysadmin_2009-05-10.txt>) |
| REQ-458 | REQ-ec99746c73ea325b9377fa69516b1e84635bc490e5e6d2cdd417932d624537a7 | CAND-9d9a05c21bb6fca74f17f3fc6b64e8e84056de6468e315b645b2601aad09a44e | [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>) |
| REQ-459 | REQ-ecbc769f1056fc694caf03cd44651294870989a7fdb0b0372ffb676fe218231a | CAND-23c416876ecd9ce780494ec760d72d69f02a06364b3a2e456964b91d3457cfcd | [email\_staff\_login\.eml](<../data/corpus/email_staff_login.eml>) |
| REQ-460 | REQ-ed845281f30d5a1ad35502abcd90eb5302c896ba4bd48aabb8f55e59f48b98f2 | CAND-848ebbec19c36e8ebee48b881f78c615995128fdc004b3c76e0b0e1890dc0746 | [evergreen\_reference\_2009\.txt](<../data/corpus/evergreen_reference_2009.txt>) |
| REQ-461 | REQ-ee2e7cfe007eeda5e1eaebe804e65e64436a08bae3fa68ecde19bddb975ab660 | CAND-e18a7b6c276d016b8a349ba15fe4f59be90a257dce29dad76e8cfdd59d1c6145 | [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>) |
| REQ-462 | REQ-ee35ed4a1232c864f30d2df70acdc1e1750dbeab7685fcd4ffd533ce1edba04d | CAND-37085161dec2e6b29610dd26689c9e2d08fbeab284a62e9498fc62a42e820102 | [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>) |
| REQ-463 | REQ-ee6eb9e9b5226aef379672a6fcdc30d5240e5c9a25af15f82908d72a4a4d5fc6 | CAND-a6d87c309aafb53488bf13e94f82a25008b83a337b2c738bcb15d21f2f42cf8f | [survey\_results\_2009\.txt](<../data/corpus/survey_results_2009.txt>) |
| REQ-464 | REQ-eee70acaa10499ac4166451351ac8e306ee26c103653513651a0d8dbb90f9df8 | CAND-8c83e75be4a91be35e1d7cb0479f58aecc37f1c44bff8af359d64a909c6f8ed2 | [meeting\_tech\_subcommittee\_2009-06-30\.txt](<../data/corpus/meeting_tech_subcommittee_2009-06-30.txt>) |
| REQ-465 | REQ-ef1d80f81aeb9f3593ccf2f674f9c52389c2232bbae655406da01de7c89f0fce | CAND-d84bd1c959ab64719c7ce6d9066186ddbc089dd72c1afbe5646847503dcc1b74 | [survey\_results\_2009\.txt](<../data/corpus/survey_results_2009.txt>) |
| REQ-466 | REQ-ef3ffc4360477da506e4e6425b314b838aa7fcb75b820b38cda49b4bcc065213 | CAND-d9f03b82dd5394344fa58c81d70d1b2533c407f3cd5838e5c538d5df8edfdf9f | [evergreen\_reference\_2009\.txt](<../data/corpus/evergreen_reference_2009.txt>) |
| REQ-467 | REQ-ef73c237684788b780936fdb29c0e7100bda45cf315bb857462f7e09f4e0e4b6 | CAND-5ceb110c0418391617aca28c5e638f6d5f66d658cf379df9cb24a10012e66191 | [conversations/conv\_pines022\_deletions\.eml](<../data/corpus/conversations/conv_pines022_deletions.eml>) |
| REQ-468 | REQ-f0720e53615fb8b41462a35963377ccdb09d901b776d6e24ef9da2bdc0a1041a | CAND-6f95be1136097dd3676b5540c9e1c90138178b67a7af50a56aecfd73141cb1f4 | [conversations/conv\_pines022\_deletions\.eml](<../data/corpus/conversations/conv_pines022_deletions.eml>) |
| REQ-469 | REQ-f0c4dec7239ca9e4e6db319fa16b4fbf95a3573b3f1dc2e24897a46b06a1a049 | CAND-a79b15ef4e3f9237dc25342f8aacf1a15a6dc0279bd0a3492759f83682e33899 | [evergreen\_reference\_2009\.txt](<../data/corpus/evergreen_reference_2009.txt>) |
| REQ-470 | REQ-f0deff9c2294e2aec763ffe5f14e3314c9b0c025357a9b11292fe3c6956deb6c | CAND-ccbd410d18c85bb72ff1403fb325c3b066aa72ccc18a5493f032300c728d1b15 | [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>) |
| REQ-471 | REQ-f183f04f55d29e8d4cf2d0a94ffdd2a082623a90bcddf40a6f1f4f1a1ce8b855 | CAND-185a6e51901dd1473b33e9c58ba8c9f4b477bcb2ce144a441beb7d6a0fe119e6 | [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>) |
| REQ-472 | REQ-f1c98bbddf05406115de6d84228ce345f45f91c9ea781172a4ec56b687bf6505 | CAND-3b2af2fb4f37fc16c7548620d95de3e506f97e041b1a9e09c7bc447454436319 | [conversations/conv\_pines016\_shelf\_space\.eml](<../data/corpus/conversations/conv_pines016_shelf_space.eml>) |
| REQ-473 | REQ-f204849fdbc1f4630bb2d3081320c2e4c4bd679fdd46b1b04a1847121c34b5eb | CAND-4c589dc6a0daa45b91ff36ce6840b521c7a54ad0f4e867445a101801f2e50bda | [conversations/conv\_pines019\_020\_missing\_intransit\.eml](<../data/corpus/conversations/conv_pines019_020_missing_intransit.eml>) |
| REQ-474 | REQ-f2244e790b412834b9f4cc3a456321c5719a8a053903f35831974228ee651f91 | CAND-a29f0b67c664ade4075700b7bf2d7bcf3fa8245bc215c07ec4c130619d4848be | [meeting\_tech\_subcommittee\_2009-06-30\.txt](<../data/corpus/meeting_tech_subcommittee_2009-06-30.txt>) |
| REQ-475 | REQ-f245d9515e6c1a8335b36be5d371ce164c76e95657e1444a17d62379986658b7 | CAND-f47d52a846ff1284a7220b4b60c1de90b2efe9ce24753370d8ee2b35bd56b7d6 | [email\_financial\_reports\.eml](<../data/corpus/email_financial_reports.eml>) |
| REQ-476 | REQ-f27f2affab23df0420adc0ff9e4833f353cd5994c641ef6f44174f65ed836ac0 | CAND-077695bb41756743b2b58dcb80ef6d2858c3e901f6447b7d1cd4cd568af20149 | [evergreen\_reference\_2009\.txt](<../data/corpus/evergreen_reference_2009.txt>) |
| REQ-477 | REQ-f2b2c28b88d4b43310f55eb8418ac71c4c37976ec835f0f3ebf3c0571f377b96 | CAND-d3fd2ac63df270bf49a8e15e18edf42901d440f19f5180153ee6158089399086 | [evergreen\_reference\_2009\.txt](<../data/corpus/evergreen_reference_2009.txt>) |
| REQ-478 | REQ-f316ec22a2a7a87ce60f2fbf46964094d078e89daf1060e04ccc374d17e3a719 | CAND-8fd53c5372cfa94f98f06de016a84c25f21ce4b5f511db756b2809e0c5352a3c | [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>) |
| REQ-479 | REQ-f3436ac1e95985f6e8b851214b890969ede14548ff8d723f5a4a4d7f4267f528 | CAND-013dddfee8e530f720e1cec8caea828be2aff401f52c51a9fb5e2000e9c630e0 | [conversations/conv\_pines015\_capacity\_interface\.eml](<../data/corpus/conversations/conv_pines015_capacity_interface.eml>) |
| REQ-480 | REQ-f38a510dae1618f355b641d6169156303b85e6a7f01a1aa92e6ba498d71ea3c4 | CAND-657aca844747054123a1fd421492ee631994e6473c818019285d64ceb4e486d0 | [email\_financial\_reports\.eml](<../data/corpus/email_financial_reports.eml>) |
| REQ-481 | REQ-f449b70934b5a2d0dd30ada53557fbe8ea2f8b3af91fccc9fc8f95b085b2b28c | CAND-042047faaf6cb5354ec24d7f6ded1ec29b5a9778d7355955d5b51e1f31c2bf42 | [meeting\_minutes/meeting\_2009-07-20\_minutes\.txt](<../data/corpus/meeting_minutes/meeting_2009-07-20_minutes.txt>) |
| REQ-482 | REQ-f4610c736073a06114b4ccd46e3a66eff83e454e16117c0d0d36031fbdd5483d | CAND-c8544ca0c414199e1b5c30bcaf22641939d19576b4ee2ef32a9a306bb9052cc3 | [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>) |
| REQ-483 | REQ-f4ebd30a18f50a61a95b253cec02f0311c26b4d994453324bc4b2c7700ae36bb | CAND-119b2191d10afac6808c3ea82a355becc29b8db56dbe3cc2abf40da44848c00c | [evergreen\_reference\_2009\.txt](<../data/corpus/evergreen_reference_2009.txt>) |
| REQ-484 | REQ-f509cab4cabc2a0227c5aa9ca01c5c4d31de17142cd8919ce15afa79757c8a03 | CAND-360ad5fe9709f7bc9935576fef35e302bab68c444437c4f9f14e1f443886d17c | [survey\_results\_2009\.txt](<../data/corpus/survey_results_2009.txt>) |
| REQ-485 | REQ-f55c38372edcdb8c9ae8a0864ba093d4c0633a4bfa3ba99a13f56fa6306c21ee | CAND-228b6eee0a67fb7cd1e0698e2b493fa9c75c9aeace137a235cec77578c73a9c1 | [evergreen\_reference\_2009\.txt](<../data/corpus/evergreen_reference_2009.txt>) |
| REQ-486 | REQ-f5954718142f9cb4e0cd5f6a701b9a0007cb6a426a3dad34e25733046e8d5f02 | CAND-5a7562025b68c460565f297950a247300989b019c4cc82637062ee8f35209a87 | [conversations/conv\_pines019\_020\_missing\_intransit\.eml](<../data/corpus/conversations/conv_pines019_020_missing_intransit.eml>) |
| REQ-487 | REQ-f7867afd8b8cffa993911556e129df9faa3f10b0a069dcddad38a26072bacdaa | CAND-dc7536fa423dce18119ad0f758d7f8f84144c4694e15d7d7fb626c74cb4a90a3 | [conversations/conv\_pines016\_shelf\_space\.eml](<../data/corpus/conversations/conv_pines016_shelf_space.eml>) |
| REQ-488 | REQ-f7a464b669aad12a2c4e7832e6069f26bdfa83d8b98ce36d317c273b7dc1d4fb | CAND-72ab73a9ea206b0e55e4c665e9f7bd0765e0ad7fe42dbebeb2d773fafa40a0d0 | [email\_staff\_login\.eml](<../data/corpus/email_staff_login.eml>) |
| REQ-489 | REQ-f86672270562466057f799a11a2a7e180a257767c7df6fa9de49224b677fdaa3 | CAND-46498c1e35b55ed80755bb9305b2dc48a04acf284f7dc39812411c7f530ea4b1 | [conversations/conv\_pines022\_deletions\.eml](<../data/corpus/conversations/conv_pines022_deletions.eml>) |
| REQ-490 | REQ-f9465ad48c7c802e7a16dd763ff61a32a190fe5b92c88920e48380f860057b80 | CAND-877c03879babd7c202432ef6f4fdcb24b0fe568ccbf39937ab565760d7d2fd73 | [meeting\_minutes/meeting\_2009-07-20\_minutes\.txt](<../data/corpus/meeting_minutes/meeting_2009-07-20_minutes.txt>) |
| REQ-491 | REQ-fb2f3effd8f915ef09a758f91efb601fb30c8c4d3281e40fcfdbde3923397c99 | CAND-096a96cdd6eafa945bc393456f7ac69755ce369e2e9edacef55a54c923deb260 | [evergreen\_reference\_2009\.txt](<../data/corpus/evergreen_reference_2009.txt>) |
| REQ-492 | REQ-fb3c6e949e2ae17e0b363be5e4b80b6c84aab64725449615d4a92e9ab0194126 | CAND-1ed92c8fd785efae8290fe19300a5ec86f30e8e91bd575b3b8a3c0d7319c539d | [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>) |
| REQ-493 | REQ-fba42c528f92883d601f4755dd305b9d3cc4f33f34cf071f3217eb9bef1ca595 | CAND-9ef1edbd32466031d633522508aa503fc2d146708111ba2276e1b4402282d913 | [conversations/conv\_pines023\_patron\_characteristics\.eml](<../data/corpus/conversations/conv_pines023_patron_characteristics.eml>) |
| REQ-494 | REQ-fe09c2b761b0d55259c7fb9e8ee0a506fda11a319aa135bdf1e9b311d335c6c7 | CAND-6719a2bb02e4df05838aaaa0ec06f92750d7271fdfebe4c2d23cf66bcadf35d4 | [evergreen\_reference\_2009\.txt](<../data/corpus/evergreen_reference_2009.txt>) |
| REQ-495 | REQ-fe39af0b4a06f57b550918d4ad8dc601c6ca7993a0cb349147922ec010c181ef | CAND-072c8a50a819c0bca3645205db02fb307bf3ceba3f377fb1d668e9f7c525b9e4, CAND-0e812cf02094db283a6a00b74e3acb324fa33ecc60b874f5bd3359943df82f8b | [conversations/conv\_pines021\_item\_purging\.eml](<../data/corpus/conversations/conv_pines021_item_purging.eml>), [interview\_cataloging\_2009-05-08\.txt](<../data/corpus/interview_cataloging_2009-05-08.txt>) |
| REQ-496 | REQ-fe3a9c6ab76dbcc714c2854e545190e84f5ef4cd34007c8395e132c33e0d52d8 | CAND-fde005d3da42fc059c16efef159b86fd353eed93fe509617196831ae235559bc | [conversations/conv\_pines016\_shelf\_space\.eml](<../data/corpus/conversations/conv_pines016_shelf_space.eml>) |
| REQ-497 | REQ-fff58904251da36eee185075862137c5e3de74e68126098296d007a5c077d37f | CAND-61f8d523ae63b026cca8c024ec246d9e78ce360b3bea61aac99884d6a8f75bfe | [conversations/conv\_pines014\_material\_volume\.eml](<../data/corpus/conversations/conv_pines014_material_volume.eml>) |

### Source inventory

- [conversations/conv\_pines014\_material\_volume\.eml](<../data/corpus/conversations/conv_pines014_material_volume.eml>) — DOC-f10d646016479a881ae8ff4ab4043844ee55a671d71f1943623db3fbb5589d8a
- [conversations/conv\_pines015\_capacity\_interface\.eml](<../data/corpus/conversations/conv_pines015_capacity_interface.eml>) — DOC-4acf2fdb375b86d49420e5743267e19b3f0af9ebe8bd764c1a88379aa9f5b662
- [conversations/conv\_pines016\_shelf\_space\.eml](<../data/corpus/conversations/conv_pines016_shelf_space.eml>) — DOC-b507e8abe1ba7c996c1d86d688e90bcf2404694ec00528c8361f26dfc8bd82f1
- [conversations/conv\_pines018\_item\_transfer\.eml](<../data/corpus/conversations/conv_pines018_item_transfer.eml>) — DOC-a47eb1f11286ff9099687b72a901e4a6ed2455b431087c0742aa78583c5bd80a
- [conversations/conv\_pines019\_020\_missing\_intransit\.eml](<../data/corpus/conversations/conv_pines019_020_missing_intransit.eml>) — DOC-b233b12122cae48b5821d685f6dc058d2d2e3cc8d7f77622fa4e7e55bddc5399
- [conversations/conv\_pines021\_item\_purging\.eml](<../data/corpus/conversations/conv_pines021_item_purging.eml>) — DOC-74ccbb6ac77183c0d1b34b1e79ed8fcbbfb4e7525cb33798c3af832fed733ad8
- [conversations/conv\_pines022\_deletions\.eml](<../data/corpus/conversations/conv_pines022_deletions.eml>) — DOC-7b8da7c05931fc99bc80d4a4bb0c8563e690e0c415b57f5ca1ae394462dc26c8
- [conversations/conv\_pines023\_patron\_characteristics\.eml](<../data/corpus/conversations/conv_pines023_patron_characteristics.eml>) — DOC-d2b26a6e7678ca4e82bfa7bb06566f329dea692ea22e8987b516fa8bc98c544b
- [conversations/conv\_pines024\_inactive\_patrons\.eml](<../data/corpus/conversations/conv_pines024_inactive_patrons.eml>) — DOC-705ab8a51bf22b7b619dae61bf8d2be1cf2487e749f13e7ac55fdde430357793
- [early\_draft\_srs\_galecia\.txt](<../data/corpus/early_draft_srs_galecia.txt>) — DOC-091180de9b2d4ea83267d989411ac89f415d4def3bbf7cd51651fb7fda8d8bf9
- [email\_financial\_reports\.eml](<../data/corpus/email_financial_reports.eml>) — DOC-8b6cfb3cf368b794d82567933f9c85062740814819b1e28b4837f6021cbcbee6
- [email\_report\_features\.eml](<../data/corpus/email_report_features.eml>) — DOC-d9e168e0c03903021bf9e636e1d8e5f56dfcb79cc110d3839e38175a7c54344e
- [email\_staff\_login\.eml](<../data/corpus/email_staff_login.eml>) — DOC-64b10e94c42508c5aea1af877ec9d2fe34485b099b29994b8b1a76cadc55e8b3
- [evergreen\_reference\_2009\.txt](<../data/corpus/evergreen_reference_2009.txt>) — DOC-e6aa9f8c6308ab748459f87b578a0df9df9c865b7911bac3686e865963b7af6f
- [interview\_cataloging\_2009-05-08\.txt](<../data/corpus/interview_cataloging_2009-05-08.txt>) — DOC-a79fab45108210e6bce7d92153dfcf055f2ef6b2cdab49a3f6f5717a3e35f29f
- [interview\_sysadmin\_2009-05-10\.txt](<../data/corpus/interview_sysadmin_2009-05-10.txt>) — DOC-b1738fd7a6de9498f19ede6747ba156ecb29ead86ad1c9a2768b53e862ece1a9
- [meeting\_minutes/meeting\_2009-03-15\_minutes\.txt](<../data/corpus/meeting_minutes/meeting_2009-03-15_minutes.txt>) — DOC-defef992db2ae0e10167fd94902eac93f82c59c4c070df030ca2f77811082818
- [meeting\_minutes/meeting\_2009-07-20\_minutes\.txt](<../data/corpus/meeting_minutes/meeting_2009-07-20_minutes.txt>) — DOC-5ab1dd8bc97af3b1ab2e378495f0e0d75fd501fcc19f923c0d8fda831074281b
- [meeting\_tech\_subcommittee\_2009-06-30\.txt](<../data/corpus/meeting_tech_subcommittee_2009-06-30.txt>) — DOC-e081aa7bd57bf5e59c75a8a86f592124757b74dff1ee0df4badc10c025092d96
- [survey\_results\_2009\.txt](<../data/corpus/survey_results_2009.txt>) — DOC-aac7bceef7a883652805583e98ec513b6ae2e7951e2ecfa18722127b1f12a5c4
