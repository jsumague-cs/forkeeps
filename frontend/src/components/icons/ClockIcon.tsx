import Svg, { ClipPath, Defs, G, Path, Rect } from "react-native-svg";
import { colors } from "../../theme/colors";

type Props = {
  size?: number;
};

/** Figma icon 2016:170 — outer box 7.75 (scaled ×5/3 ≈ 13). */
export function ClockIcon({ size = 13 }: Props) {
  return (
    <Svg width={size} height={size} viewBox="0 0 7.75385 7.75385" fill="none">
      <G clipPath="url(#clockClip)">
        <Path
          d="M3.87692 7.1077C5.66123 7.1077 7.10769 5.66123 7.10769 3.87692C7.10769 2.09262 5.66123 0.646155 3.87692 0.646155C2.09262 0.646155 0.646153 2.09262 0.646153 3.87692C0.646153 5.66123 2.09262 7.1077 3.87692 7.1077Z"
          stroke={colors.primary}
          strokeWidth={0.646154}
          strokeLinecap="round"
          strokeLinejoin="round"
        />
        <Path
          d="M3.87692 1.93846V3.87692L5.16923 4.52308"
          stroke={colors.primary}
          strokeWidth={0.646154}
          strokeLinecap="round"
          strokeLinejoin="round"
        />
      </G>
      <Defs>
        <ClipPath id="clockClip">
          <Rect width={7.75385} height={7.75385} fill="white" />
        </ClipPath>
      </Defs>
    </Svg>
  );
}
