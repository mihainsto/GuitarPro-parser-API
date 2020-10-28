import guitarpro

def parse_tab(fileName):
  curl = guitarpro.parse(fileName)
  song = {}
  song['tracks'] = []
  song['tempo'] = curl.tempo
  song['tempoName'] = curl.tempoName

  for track in curl.tracks:
    thisTrack = {}
    thisTrack['offset'] = track.offset
    measures = []
    for measure in track.measures:
      thisMeasure = {}
      thisMeasure['start'] = measure.start
      voices = []
      for voice in measure.voices:
        thisVoice = {}
        beats = []
        for beat in voice.beats:
          thisBeat = {}
          thisBeat['duration'] = beat.duration.value
          thisBeat['start'] = beat.start
          notes = []
          for note in beat.notes:
            thisNote  = {}
            thisNote['value'] = note.value
            thisNote['string'] = note.string
            notes.append(thisNote)
          thisBeat['notes'] = notes
          beats.append(thisBeat)
        thisVoice['beats'] = beats
        voices.append(thisVoice)
      thisMeasure['voices'] = voices
      measures.append(thisMeasure)

    thisTrack["measures"] = measures
    song['tracks'].append(thisTrack)

  return song