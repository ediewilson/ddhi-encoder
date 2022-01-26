A collection of command-line utilities to assist in the creation of
TEI-encoded oral history interviews for the Dartmouth Digital
History Initiative.

.. _ttu-encoder-1:

Installation
============

Use pip to install this package:

.. code:: bash

   pip install ttu-encoder

To peform named-entity tagging with ``ttu_tag``, you will need a Spacy
model. Before running ``ttu_tag``, install Spacy's small English model:

.. code:: bash

   python -m spacy download en_core_web_sm

See `the Spacy documentation <https://spacy.io/models>`__ for more
information.

Use
===


Use ``ttu_convert`` to transform a DOCX-encoded transcription into a
simply structured TEI document.

.. code:: bash

   ttu_convert ~/Desktop/transcripts/zien_jimmy_transcript_final.docx -o tmp.tei.xml

Use ``ttu_tag`` to add named-entity tags to a TEI-encoded
transcription:

.. code:: bash

   ttu_tag -o zien.tei.xml tmp.tei.xml

Encoders are then expected to edit the text of the interview,
correcting automatically generated named-entity tags and adding new
ones.

Use ``ttu_generate_standoff`` to  create a ``<standOff>`` element in the
interview and link the entities to names in the text.

Use ``ttu_mentioned_places`` to extract the places in a TEI file's
standoff markup and print it as tab-separated values:

.. code:: bash

	  ttu_mentioned_places lovely.tei.xml > lovely.tsv

Then use OpenRefine or another tool to refine this list with
identifiers and other metadata.

Use ``ttu_update_places`` to update the places in a TEI file's
standoff markup with identifiers and geo-coordinates obtained via
OpenRefine or other procedure:

.. code:: bash

	  ttu_update_places lovely.tei.xml lovely_updates.tsv >
	  updated_lovely.tei.xml
	  
Similarly, use ``ttu_mentioned_events`` and ``ttu_update_events`` to
perform the same operations for events.
